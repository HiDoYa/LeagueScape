import json, sys

file_name = sys.argv[1]
file_open = open(file_name, "r")
jsonfile = json.loads(file_open.read())

for x in jsonfile:
    print('{1:<{0}}'.format(20, x["team"]) + '  ' + x["score"])