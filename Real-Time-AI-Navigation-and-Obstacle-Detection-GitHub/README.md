# Real-Time AI Navigation and Obstacle Detection for Blind Users

A web-based assistive navigation project combining movement monitoring, YOLO-based obstacle detection, GPS/location handling, route guidance, voice feedback and an SOS/trusted-contact workflow.

> **Source note:** This repository is built from the source files supplied for the project. The original project also contained compiled EXE/build files and large YOLO model files; those are intentionally excluded from the GitHub source repository.

## Main modules

- **Movement monitoring:** the supplied `obstacle.py` implementation classifies movement from accelerometer samples using magnitude statistics and peak counting, with a state machine for stable state changes.
- **Obstacle detection:** YOLOv8 inference on camera frames, distance estimation from bounding-box height, obstacle-zone classification and spoken warnings.
- **Navigation:** destination geocoding through OpenStreetMap Nominatim and walking-route retrieval through OSRM, with a fallback straight-line estimate when the route service is unavailable.
- **Voice feedback:** `pyttsx3` is used by the Python backend for spoken alerts.
- **SOS/trusted contacts:** contacts are loaded from a local `contacts.json`; the backend records the SOS request and returns contact information. The browser-side application can initiate a phone call using `tel:`.
- **PWA support:** `manifest.json` and `sw.js` are included for the web application shell.

## Important implementation note

The project report describes an SVM-based movement detection module, while the supplied `obstacle.py` source currently contains a magnitude/peak-based classifier rather than an SVM model. This repository preserves the supplied source implementation rather than changing it to match the report.

## Repository structure

```text
Real-Time-AI-Navigation-and-Obstacle-Detection/
├── README.md
├── requirements.txt
├── .gitignore
├── obstacle.py
├── movements.html
├── home.html
├── manifest.json
├── sw.js
├── gps_test_app.py
├── obstacle.spec
├── models/
│   └── README.md
├── docs/
│   ├── Project_source_code.pdf
│   ├── Project_Document.pdf
│   └── Journal_paper.pdf
└── screenshots/
    └── project-poster.jpeg
```

## Setup

Use Python 3.x. Create and activate a virtual environment, then install dependencies:

```bash
python -m venv venv
```

Windows:

```cmd
venv\Scripts\activate
pip install -r requirements.txt
```

Linux/macOS:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

Place the required `yolov8n.pt` model in the project root before starting obstacle detection. See `models/README.md`.

## Run

```bash
python obstacle.py
```

The supplied backend starts Flask on port `5000`. Open:

```text
http://127.0.0.1:5000/
```

For phone sensor/camera access, browser security requirements may require HTTPS and appropriate permissions. The original source also contains network/HTTPS handling for local testing.

## Google Maps API key

The supplied `movements.html` contained a Google Maps API key. The key has been **redacted from this GitHub copy** so it is not published as a credential.

Before using the Google Maps portion of the page, configure your own restricted Google Maps JavaScript API key according to your project/account setup.

## Files intentionally excluded

Do not commit:

- `.exe` files
- `build/` and `dist/`
- `yolov8n.pt` / `yolov8s.pt` unless redistribution is permitted
- `cert.pem` / `key.pem`
- `contacts.json`
- Python virtual environments

## External services

The supplied navigation code uses online services for destination lookup and route calculation. Therefore, navigation is not completely offline.

## Documentation

The `docs/` directory contains the supplied project documentation and source-code reference. The `screenshots/` directory contains the project poster.

## License

No project-specific open-source license was supplied with the source files. Add an appropriate license before public distribution if desired.
