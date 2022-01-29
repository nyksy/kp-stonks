from tkinter import EXCEPTION
import requests
import json

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
