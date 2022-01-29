from flask import Flask, render_template, request, jsonify
from utils import get_delivery_fee

app = Flask(__name__)


@app.route("/")
def index():
    data = get_delivery_fee()
    return render_template('index.html', data=data)


@app.route('/loc', methods=['GET'])
def parse_coordinates():

    lat = request.args.get('lat')
    lng = request.args.get('lng')

    fee = get_delivery_fee(str(lat) + ',' + str(lng))
    print(fee)
    return fee


@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({'status': 'ok'})


if __name__ == '__main__':
    app.run()
