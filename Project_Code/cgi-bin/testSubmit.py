#! /usr/bin/python
import cgi, cgitb, json

form = cgi.FieldStorage()
name = form.getvalue("name")
desc = form.getvalue("desc")
auth = form.getvalue("auth")

print "Content-type: text/html\n\n"

with open("../fake-backend/db.json", "r") as f:
	json_obj = json.load(f)

newProposal = {}
newProposal['Description'] = desc
newProposal['Author'] = auth
newProposal['Donations'] = []
newProposal['Current_Price'] = 0
newProposal['Bet_History'] = [0]
newProposal['Funding_Level'] = 0
json_obj[name] = newProposal


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
with open("../fake-backend/db.json", "w") as f:
	json.dump(json_obj, f)

#print "Hello world!!"