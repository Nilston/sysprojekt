from flask import Flask, render_template, request, json, jsonify

app = Flask(__name__)
#this website is a prototype for a webpage for team-communications or small tournaments. teams can get information about other teams
#and so on. there is possiblities to get information about teams in json aswell.

#startpage with information and search-possibility.
@app.route('/')
def startpage():
    with open('database.json') as json_file:
        data = json.load(json_file)
        activities = data["activity"]
    return render_template("index.html", activities=activities)

#the add-team route is taking care of input to the database. it also handles the
#editpages entries.
@app.route('/addactivity', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        search = request.form['searching']
        with open('database.json') as json_file:
            data = json.load(json_file)
            count = 0
            noactivity = "Det fanns ingen aktivitet med det namnet!"      #message for no team
            activities = data["activity"]
            for activity in activities:                          #search for the team in the dictionary we gotten from the jsonfile
                print count
                print len(activities) - 1
                if activity["name"] == search:
                    activity["pos"] = count                 #count to make sure that we configure the right team in the jsonfile
                    return render_template("addactivity.html", activity=activity)
                if activity["name"] != search and count == len(activities) - 1:
                    return render_template("done.html", noactivity = noactivity)
                count += 1



    else:
        return render_template("addactivity.html")

#editpage for editing the information in the teams
@app.route('/edit', methods = ['POST', 'GET'])
def edit():
    return render_template("edit.html")

#resultpage for the teamsearch
@app.route('/res', methods = ['POST', 'GET'])
def resy():
    search = request.form['searchy']
    with open('database.json') as json_file:
        data = json.load(json_file)
        activities = data["activity"]
        noactivity = "Det fanns inget aktivitet med det namnet!"
        for t in activities:
            if t["name"] == search:                     #searches for team - if team has the same name as the search
                return render_template("activities.html", t=t)       #send to resultpage with the team
        return render_template("done.html", noactivity = noactivity)        #give message about that the team dosent exist in json-database

#resultpage for all teams
@app.route('/activities')
def search():
    with open('database.json') as json_file:
        data = json.load(json_file)
        activities = data["activity"]
        return render_template("activities.html", activities=activities)

#update-page to tell the user that information has been updated
@app.route('/updated', methods = ['POST', 'GET'])
def updated():
    if request.method == 'POST':            #request all the info that could be updated
        name = request.form['name']
        player1 = request.form['player1']
        player2 = request.form['player2']
        player3 = request.form['player3']
        player4 = request.form['player4']
        player5 = request.form['player5']
        location = request.form['location']
        time = request.form['time']
        contact = request.form['contact']
        pos = int(request.form['pos'])      #converts the indice to an int
        update_team_json(pos, name, player1, player2, player3, player4, player5, location, time, contact)#sends to the method
        return render_template("updated.html", name=name)

#done-page that gives feedback to user regarding adding a new team to the database.
@app.route('/done', methods = ['POST', 'GET'])
def done():
    if request.method == 'POST':                #requests all fields
        name = request.form['name']
        player1 = request.form['player1']
        player2 = request.form['player2']
        player3 = request.form['player3']
        player4 = request.form['player4']
        player5 = request.form['player5']
        location = request.form['location']
        time = request.form['time']
        contact = request.form['contact']
        add_team_json(name, player1, player2, player3, player4, player5, location, time, contact) #sends to method
        return render_template("done.html", name=name)

#add_team_json adds teams to the database.json-file.
def add_team_json(name, player1, player2, player3, player4, player5, location, time, contact):
    data = {"name":name, "player1":player1, "player2": player2, "player3": player3, "player4": player4, "player5":player5, "location":location, "time":time, "contact":contact}
    with open('database.json') as json_file:
        user = json.load(json_file)
        user["activity"].append(data)
    with open("database.json", "w") as json_file:
        json.dump(user, json_file, indent=3)
    pass
#updates team information in the jsonfile.
def update_team_json(pos, name, player1, player2, player3, player4, player5, location, time, contact):
    with open('database.json', 'r') as f:
        json_data = json.load(f)
        activity = json_data["activity"][pos]  #finds proper element
        activity['name'] = name
        activity['player1'] = player1
        activity['player2'] = player2
        activity['player3'] = player3
        activity['player4'] = player4
        activity['player5'] = player5
        activity['location'] = location
        activity['time'] = time
        activity['contact'] = contact
        json_data["activity"][pos] = activity  #updates proper element with new information
    with open('database.json', 'w') as f:
        json.dump(json_data, f, indent=3)
    pass

#errorhandler for the 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
