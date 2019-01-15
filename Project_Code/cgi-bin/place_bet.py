#!/usr/bin/python
import cgi, cgitb, json, sys

def calculate(win, current_score, volume):
	new_score = current_score
	if win: 
		new_score += (10 * volume) / (1 + 10**(current_score / 400));
	else:
		new_score -= (10 * volume) / (1 + 10**((-1 * current_score) / 400));
	return new_score


form = cgi.FieldStorage()
title = form.getvalue("title")
volume = int(form.getvalue("Volume"))
choice = form.getvalue("Type")

with open("../fake-backend/db.json", "r") as f:
	json_obj = json.load(f)

#for i in range(0, volume):
#	if choice == "Over":
#		json_obj[title]["Bet_History"].append(float(json_obj[title]["Bet_History"][len(json_obj[title]["Bet_History"]) - 1]) + .1)
#	else:
#		json_obj[title]["Bet_History"].append(float(json_obj[title]["Bet_History"][len(json_obj[title]["Bet_History"]) - 1]) - .1)
length = len(json_obj[title]["Bet_History"])
json_obj[title]["Bet_History"].append(calculate(choice=="Over", float(json_obj[title]["Bet_History"][length - 1]), volume))
json_obj[title]["Current_Price"] = 1 / (1 + 100**(-1 * float(json_obj[title]["Bet_History"][length]) / 400))
if len(str(json_obj[title]["Current_Price"])) > 5:
	if str(json_obj[title]["Current_Price"])[5] != ".":
		json_obj[title]["Current_Price"] = str(json_obj[title]["Current_Price"])[0:5]
#json_obj[title]["Current_Price"] = json_obj[title]["Bet_History"][len(json_obj[title]["Bet_History"]) - 1]

with open("../fake-backend/db.json", "w") as f:
	json.dump(json_obj, f)