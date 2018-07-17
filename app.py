from flask import Flask
from flask import jsonify

from rpi import temperature

app = Flask(__name__)
app.config['SECRET_KEY'] = 'blablabla'


@app.route("/")
def hello():
    return jsonify({"celsius": temperature.temp()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
