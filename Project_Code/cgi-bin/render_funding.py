#!/usr/bin/python
import cgi, cgitb, json

form = cgi.FieldStorage() 
title = form.getvalue("title")

#project = form.getvalue("Project_Name")
with open("../fake-backend/db.json", "r") as f:
	json_obj = json.load(f)

replacement = dict()
if title in json_obj:
	 replacement = json_obj[title]
	 replacement["Title"] = title

print "Content-type: text/html\n\n"
with open("../pages/fund_page.html") as f:
	for line in f:
		split_line = line.split()
		if len(split_line) > 1:
			if split_line[1][0] == '#':
				print(split_line[0] + " " + str(replacement[split_line[2]]) + " " + split_line[len(split_line) - 1])
			elif split_line[0] == "document.ReviewForm.title.value":
				print("document.ReviewForm.title.value =" + " \"" +  replacement["Title"] + "\";")
			elif split_line[0] == "document.FundItForm.title.value":
				print("document.FundItForm.title.value =" + " \"" +  replacement["Title"] + "\";")
			else:
				print(line)
		else:
			print(line)