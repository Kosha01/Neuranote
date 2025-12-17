from firebase_admin import messaging

def send_test_notification(token):
    message = messaging.Message(
        notification=messaging.Notification(
            title="🧠 NeuraNote",
            body="Test notification from Flask backend 🚀"
        ),
        token=token
    )

    response = messaging.send(message)
    return response
