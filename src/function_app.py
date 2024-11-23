import logging
import json
import azure.functions as func
import oandapyV20
import oandapyV20.endpoints.orders as orders

# OANDA API設定
OANDA_API_URL = "https://api-fxpractice.oanda.com/v3"
OANDA_API_TOKEN = ${{ secrets.OANDA_API_TOKEN }} # OANDA APIトークン
OANDA_ACCOUNT_ID = ${{ secrets.OANDA_ACCOUNT_ID }} # OANDAアカウントID

client = oandapyV20.API(access_token=OANDA_API_TOKEN)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Webhook received.")

    try:
        # Webhookデータを取得
        req_body = req.get_json()
        action = req_body.get("action")  # "buy" または "sell"
        instrument = req_body.get("instrument")  # 通貨ペア (例: "EUR_USD")
        units = req_body.get("units")  # 注文量

        if not action or not instrument or not units:
            return func.HttpResponse(
                "Invalid input. 'action', 'instrument', and 'units' are required.",
                status_code=400
            )

        # OANDAで注文を作成
        order_data = {
            "order": {
                "instrument": instrument,
                "units": units if action == "buy" else f"-{units}",
                "type": "MARKET",
                "positionFill": "DEFAULT"
            }
        }

        r = orders.OrderCreate(OANDA_ACCOUNT_ID, data=order_data)
        client.request(r)

        logging.info(f"Order created: {r.response}")
        return func.HttpResponse(
            json.dumps({"status": "success", "details": r.response}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(
            json.dumps({"status": "error", "message": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
