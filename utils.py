import requests
import json

API_URL = 'https://apim-kotipizza-ecom-prod.azure-api.net/webshop/v1/restaurants/nearby?type=DELIVERY&coordinates=62.6153386,29.7500527'


def read_data_json():
    req = requests.get(API_URL)
    return json.loads(req.content)


def get_delivery_fee():
    data = read_data_json()

    if data:
        data = data[0]
        if data['openForDeliveryStatus'] == "CLOSED":
            return "suljettu :C"
        return data["currentDeliveryEstimate"]
