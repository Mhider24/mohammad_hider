from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello from Flask backend!"})

@app.route('/api/test')
def test():
    return jsonify({"status": "success", "data": "Backend is working!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)