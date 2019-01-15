#! /usr/bin/python
import json

print "Content-type: text/html\n\n"

with open("../fake-backend/db.json", "r") as f:
	json_obj = json.load(f)


with open("../pages/list_proposals.html", "r") as g:
	for line in g:
		print(line)
		split_line = line.split()
		if len(split_line) > 0:
			if line.split()[0] == "<body>":
				break

	for i in json_obj:
		print("<div id='box'>")
		print("\t<a href=\"render_proposal.py?title=" + "Project One" + "\">"),
		print("<span> " + i + " <b> by </b> " + json_obj[i]["Author"] + " </b></span></a>")
		print("</div>")

	print("</body>")
	print("</html>")
		#print "Hello world!"

#print "Hello world!!"