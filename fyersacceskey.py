from datetime import date
from fyers_apiv3 import fyersModel
import os
from dotenv import load_dotenv
import datetime as dt
import json
load_dotenv()


client_id = os.getenv('client_id')
secret_key = os.getenv('secret_key')
redirect_uri = os.getenv('redirect_uri')

today = str(date.today())  

def get_access_token():
    access = ""
    
    if not os.path.exists("./authcode"):
        print("Creating authcode directory")
        os.makedirs("./authcode")

    auth_file = f"./authcode/{today}.json"  

    if not os.path.exists(auth_file):
        session = fyersModel.SessionModel(client_id=client_id, secret_key=secret_key,
                                          redirect_uri=redirect_uri, response_type="code", grant_type="authorization_code")
        response = session.generate_authcode()
        print("Login Url : ", response)
        auth_code = input("Enter Auth Code : ")
        session.set_token(auth_code)
        access_token = session.generate_token()["access_token"]

        auth_data = {
            "access_token": access_token
        }

        with open(auth_file, "w") as f:
            json.dump(auth_data, f)

    else:
        with open(auth_file, "r") as f:
            auth_data = json.load(f)
            access = auth_data.get("access_token", "")

    return access


access_token = get_access_token()

fyers = fyersModel.FyersModel(
    client_id=client_id, token=access_token, log_path=os.getcwd())

# print(fyers.get_profile())
print(fyers.funds())
print(fyers.holdings())

# data = {"symbol": "NSE:NIFTYBANK-INDEX", "resolution": "1", "date_format": "1",
#         "range_from": "2023-01-17", "range_to": "2023-01-17", "cont_flag": "1"}

# print(fyers.history(data))


# newToken = f"{client_id}:{access_token}"
# symbol = ['NSE:NIFTYBANK-INDEX','NSE:NIFTY50-INDEX']
# cws = ws.FyersSocket(access_token=newToken,
#                      run_background=False, log_path=os.getcwd())


# def on_ticks(msg):
#     script = msg[0]['symbol']
#     ltp = msg[0]['ltp']
#     high = msg[0]['high_price']
#     low = msg[0]['low_price']
#     close =msg[0]['close']
#     ltt = dt.datetime.fromtimestamp(msg[0]['timestamp'])
#     print(
#         f"Script:{script}  ,  ltp:{ltp}  ,  HIGH:{high} ,  LOW:{low},  ltt:{ltt}, close:{close}")


# cws.websocket_data = on_ticks
# cws.subscribe(symbol=symbol, data_type="symbolData")
# cws.unsubscribe(symbol=symbol)
# cws.keep_running()
# cws.close() 

