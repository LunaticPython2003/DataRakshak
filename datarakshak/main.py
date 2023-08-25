from flask import Flask, Response
from threading import Thread
from scripts.generator import gen


app = Flask(__name__)

@app.route('/')
def index():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


def run_app(port):
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    t1 = Thread(target=run_app, args=(5000,))
    t1.start()
    t2 = Thread(target=run_app, args=(5001,))
    t2.start()
