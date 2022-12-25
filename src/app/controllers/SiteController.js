const Course = require("../models/Course");
const { mutipleMongooseToObject } = require("../../util/mogoose");

const fs = require("fs");
const exec = require("exec");

class SiteController {
  // [GET] /
  index(req, res, next) {
    fs.readFile("./model2/Ans_query.json", (err, data) => {
      if (err) throw err;
      var frameid = JSON.parse(data);
      
      Course.find({ IDFrame: frameid})
        .then((courses) => {
          var courses_order = [];
          for (let i = 0; i < frameid.length; i++){
            for (let j = 0; j < courses.length; j++){
              if (frameid[i] == courses[j].IDFrame) {
                courses_order.push(courses[j])
              }
            }
          }
          res.render("home",{ 
            courses: mutipleMongooseToObject(courses_order),
          });
        })
        .catch(next);
    });
  }

  // [GET] /search
  search(req, res) {
    res.render("search");
  }

  // [POST] / or /search
  getData(req, res, next) {
    var query = req.body;
    var English = query["English"];
    var data = JSON.stringify(query);
    fs.writeFileSync('./model2/Query.json', data);
    fs.writeFile("./model2/Query.txt", English, (err) => {
      if (err) {
        console.error(err);
      }
    });
    
    res.redirect('/')
  }

  // [GET] /Detail/:slug
  showDetail(req, res, next) {
    Course.findOne({ IDFrame: req.params.idframe })
        .then((course) => {
            var PositionFrame = course.PositionFrame
            var PositionFrames = []
            for (let i = 0; i < 25; i++){
              PositionFrames.push(PositionFrame - 12 + i)
            }
            Course.find({ Batch: course.Batch, VideoID: course.VideoID, PositionFrame: PositionFrames}).sort( { PositionFrame: 1 } )
              .then((courses) => {
                res.render('detail', {
                  courses: mutipleMongooseToObject(courses),
                });
              })
              .catch(next);
        })
        .catch(next);
  }

  // [GET] /KNN/:slug
  showKNN(req, res, next) {
    Course.findOne({ IDFrame: req.params.idframe })
        .then((course) => {
            var PositionFrame = course.PositionFrame
            var PositionFrames = []
            for (let i = 0; i < 25; i++){
              PositionFrames.push(PositionFrame - 12 + i)
            }
            Course.find({ Batch: course.Batch, VideoID: course.VideoID, PositionFrame: PositionFrames}).sort( { PositionFrame: 1 } )
              .then((courses) => {
                res.render('detail', {
                  courses: mutipleMongooseToObject(courses),
                });
              })
              .catch(next);
        })
        .catch(next);
  }
}

module.exports = new SiteController();
