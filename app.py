from flask import Flask, render_template, request, jsonify
import requests
import json

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
    app.run(threaded=True, port=5000)

API_URL = 'https://apim-kotipizza-ecom-prod.azure-api.net/webshop/v1/restaurants/nearby?type=DELIVERY'
COORDS = '&coordinates='
DEFAULT = '62.6153386,29.7500527'


def read_data_json(coords):
    print(API_URL + COORDS + coords)
    req = requests.get(API_URL + COORDS + coords)
    return json.loads(req.content)


def get_delivery_fee(coords=DEFAULT) -> str:
    data = read_data_json(coords)

    if data and len(data) > 0:
        # TODO useamman ravintolan händläys mikäli niitä löytyy, tällä hetkellä otetaan ensimmäinen
        data = data[0]
        if data['openForDeliveryStatus'] == "CLOSED":
            return "Suljettu!"
        if "dynamicDeliveryFee" in data:
            return str(data["dynamicDeliveryFee"]) + " €"
        return "Tietoa ei saatavilla."
    return "Tietoa ei saatavilla."
