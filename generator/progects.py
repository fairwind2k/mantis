import string
import random
import os.path
from model.project import Project
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "p:f:", ["number of pojects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

p = 1
f = "data/projects.json"

for o, a in opts:
    if o == "-p":
        p = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.digits
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata =[Project(name=random_string("name", 10)) for i in range(p)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,"w") as out:
    jsonpickle.set_encoder_options("json", indent=1)
    out.write(jsonpickle.encode(testdata))
    # out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))