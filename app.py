import uuid, random, requests, urllib.parse
from flask import Flask, render_template, redirect, url_for, request, session
from lib import getData, getDataJSON, saveDataJSON

app = Flask(__name__)
app.secret_key = b'6b1c2d979b55431bdc13c133bc026c80311b606aad7f3987b6638970bff1a5e1'

@app.errorhandler(404)
def notfound(e):
    return render_template("notfound.html")

@app.route("/")
def index():
    """if request.args.get('lang', default="fr") == None:
        translatedText = {}

        headers = {
            "Authorization": "DeepL-Auth-Key 9b267d6b-166b-e365-0c72-8a1c7563d476:fx",
            "Content-Type": "x-www-form-urlencoded"
        }
        requestData = {
            "text": urllib.parse.quote_plus()
        }

        return render_template("translateindex.html", translatedText=translatedText)"""
    return render_template("index.html", lang=request.args.get('lang', default="fr"))

@app.route("/game")
def game():
    userID = id = str(uuid.uuid4())
    factsIDS = getData("Game", "ID", None, None)
    factsChosen = []
    context = []

    for i in range(5):
        correctResponseID = random.choice(factsIDS)[0]
        while correctResponseID in factsChosen:
            correctResponseID = random.choice(factsIDS)[0]
        factsChosen.append(correctResponseID)

        fact = getData("Game", "*", "ID", correctResponseID)
        correctReponse = fact[1]
        monsterDialog = fact[2]
        badResponse1 = fact[3]
        badResponse2 = fact[4]
        badResponse3 = fact[5]
        badResponses = [badResponse1, badResponse2, badResponse3]
        context.append({
            "ID": correctResponseID,
            "correctResponse": correctReponse,
            "monsterDialog": monsterDialog,
            "badResponses": badResponses
        })

    data = getDataJSON()
    data["sessions"][userID] = context
    saveDataJSON(data)
    
    return render_template("game.html", context=context)


@app.route('/api/sessions/<uuid>')
def sessions(uuid):
    pass

@app.route('/fact/<id>')
def specificFact(id):
    factTuple = getData("Fact", "*", "id", id)
    fact = {
        "info": factTuple[0],
        "fullText": factTuple[1],
        "source": factTuple[2]
    }

    return render_template("specificfact.html", factData=fact)

@app.route('/bilan/<uuid>')
def bilan(uuid):
    data = getDataJSON()["sessions"][uuid]
    sessionFacts = []

    for fact in data:
        factID = fact["ID"]
        factHeadline = getData("Fact", "Info", "id", factID)
        factPageLink = f"/fact/{factID}"

        fact = {
            "id": factID,
            "headline": factHeadline,
            "link": factPageLink
        }
        sessionFacts.append(fact)

    return render_template("bilan.html", sessionFacts=sessionFacts)

if __name__ == "__main__":
    app.run(debug=True)