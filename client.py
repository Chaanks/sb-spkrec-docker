import requests
import urllib.parse


IP = ""
PORT = "80"
URL = f"http://{IP}:{PORT}/api/spkrec"

# Speaker is not the same
utt_1 = open("server/wavs/Abel_Ezechiel.wav", 'rb')
utt_2 = open("server/wavs/Abi_yao_Vidal.wav", 'rb')
data = {"utt_1": utt_1, "utt_2": utt_2}

req = requests.get(URL, files=data)
print(req.json())

# Speaker is the same
utt_1 = open("server/wavs/Abel_Ezechiel.wav", 'rb')
utt_2 = open("server/wavs/Abel_Ezechiel.wav", 'rb')
data = {"utt_1": utt_1, "utt_2": utt_2}

req = requests.get(URL, files=data)
print(req.json())