import json
with open("./Unit.json", "r") as file:
    data = json.loads(file.read())
    file.close()

with open("./temp.html", "w+") as file:
    for key in data:
        file.write("<tr>\n\t<td>" + key.title() + "</td>\n\t<td><input type=\"text\" name=\"" + key + "\"/></td>\n</tr>\n")