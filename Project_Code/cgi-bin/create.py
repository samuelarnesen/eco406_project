#!/usr/bin/python
import cgi, cgitb, json, sys

form = cgi.FieldStorage()
user = form.getvalue("user")
pw = form.getvalue("pw")
bio = form.getvalue("bio")

with open("../fake-backend/logins.json", "r") as f:
	json_obj = json.load(f)

newUser = {}
newUser['password'] = pw
newUser['education'] = bio
json_obj[user] = newUser

with open("../fake-backend/logins.json", "w") as f:
	json.dump(json_obj, f)