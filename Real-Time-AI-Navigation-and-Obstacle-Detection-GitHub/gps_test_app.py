current_location = {
    "lat": None,
    "lon": None
}

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# ---------------- HOME PAGE ----------------
@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>GPS Test Page</title>
</head>
<body>
<h3>GPS Test Page</h3>
<button onclick="sendGPS()">Send GPS</button>

<script>
function sendGPS(){
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(
            function(pos){
                fetch(" ${window.location.origin}/location", {
                    method: "POST",
                    headers: {"Content-Type":"application/json"},
                    body: JSON.stringify({
                        lat: pos.coords.latitude,
                        lon: pos.coords.longitude
                    })
                })
                .then(res => res.json())
                .then(data => alert(
                    "GPS Sent!\\nLat: "+data.lat+"\\nLon: "+data.lon
                ));
            },
            function(err){
                alert("GPS Error: " + err.message);
            }
        );
    } else {
        alert("Geolocation not supported");
    }
}
</script>
</body>
</html>
"""

# ---------------- RECEIVE GPS ----------------
@app.route("/location", methods=["POST"])
def receive_location():
    data = request.get_json()

    current_location["lat"] = data["lat"]
    current_location["lon"] = data["lon"]

    print("📍 GPS Stored:", current_location)

    return jsonify({
        "status": "ok",
        "lat": current_location["lat"],
        "lon": current_location["lon"]
    })


# ---------------- SAVE TRUSTED CONTACT ----------------
@app.route("/save_contact", methods=["POST"])
def save_contact():
    data = request.json   # { name, phone }

    # create file if not exists
    if not os.path.exists("contacts.json"):
        with open("contacts.json", "w") as f:
            json.dump({}, f)

    with open("contacts.json", "r+") as f:
        contacts = json.load(f)
        contacts[data["name"].lower()] = data["phone"]
        f.seek(0)
        json.dump(contacts, f, indent=4)
        f.truncate()

    print("✅ Trusted contact saved:", data)
    return jsonify({"status": "saved"})

# ---------------- RUN APP (ALWAYS LAST) ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

