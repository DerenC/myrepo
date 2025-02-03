
from flask import Flask, request, jsonify
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import librosa
import io


## Task 2(b)

app = Flask(__name__)

@app.route("/ping", methods=['GET'])
def ping():
	return "pong"


## Task 2(c)

supported_file_formats = ["wav", "mp3", "aiff", "flac", "ogg"]
# Unsupported_formats = ["m4a", "mp4", "aac", "wma]	# Discovered after testing

audio_sample_rate = 16000

model_name = "facebook/wav2vec2-large-960h"
processor = Wav2Vec2Processor.from_pretrained(model_name)
model = Wav2Vec2ForCTC.from_pretrained(model_name)

@app.route('/asr', methods=['POST'])
def transcribe_audio():
	if 'file' not in request.files:
		return jsonify({"error": "No file provided"}), 400

	audio_file = request.files['file']

	if audio_file.filename.split(".")[-1] not in supported_file_formats:
		supported_formats_as_str = rreplace(', '.join(supported_file_formats), ', ', ' & ')
		error_message = f"Invalid file format. Only support {supported_formats_as_str} for now."
		return jsonify({"error": error_message}), 400

	audio_bytes = audio_file.read()

	audio_input, sample_rate = librosa.load(io.BytesIO(audio_bytes), sr=audio_sample_rate)

	input_values = processor(audio_input, sampling_rate=sample_rate, return_tensors="pt").input_values

	with torch.no_grad():
		logits = model(input_values).logits

	predicted_ids = torch.argmax(logits, dim=-1)
	transcription = processor.decode(predicted_ids[0])

	duration = librosa.get_duration(y=audio_input, sr=sample_rate)

	return jsonify({
		"transcription": transcription,
		"duration": duration,
	})

# Replace the last occurrence of an expression in a string
def rreplace(string, old, new):
    return (string[::-1].replace(old[::-1],new[::-1], 1))[::-1]
