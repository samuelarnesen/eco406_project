#!/usr/bin/python
import cgi, cgitb, json

form = cgi.FieldStorage() 
title = form.getvalue("title")

#project = form.getvalue("Project_Name")
f = open("./fake-backend/db.json", "r")
json_obj = json.load(f)

replacement = dict()
replacement["Title"] = "DUMMY PROJECT"
replacement["Author"] = "Sam Arnesen"
replacement["Description"] = "This is a dummy project"

if title in json_obj:
	 replacement = json_obj[title]
	 replacement["Title"] = title


with open("./pages/bet_page.html") as f:
	for line in f:
		split_line = line.split()
		if len(split_line) > 1:
			if split_line[1][0] == '#':
				print(split_line[0] + " " + str(replacement[split_line[2]]) + " " + split_line[len(split_line) - 1])
			elif split_line[0] == "document.ReviewForm.title.value":
				print("document.ReviewForm.title.value =" + " \"" +  replacement["Title"] + "\";")
			elif split_line[0] == "document.FundForm.title.value":
				print("document.FundForm.title.value =" + " \"" +  replacement["Title"] + "\";")
			elif split_line[0] == "document.PlaceBetForm.title.value":
				print("document.PlaceBetForm.title.value =" + " \"" +  replacement["Title"] + "\";")
			else:
				print(line)
		else:
			print(line)