from flask import Flask, render_template, request, json, jsonify

app = Flask(__name__)

@app.route('/')
def startpage():
    with open('database.json') as json_file:
        data = json.load(json_file)
        activities = data["activity"]
    return render_template("index.html", activities=activities)

@app.route('/addactivity', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        search = request.form['searching']
        with open('database.json') as json_file:
            data = json.load(json_file)
            count = 0
            noactivity = "Det fanns ingen aktivitet med det namnet!"
            activities = data["activity"]
            for activity in activities:
                print count
                print len(activities) - 1
                if activity["name"] == search:
                    activity["pos"] = count
                    return render_template("addactivity.html", activity=activity)
                if activity["name"] != search and count == len(activities) - 1:
                    return render_template("done.html", noactivity = noactivity)
                count += 1



    else:
        return render_template("addactivity.html")

@app.route('/edit', methods = ['POST', 'GET'])
def edit():
    return render_template("edit.html")

@app.route('/res', methods = ['POST', 'GET'])
def resy():
    search = request.form['searchy']
    with open('database.json') as json_file:
        data = json.load(json_file)
        activities = data["activity"]
        noactivity = "Det fanns inget aktivitet med det namnet!"
        for t in activities:
            if t["name"] == search:
                return render_template("activities.html", t=t)
        return render_template("done.html", noactivity = noactivity)

@app.route('/activities')
def search():
    with open('database.json') as json_file:
        data = json.load(json_file)
        activities = data["activity"]
        return render_template("activities.html", activities=activities)

@app.route('/updated', methods = ['POST', 'GET'])
def updated():
    if request.method == 'POST':
        name = request.form['name']
        player1 = request.form['player1']
        player2 = request.form['player2']
        player3 = request.form['player3']
        player4 = request.form['player4']
        player5 = request.form['player5']
        location = request.form['location']
        time = request.form['time']
        contact = request.form['contact']
        pos = int(request.form['pos'])
        update_team_json(pos, name, player1, player2, player3, player4, player5, location, time, contact)
        return render_template("updated.html", name=name)

@app.route('/done', methods = ['POST', 'GET'])
def done():
    if request.method == 'POST':
        name = request.form['name']
        player1 = request.form['player1']
        player2 = request.form['player2']
        player3 = request.form['player3']
        player4 = request.form['player4']
        player5 = request.form['player5']
        location = request.form['location']
        time = request.form['time']
        contact = request.form['contact']
        add_team_json(name, player1, player2, player3, player4, player5, location, time, contact)
        return render_template("done.html", name=name)

def add_team_json(name, player1, player2, player3, player4, player5, location, time, contact):
    data = {"name":name, "player1":player1, "player2": player2, "player3": player3, "player4": player4, "player5":player5, "location":location, "time":time, "contact":contact}
    with open('database.json') as json_file:
        user = json.load(json_file)
        user["activity"].append(data)
    with open("database.json", "w") as json_file:
        json.dump(user, json_file, indent=3)
    pass

def update_team_json(pos, name, player1, player2, player3, player4, player5, location, time, contact):
    with open('database.json', 'r') as f:
        json_data = json.load(f)
        activity = json_data["activity"][pos]
        activity['name'] = name
        activity['player1'] = player1
        activity['player2'] = player2
        activity['player3'] = player3
        activity['player4'] = player4
        activity['player5'] = player5
        activity['location'] = location
        activity['time'] = time
        activity['contact'] = contact
        json_data["activity"][pos] = activity
    with open('database.json', 'w') as f:
        json.dump(json_data, f, indent=3)
    pass

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
