from flask import Flask, render_template
from utils import get_delivery_fee

app = Flask(__name__)


@app.route("/")
def index():
    data = get_delivery_fee()
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
