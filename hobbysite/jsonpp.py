#!/usr/bin/python -tt
import sys
import json


def jsonpp(jsonfile):
  jf = open(jsonfile)
  data = json.loads(jf.read())
  print(json.dumps(data, indent=4, separators=(',',':')))


if __name__ == "__main__":
  if (len(sys.argv) > 1):
    jsonpp(sys.argv[1])
