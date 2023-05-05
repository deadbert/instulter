from db import nouns, verbs, adjectives
from flask import Flask, request
import random


app = Flask(__name__)


@app.get('/insult')
def insult_user():
    verb = random.choice(verbs)
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f'You are a {verb} {adjective} {noun}'


@app.post('/verb')
def new_verb():
    verb = request.get_json()
    for key in verb:
        if verb[key] not in verbs:
            verbs.append(verb[key])
    return verb, 201


@app.post('/noun')
def new_noun():
    noun = request.get_json()
    for key in noun:
        if noun[key] not in nouns:
            nouns.append(noun[key])
    return noun, 201


@app.post('/adjective')
def new_adjective():
    adjective = request.get_json()
    for key in adjective:
        if adjective[key] not in adjectives:
            adjectives.append(adjective[key])
    return adjective, 201


@app.get('/adjectives')
def get_adjectives():
    return adjectives, 200


@app.get('/verbs')
def get_verbs():
    return verbs, 200


@app.get('/nouns')
def get_nouns():
    return nouns, 200




