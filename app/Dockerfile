FROM python:3.9

WORKDIR /app

# Install FFmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Install Python packages
RUN pip install flask==2.0.1 \
    slack_sdk==3.19.5 \
    requests==2.28.2 \
    SpeechRecognition==3.10.0 \
    pydub==0.25.1 \
    gunicorn==20.1.0

# Copy application code
COPY . .

# Expose port
EXPOSE 10000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]
