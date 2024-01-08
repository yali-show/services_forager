from http_client import HttpBinClient, logging
from datetime import datetime
from flask import Flask, jsonify, Response

CLIENT_HTTPBIN = HttpBinClient()
history = dict()

app = Flask(__name__)


@app.route('/get_ip', methods=['GET'])
def get_ip_httpbin() -> Response | tuple[Response, int]:
    """
    Getting data from and saving in history variable
    :return:
    """

    try:
        logging.info("Saving data from server (ip)")

        ip = CLIENT_HTTPBIN.get_ip()
        date = datetime.now().strftime("%m %d, %Y %H:%M:%S")
        history[date] = ip
        return jsonify(ip)

    except Exception as ex:
        logging.error("Error in get_ip_httpbin")
        return jsonify({"error": str(ex)}), 500


app.run(debug=True)
