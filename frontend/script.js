// Firebase SDKs
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";
import { getMessaging, getToken } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-messaging.js";

// 🔒 USE YOUR OWN VALUES (DO NOT SHARE THEM)
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  messagingSenderId: "YOUR_SENDER_ID",
  appId: "YOUR_APP_ID"
};

// 🔑 Public VAPID key (safe to paste locally, never online)
const VAPID_KEY = "BLd2K5NxLiMp3uorTrvWd2EsJn-aODUKw_WnQkLMJVJSAfGoNyqitRPPUQoTL3JhKz_UxpSHmMeqhNbIAxVr5JE";

const app = initializeApp(firebaseConfig);
const messaging = getMessaging(app);

let FCM_TOKEN = null;

// Ask permission
if ("Notification" in window) {
  Notification.requestPermission().then(permission => {
    console.log("Notification permission:", permission);
  });
}

// Get FCM token
getToken(messaging, { vapidKey: VAPID_KEY })
  .then((currentToken) => {
    if (currentToken) {
      FCM_TOKEN = currentToken;
      console.log("✅ FCM TOKEN:", currentToken);
    } else {
      console.log("❌ No token received");
    }
  })
  .catch((err) => {
    console.error("FCM error:", err);
  });

// Local browser notification test
window.testLocalNotification = function () {
  new Notification("🧠 NeuraNote", {
    body: "Local notification test successful 🎉"
  });
};

// Send notification via Flask backend
window.sendBackendNotification = function () {
  if (!FCM_TOKEN) {
    alert("FCM token not available");
    return;
  }

  fetch("http://127.0.0.1:5000/test-notification", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ token: FCM_TOKEN })
  })
    .then(res => res.json())
    .then(data => console.log("Backend response:", data))
    .catch(err => console.error(err));
};
