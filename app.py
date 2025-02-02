from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Function to fetch cryptocurrency rates for multiple coins
def get_crypto_rates():
    url = "https://api.coingecko.com/api/v3/simple/price"
    
    # Expanded list of supported cryptocurrencies
    crypto_list = "bitcoin,ethereum,litecoin,dogecoin,cardano,xrp,solana,polkadot,chainlink,cosmos,akash-network"
    
    params = {
        "ids": crypto_list,
        "vs_currencies": "usd"
    }
    
    response = requests.get(url, params=params)
    return response.json()

@app.route("/convert", methods=["GET"])
def convert():
    rates = get_crypto_rates()
    amount = float(request.args.get("amount", 0))
    from_currency = request.args.get("from", "").lower()
    to_currency = request.args.get("to", "").lower()

    # Check if currencies exist in the response data
    if from_currency not in rates or to_currency not in rates:
        return jsonify({"error": "Invalid currency"}), 400

    from_rate = rates[from_currency]["usd"]
    to_rate = rates[to_currency]["usd"]
    converted_amount = (amount * from_rate) / to_rate

    return jsonify({
        "from": from_currency,
        "to": to_currency,
        "original_amount": amount,
        "converted_amount": converted_amount
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
