/#!/usr/bin/python
import cgi, cgitb, json, sys

form = cgi.FieldStorage()
name = form.getvalue("name")
desc = form.getvalue("desc")
auth = form.getvalue("auth")

with open("../fake-backend/db.json", "r") as f:
	json_obj = json.load(f)

newProposal = {}
newProposal['Description'] = desc
newProposal['Author'] = auth
newProposal['Donations'] = []
newProposal['Current_Price'] = 0
newProposal['Bet_History'] = []
newProposal['Funding_Level'] = 0
json_obj[name] = newProposal

with open("../fake-backend/db.json", "w") as f:
	json.dump(json_obj, f)