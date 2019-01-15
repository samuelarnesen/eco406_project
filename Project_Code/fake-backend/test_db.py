import json 
dictionary = json.load(open("db.json"))
count = 1
for i in dictionary:
	print(count)
	count += 1