import flask
import requests
from flask import request, render_template
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/api/v1/shakespearify/pokemon/", methods=["GET"])
def shakespearify():
    query = request.args["name"]

    pokemon_info = check_pokemon_valid(query)
    if pokemon_info == False:
        return {"Error": "Pokemon not found"}
    else:
        return pokemon_info


def check_pokemon_valid(poke_query):
    url = "https://pokeapi.co/api/v2/pokemon-species/" + poke_query
    response = requests.get(url)
    if response.text == "Not Found":
        print(response.text)
        return False
    else:
        json_object = response.text
        python_obj = json.loads(json_object)
        items = python_obj.get("flavor_text_entries")
        raw_desc = items[8]["flavor_text"].replace("\r", "").replace("\n", "")
        desc = translate(raw_desc)
        pokemon_info = {
            "Pokemon name": poke_query.capitalize(),
            "description": desc,
        }
        return pokemon_info


def translate(desc_string):
    url = (
        "https://api.funtranslations.com/translate/shakespeare.json?text="
        + desc_string.replace(" ", "%20")
    )
    response = requests.get(url)
    json_object = response.text
    python_obj = json.loads(json_object)
    desc = python_obj["contents"]["translated"]
    return desc


def main():
    app.run(host="0.0.0.0")


if __name__ == "__main__":
    main()
