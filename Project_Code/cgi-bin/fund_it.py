#!/usr/bin/python
import cgi, cgitb, json, math

form = cgi.FieldStorage()
title = form.getvalue("title")
amount = form.getvalue("amount")

with open("../fake-backend/db.json", "r") as f:
	json_obj = json.load(f)

json_obj[title]["Donations"].append(float(amount))

current_funding_level = 0
for i in json_obj[title]["Donations"]:
	current_funding_level += math.sqrt(float(i))
current_funding_level = current_funding_level**2

str_fund = str(current_funding_level)
split_fund = str_fund.split(".")
str_fund = "$" + split_fund[0] + "."
if len(split_fund) > 1:
	if len(split_fund[1]) > 1:
		str_fund += split_fund[1][0:2]
	else:
		str_fund += split_fund[1][0] + "0"
else:
	str_fund += "00"

json_obj[title]["Funding_Level"] = str_fund

with open("../fake-backend/db.json", "w") as f:
	json.dump(json_obj, f)

