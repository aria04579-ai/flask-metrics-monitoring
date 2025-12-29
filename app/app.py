from flask import Flask
from prometheus_client import (
    Counter,
    Gauge,
    generate_latest,
    start_http_server,
)
import time
from prometheus_client.exposition import basic_auth_handler

app = Flask(__name__)


REQUEST = Counter("http_request_total", "Total HTTP requests")
RESPONSE_TIME = Gauge("http_response_duration_seconds", "HTTP response duration seconds")


@app.route('/')
def index():
    REQUEST.inc()
    start_time = time.time()
    time.sleep(0.5)
    RESPONSE_TIME.set(time.time() - start_time)
    return "Hello from Python app\n", 200


@app.route('/metrics')
def metrics():
    return generate_latest()


if __name__ == "__main__":
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)