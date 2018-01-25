from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)
# Index endpoint
@app.route('/')
def hello_world():
    return "Blockshell"

@app.route('/allblocks')
def blocks():
    f = open("chain.txt", "r")
    data = json.loads(f.read())
    f.close()
    return render_template('blocks.html', data=data)

@app.route('/block/<hash>')
def block(hash):
    f = open("chain.txt", "r")
    data = json.loads(f.read())
    f.close()
    for eachBlock in data:
        if eachBlock['hash'] == hash:
            return render_template('blockdata.html', data=eachBlock)


if __name__ == '__main__':
    app.run(debug=True)
