from flask import Flask, jsonify
import time
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

metrics = []

@app.route("/health")
def health():
    return "OK", 200

@app.route("/metrics")
def metrics_route():
    return jsonify(metrics)

@app.route("/collect")
def collect():
    start = time.time()

    time.sleep(0.1)  # simula processamento real

    response_time = round((time.time() - start) * 1000, 2)

    data = {
        "service": "api",
        "status": "healthy",
        "response_time": response_time,
        "timestamp": time.time()
    }

    metrics.append(data)

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)