import subprocess
import sys

# Install required packages
packages = [
    "flask==2.0.1",
    "slack_sdk==3.19.5",
    "requests==2.28.2",
    "SpeechRecognition==3.10.0",
    "pydub==0.25.1",
    "gunicorn==20.1.0"
]

for package in packages:
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("All packages installed successfully!")
