#!/usr/bin/python
import cgi, cgitb, json, sys

form = cgi.FieldStorage()
user = form.getvalue("user")
pw = form.getvalue("pw")

with open("../fake-backend/logins.json", "r") as f:
	json_obj = json.load(f)

g = open("../pages/next.html", 'w')

if user not in json_obj:
	g.write("<html><body><script>window.location.href = 'loginFailed.html';</script></body></html>")
	print('failed')
else:
	if pw not in json_obj[user]["password"]:
		g.write("<html><body><script>window.location.href = 'loginFailed.html';</script></body></html>")
		print('failed')	
	else:
		g.write("<html><body><script>window.location.href = '../cgi-bin/render_list.py';</script></body></html>")
		print('workd')	
g.close()