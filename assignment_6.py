from flask import Flask, render_template, request, json, jsonify

app = Flask(__name__)
#this website is a prototype for a webpage for team-communications or small tournaments. teams can get information about other teams
#and so on. there is possiblities to get information about teams in json aswell.

#startpage with information and search-possibility.
@app.route('/')
def startpage():
    with open('database.json') as json_file:
        data = json.load(json_file)
        teams = data["teams"]
    return render_template("index.html", teams=teams)

#the add-team route is taking care of input to the database. it also handles the
#editpages entries.
@app.route('/addteam', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        search = request.form['searching']
        with open('database.json') as json_file:
            data = json.load(json_file)
            count = 0
            noteam = "Det fanns inget lag med det namnet!"      #message for no team
            teams = data["teams"]
            for searchedteam in teams:                          #search for the team in the dictionary we gotten from the jsonfile
                if searchedteam["teamname"] == search:
                    searchedteam["pos"] = count                 #count to make sure that we configure the right team in the jsonfile
                    return render_template("addteam.html", searchedteam=searchedteam)
                    count += 1
            return render_template("done.html", noteam = noteam)


    else:
        return render_template("addteam.html")

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
        teams = data["teams"]
        noteam = "Det fanns inget lag med det namnet!"
        for t in teams:
            if t["teamname"] == search:                     #searches for team - if team has the same name as the search
                return render_template("teams.html", t=t)       #send to resultpage with the team
        return render_template("done.html", noteam = noteam)        #give message about that the team dosent exist in json-database

#resultpage for all teams
@app.route('/teams')
def search():
    with open('database.json') as json_file:
        data = json.load(json_file)
        teams = data["teams"]
        return render_template("teams.html", teams=teams)

#extra functionality - if someone knows the teamname, they can just enter the name in the url if they write like url/team/Balsta Boys.
@app.route('/teams/<teamname>')
def searchteam(teamname):
    with open('database.json') as json_file:
        data = json.load(json_file)
        teams = data["teams"]
        for t in teams:
            if t["teamname"] == teamname:
                return render_template("teams.html", t=t)

#update-page to tell the user that information has been updated
@app.route('/updated', methods = ['POST', 'GET'])
def updated():
    if request.method == 'POST':            #request all the info that could be updated
        teamname = request.form['teamname']
        player1 = request.form['player1']
        player2 = request.form['player2']
        player3 = request.form['player3']
        player4 = request.form['player4']
        player5 = request.form['player5']
        comment = request.form['comment']
        tele = request.form['tele']
        email = request.form['email']
        pos = int(request.form['pos'])      #converts the indice to an int
        update_team_json(pos, teamname, player1, player2, player3, player4, player5, comment, tele, email)#sends to the method
        return render_template("updated.html", teamname=teamname)

#done-page that gives feedback to user regarding adding a new team to the database.
@app.route('/done', methods = ['POST', 'GET'])
def done():
    if request.method == 'POST':                #requests all fields
        teamname = request.form['teamname']
        player1 = request.form['player1']
        player2 = request.form['player2']
        player3 = request.form['player3']
        player4 = request.form['player4']
        player5 = request.form['player5']
        comment = request.form['comment']
        tele = request.form['tele']
        email = request.form['email']
        add_team_json(teamname, player1, player2, player3, player4, player5, comment, tele, email) #sends to method
        return render_template("done.html", teamname=teamname)

#add_team_json adds teams to the database.json-file.
def add_team_json(teamname, player1, player2, player3, player4, player5, comment, tele, email):
    data = {"teamname":teamname, "player1":player1, "player2": player2, "player3": player3, "player4": player4, "player5":player5, "comment":comment, "tele":tele, "email":email}
    with open('database.json') as json_file:
        user = json.load(json_file)
        user["teams"].append(data)
    with open("database.json", "w") as json_file:
        json.dump(user, json_file, indent=3)
    pass
#updates team information in the jsonfile.
def update_team_json(pos, teamname, player1, player2, player3, player4, player5, comment, tele, email):
    with open('database.json', 'r') as f:
        json_data = json.load(f)
        team = json_data["teams"][pos]  #finds proper element
        team['teamname'] = teamname
        team['player1'] = player1
        team['player2'] = player2
        team['player3'] = player3
        team['player4'] = player4
        team['player5'] = player5
        team['comment'] = comment
        team['tele'] = tele
        team['email'] = email
        json_data["teams"][pos] = team  #updates proper element with new information
    with open('database.json', 'w') as f:
        json.dump(json_data, f, indent=3)


#jsonify converts the dictionary to a jsonobject
@app.route('/api/teams')
def users():
    with open('database.json') as json_file:
        users = json.load(json_file)
        return jsonify(users)

#finds a team by entering a team-name in the url. this way it is easier for a users
# of this website to make jsoncalls to our website
@app.route('/api/teams/<teamname>')
def findusers(teamname):
    with open('database.json') as json_file:
        data = json.load(json_file)
        teams = data["teams"]
        for t in teams:
            if t["teamname"] == teamname:
                return jsonify(t)

#errorhandler for the 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
