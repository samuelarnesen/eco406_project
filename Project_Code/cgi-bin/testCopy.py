#! /usr/bin/python
import cgi, cgitb, json

with open("../fake-backend/db.json", "r") as f:
	json_obj = json.load(f)