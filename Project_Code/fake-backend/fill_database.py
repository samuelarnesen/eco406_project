import json

thing = dict()

thing["Project One"] = dict()
thing["Project Two"] = dict()
thing["Project Three"] = dict()

thing["Project One"]["Author"] = "Sam"
thing["Project Two"]["Author"] = "Shreyas"
thing["Project Three"]["Author"] = "Nick"

thing["Project One"]["Description"] = "This is the description for Project One"
thing["Project Two"]["Description"] = "This is the description for Project Two"
thing["Project Three"]["Description"] = "This is the description for Project Three"

thing["Project One"]["Current_Price"] = 0.76
thing["Project Two"]["Current_Price"] = 0.65
thing["Project Three"]["Current_Price"] = 0.98

thing["Project One"]["Bet_History"] = [.5, .6, .7, .8, .75, .77, .76]
thing["Project Two"]["Bet_History"] = [.5, .6, .7, .65]
thing["Project Three"]["Bet_History"] = [.5, .6, .7, .8, .9, .95, .98]

thing["Project One"]["Donations"] = [5, 7, 2, 4, 5]
thing["Project Two"]["Donations"] = [1, 2, 1]
thing["Project Three"]["Donations"] = [8, 3, 2, 6, 4, 8, 12, 3]

thing["Project One"]["Funding_Level"] = 111.0
thing["Project Two"]["Funding_Level"] = 12.0
thing["Project Three"]["Funding_Level"] = 340.0

print(json.dumps(thing))