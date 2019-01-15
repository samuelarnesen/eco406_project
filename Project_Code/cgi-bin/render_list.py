#!/usr/bin/python
import json

print "Content-type: text/html\n\n"

with open("../fake-backend/db.json", "r") as f:
	json_obj = json.load(f)

with open("../pages/list_proposals.html") as g:
	for line in g:
		print(line)
		split_line = line.split()
		if len(split_line) > 0:
			if line.split()[0] == "</center>":
				break

	print("<script> if (location.href.indexOf('reload')==-1){location.href=location.href+'?reload';}</script>")

	for i in json_obj:
		title = i
		if len(title) > 50:
			title = title[:50] + "..."
		print("<div id='box'>")
		print("\t<a href=\"render_proposal.py?title=" + i + "\">"),
		print("<span> " + title + "</b></span></a>")
		print("</div>")

	print("<div class=\"btn-group\">")
	print("<button class=\"button button1\" onclick=\"window.location.replace('../pages/submit_proposal.html')\">Submit Proposal!</button>")
	print("</div>")

	print("</body>")
	print("</html>")

