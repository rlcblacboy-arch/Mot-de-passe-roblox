from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

MOTS_INTERDITS = ["insulte1", "insulte2", "motinterdit"]

@app.route("/", methods=["GET", "POST"])
def accueil():
    return "Serveur actif"
@app.route("/Mot de passe", methods=["POST"])
def chat():
    data = request.get_json() or {}
    message = data.get("message", "")

    message_min = message.lower()

    bloque = any(mot in message_min for mot in MOTS_INTERDITS)

    if bloque:
        print("Message bloqué :", message)
        return jsonify({"ok": False, "autorise": False})

    print("Message autorisé :", message)
    return jsonify({"ok": True, "autorise": True})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
