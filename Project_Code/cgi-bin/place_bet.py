#!/usr/bin/python
import cgi, cgitb, json, sys

form = cgi.FieldStorage()
title = form.getvalue("title")
volume = int(form.getvalue("Volume"))
choice = form.getvalue("Type")

with open("../fake-backend/db.json", "r") as f:
	json_obj = json.load(f)

for i in range(0, volume):
	if choice == "Over":
		json_obj[title]["Bet_History"].append(float(json_obj[title]["Bet_History"][len(json_obj[title]["Bet_History"]) - 1]) + .1)
	else:
		json_obj[title]["Bet_History"].append(float(json_obj[title]["Bet_History"][len(json_obj[title]["Bet_History"]) - 1]) - .1)

json_obj[title]["Current_Price"] = json_obj[title]["Bet_History"][len(json_obj[title]["Bet_History"]) - 1]

with open("../fake-backend/db.json", "w") as f:
	json.dump(json_obj, f)