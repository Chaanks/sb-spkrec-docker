#!flask/bin/python
import os
import argparse

from flask import Flask, render_template, request, send_file, jsonify
from speechbrain.pretrained import SpeakerRecognition


parser = argparse.ArgumentParser(
    description='Perform speaker recognition server')
parser.add_argument("-p", "--port", type=int, default=5002,
                    help="port to listen on.")
parser.add_argument("--debug", type=bool, default=False,
                    help="true to enable Flask debug mode.")
args = parser.parse_args()

model = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/spkrec-ecapa-voxceleb")
app = Flask(__name__)


@app.route("/api/spkrec", methods=["GET"])
def spkrec():
	request.files['utt_1'].save("utt_1.wav")
	request.files['utt_2'].save("utt_2.wav")

	score, prediction = model.verify_files("utt_1.wav", "utt_2.wav")
	print(f"prediction: {prediction.item()}, score: {score.item()}")

	os.remove("utt_1.wav")
	os.remove("utt_2.wav")

	return jsonify(
		score=score.item(),
		prediction=prediction.item()
	)


def main():
    app.run(debug=args.debug, host="::", port=args.port)


if __name__ == "__main__":
    main()
