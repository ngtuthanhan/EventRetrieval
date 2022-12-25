import os
from os import listdir
all_file = [f for f in listdir("./submission")]
for file in all_file:
    os.rename("./submission/" + file,"./submission/" +"query-" + file)