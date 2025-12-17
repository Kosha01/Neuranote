from flask import Flask
from flask_cors import CORS
from routes.note_routes import note_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(note_bp, url_prefix="/api/notes")

@app.route("/")
def home():
    return {"message": "NeuraNote backend is running 🚀"}

if __name__ == "__main__":
    app.run(debug=True)
