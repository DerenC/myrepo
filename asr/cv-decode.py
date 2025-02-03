import sys
import os
import requests
import pandas as pd

def clear_console():
	sys.stdout.write("\033[H\033[J")
	sys.stdout.flush()

def print_progress_bar(info, iteration, total, length=50):
	percent = (iteration / total) * 100
	bar_length = int(length * iteration // total)
	bar = "#" * bar_length + "-" * (length - bar_length)
	print(f"[{bar}] {percent:.2f}% ({iteration}/{total})")
	print(f"{info}")

url = "http://localhost:8001/asr"

cwd = os.getcwd()
common_voice_dir_path = os.path.abspath(os.path.join(cwd, "../../../common_voice"))
cv_valid_dev_dir_path = os.path.join(common_voice_dir_path, "cv-valid-dev\cv-valid-dev")

starting_ind = 3400

all_files = os.listdir(cv_valid_dev_dir_path)
all_mp3_files = list(filter(lambda filename: filename.endswith(".mp3"), all_files))
files_to_process = all_mp3_files[starting_ind:]
totalIter = len(all_mp3_files)

csv_filename = "cv-valid-dev.csv"
csv_file_path = os.path.join(common_voice_dir_path, csv_filename)
if not os.path.exists(csv_file_path):
	print(f"{csv_filename} does not exist")
	sys.exit(1)

df = pd.read_csv(csv_file_path)
nRow = df.shape[0]

transcriptions = df.get("generated_text")
if transcriptions is None:
	transcriptions = [""] * nRow

nIter = starting_ind
lastBatchNum = 0
batchSize = 10

for file in files_to_process:
	file_path = os.path.join(cv_valid_dev_dir_path, file)

	with open(file_path, "rb") as f:
		files = {"file": f}
		response = requests.post(url, files=files)

	transcribed_text = response.json()["transcription"]
	transcriptions[nIter] = transcribed_text

	nIter += 1
	clear_console()
	print_progress_bar(transcribed_text, nIter, totalIter)

	if nIter // 10 != lastBatchNum:
		lastBatchNum = nIter // 10
		df["generated_text"] = transcriptions
		df.to_csv(csv_file_path, index=False)

df["generated_text"] = transcriptions
df.to_csv(csv_file_path, index=False)
