import requests
import logging


class HttpBinClient:
    def __init__(self, base_url="https://httpbin.org"):
        self.base_url = base_url
        logging.info("HttpBin innit")

    def get_ip(self) -> dict:
        """
        Get information about the IP address from which the request originated
        :return: dict - ip of server
        """
        try:
            logging.info("Waiting for response (ip) from server")

            url = f"{self.base_url}/ip"
            response = requests.get(url)
            return response.json()

        except Exception as ex:
            logging.error("Get ip error in HttpBinClient")
            logging.error(str(ex))

    def post_basic_authentication(self, data: dict, auth: tuple) -> dict:
        """
        Post request basic authentication example
        :param data: {key: value}
        :param auth: (username, password)
        :return: response from post request of authentication
        """
        try:
            logging.info("Posting authentication data")

            url = f"{self.base_url}/post"
            data = {'data': data}
            auth = (auth, )
            response = requests.post(url, data=data, auth=auth)
            return response.json()

        except Exception as ex:
            logging.error("Error in post_basic_authentication method in"
                          " HttpBinClient")
            logging.error(str(ex))

    def delete_request(self, params: dict) -> dict:
        """
        Delete request for httpbin
        :return: response from delete request
        """
        try:
            logging.info("Delete request sending")

            url = f"{self.base_url}/delete"
            response = requests.delete(url, params=params)

            return response.json()
        except Exception as ex:
            logging.error("Error in delete_request in HttpBinClient")
            logging.error(str(ex))
