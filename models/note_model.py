from datetime import datetime
import uuid

def create_note(data):
    return {
        "id": str(uuid.uuid4()),
        "title": data.get("title", ""),
        "content": data.get("content", ""),
        "type": data.get("type", "normal"),
        "tags": data.get("tags", []),
        "event_date": data.get("event_date"),
        "created_at": datetime.utcnow().isoformat(),
        "updated_at": datetime.utcnow().isoformat()
    }
