from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.hmskj9c.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/api/login', methods="POST")
def D3_workout_post():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    doc = {
        'id': id_receive,
        'pw': pw_receive
    }
    db.login.insert_one(doc)

    return jsonify({'msg':'로그인 완료!'})