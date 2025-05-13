from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    print("User:", user_message)

    # 💬 Simulated responses based on keywords
    if "stock" in user_message.lower():
        reply = "🤖 Stocks represent ownership in a company."
    elif "mutual fund" in user_message.lower():
        reply = "🤖 A mutual fund pools money from investors to buy assets."
    elif "bitcoin" in user_message.lower():
        reply = "🤖 Bitcoin is a decentralized digital currency."
    else:
        reply = f"🤖 You asked: '{user_message}'. I'm a simulated AI for now."

    print("Bot:", reply)
    return jsonify({"reply": reply})


if __name__ == '__main__':
    # 🔧 Required to make it reachable by your phone
    app.run(host='0.0.0.0', port=5000, debug=True)
