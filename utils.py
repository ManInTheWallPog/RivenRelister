"""Common methods used by all modules"""

import json
import requests


jwt_token = None
headers = {}
ingame_name = None
WFM_API = "https://api.warframe.market/v1/"


def get_request(url):
    """Executes a wfm query"""
    request = requests.get(WFM_API + url, stream=True)
    if request.status_code == 200:
        return request.json()["payload"]
    return None


def login(user_email: str, user_password: str, platform: str = "pc", language: str = "en"):
    """Login function, copied from the wfm discord."""

    global jwt_token, ingame_name, headers
    headers = {
        "content-type": "application/json; utf-8",
        "accept": "application/json",
        "authorization": "jwt",
        "platform": platform,
        "language": language,
    }
    content = {"email": user_email, "password": user_password, "auth_type": "header"}
    response = requests.post("https://api.warframe.market/v1/auth/signin", data=json.dumps(content), headers=headers)
    if response.status_code != 200:
        print("couldn't login with those credentials")
        return None
    print("logged succesfully")
    ingame_name = response.json()["payload"]["user"]["ingame_name"]
    jwt_token = response.headers["authorization"]
    headers["authorization"] = jwt_token
    headers["auth_type"] = "header"
    return [headers, ingame_name, jwt_token]


def get_current_auctions():
    """Returns the current auctions of the user."""
    if ingame_name:
        result = get_request("/profile/" + ingame_name + "/auctions")
        if result:
            return result["auctions"]
    return None


def wfm_string(item_name, seller_name, price, rank=None):
    """Writes a message that can be copied directly as if the user came from wfm"""
    if rank is not None:
        print(
            "/w "
            + str(seller_name)
            + " hi! i want to buy: "
            + item_name.title().replace("_", " ")
            + " (rank "
            + str(rank)
            + ") for "
            + str(price)
            + " platinum. (warframe.market)\n"
        )
    else:
        print(
            "/w "
            + str(seller_name)
            + " hi! i want to buy: "
            + item_name.title().replace("_", " ")
            + " for "
            + str(price)
            + " platinum. (warframe.market)\n"
        )
