from flask import Flask
from flask_cors import CORS
from routes.note_routes import note_bp
from flask import Flask, request
from notifications import send_test_notification


app = Flask(__name__)
CORS(app)

app.register_blueprint(note_bp, url_prefix="/api/notes")

@app.route("/")
def home():
    return {"message": "NeuraNote backend is running 🚀"}
@app.route("/test-notification", methods=["POST"])
def test_notification():
    data = request.json
    token = data.get("token")

    if not token:
        return {"error": "FCM token missing"}, 400

    response = send_test_notification(token)
    return {
        "message": "Notification sent successfully",
        "response": response
    }


if __name__ == "__main__":
    app.run(debug=True)
