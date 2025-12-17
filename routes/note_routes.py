from flask import Blueprint, request, jsonify
from datetime import datetime
from models.note_model import create_note
from firebase_config import db

note_bp = Blueprint("notes", __name__)

notes_ref = db.collection("notes")


# CREATE NOTE
@note_bp.route("/", methods=["POST"])
def add_note():
    data = request.json
    note = create_note(data)

    notes_ref.document(note["id"]).set(note)
    return jsonify(note), 201


# GET ALL NOTES
@note_bp.route("/", methods=["GET"])
def get_notes():
    notes = []
    docs = notes_ref.stream()

    for doc in docs:
        notes.append(doc.to_dict())

    return jsonify(notes), 200


# GET SINGLE NOTE
@note_bp.route("/<note_id>", methods=["GET"])
def get_note(note_id):
    doc = notes_ref.document(note_id).get()

    if not doc.exists:
        return jsonify({"error": "Note not found"}), 404

    return jsonify(doc.to_dict()), 200


# UPDATE NOTE
@note_bp.route("/<note_id>", methods=["PUT"])
def update_note(note_id):
    data = request.json
    doc_ref = notes_ref.document(note_id)
    doc = doc_ref.get()

    if not doc.exists:
        return jsonify({"error": "Note not found"}), 404

    updated_data = doc.to_dict()
    updated_data.update({
        "title": data.get("title", updated_data["title"]),
        "content": data.get("content", updated_data["content"]),
        "type": data.get("type", updated_data["type"]),
        "tags": data.get("tags", updated_data["tags"]),
        "event_date": data.get("event_date", updated_data["event_date"]),
        "updated_at": datetime.utcnow().isoformat()
    })

    doc_ref.set(updated_data)
    return jsonify(updated_data), 200


# DELETE NOTE
@note_bp.route("/<note_id>", methods=["DELETE"])
def delete_note(note_id):
    notes_ref.document(note_id).delete()
    return jsonify({"message": "Note deleted successfully"}), 200
