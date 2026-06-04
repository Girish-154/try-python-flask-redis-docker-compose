import os
from flask import Flask
from redis import Redis

app = Flask(__name__)

redis_client = Redis(
    host=os.environ.get("REDIS_HOST"),
    port=6379,
    decode_responses=True
)

@app.route('/')
def hello():
    count = redis_client.incr('hits')
    return f'Hello World! I have been seen {count} times.'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
