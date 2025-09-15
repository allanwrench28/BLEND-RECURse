from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/ghst_pool', methods=['GET'])
def get_ghst_pool():
    ghst_pool = [
        {"name": "GHST Alpha", "expertise": "AI Ethics", "weight": 1},
        {"name": "GHST Beta", "expertise": "Data Science", "weight": 2},
        {"name": "GHST Gamma", "expertise": "UI/UX Design", "weight": 3},
        {"name": "GHST Delta", "expertise": "DevOps", "weight": 1},
        {"name": "GHST Epsilon", "expertise": "Cybersecurity", "weight": 2}
    ]
    return jsonify(ghst_pool)


if __name__ == '__main__':
    app.run(port=5000)
