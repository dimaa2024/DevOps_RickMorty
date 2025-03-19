from flask import Flask, jsonify
import csv

app = Flask(__name__)

@app.route('/robots')
def robots():
    data = []
    with open('../script/robots.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return jsonify(data)

@app.route('/healthcheck')
def healthcheck():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)