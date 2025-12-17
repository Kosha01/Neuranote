from flask import Blueprint, request, jsonify
from datetime import datetime
from models.note_model import create_note

# Blueprint
note_bp = Blueprint("notes", __name__)

# Temporary in-memory storage
NOTES = []


# -------------------------------
# CREATE A NOTE
# -------------------------------
@note_bp.route("/", methods=["POST"])
def add_note():
    data = request.json
    note = create_note(data)
    NOTES.append(note)
    return jsonify(note), 201


# -------------------------------
# GET ALL NOTES
# -------------------------------
@note_bp.route("/", methods=["GET"])
def get_notes():
    return jsonify(NOTES), 200


# -------------------------------
# GET SINGLE NOTE BY ID
# -------------------------------
@note_bp.route("/<note_id>", methods=["GET"])
def get_note(note_id):
    for note in NOTES:
        if note["id"] == note_id:
            return jsonify(note), 200

    return jsonify({"error": "Note not found"}), 404


# -------------------------------
# UPDATE A NOTE
# -------------------------------
@note_bp.route("/<note_id>", methods=["PUT"])
def update_note(note_id):
    data = request.json

    for note in NOTES:
        if note["id"] == note_id:
            note["title"] = data.get("title", note["title"])
            note["content"] = data.get("content", note["content"])
            note["type"] = data.get("type", note["type"])
            note["tags"] = data.get("tags", note["tags"])
            note["event_date"] = data.get("event_date", note["event_date"])
            note["updated_at"] = datetime.utcnow().isoformat()

            return jsonify(note), 200

    return jsonify({"error": "Note not found"}), 404


# -------------------------------
# DELETE A NOTE
# -------------------------------
@note_bp.route("/<note_id>", methods=["DELETE"])
def delete_note(note_id):
    global NOTES
    NOTES = [note for note in NOTES if note["id"] != note_id]
    return jsonify({"message": "Note deleted successfully"}), 200
