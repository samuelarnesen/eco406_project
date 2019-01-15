import json

db = dict()
with open("projects_for_db", "r") as f:
	count = 0
	title = ""
	for line in f:
		if len(line) > 0:
			if line[0][0] != '\n':
				real_line = line
				if real_line[len(real_line) - 1] == "\n":
					real_line = real_line[:len(real_line) - 1]
				if count % 3 == 0:
					title = real_line
					db[title] = dict()
				if count % 3 == 1:
					db[title]["Description"] = real_line
				if count % 3 == 2:
					db[title]["Author"] = real_line
					db[title]["Current_Price"] = 0.5
					db[title]["Bet_History"] = [0]
					db[title]["Donations"] = []
					db[title]["Funding_Level"] = 0.0
				count += 1

print(json.dumps(db))
