from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the API!"}), 200

@app.route('/about')
def about():
    return jsonify({"version": "1.0", "author": "Yagmur Ozden"}), 200

if __name__ == '__main__':
    # here app is listening to any host Ip and port 5000 
    app.run(debug=True, host='0.0.0.0', port=5000)