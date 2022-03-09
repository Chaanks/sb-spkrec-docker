### Docker
To build and run the docker:  
> `docker image build -t sb-docker:latest .`  
> `sudo docker run -p 80:5002 sb-docker -p 5002`


### Speaker recognition
```
import requests
import urllib.parse


IP = "x.x.x.x"
PORT = "80"
URL = f"http://{IP}:{PORT}/api/spkrec"

utt_1 = open("server/static/wavs/Abel_Ezechiel.wav", 'rb')
utt_2 = open("server/static/wavs/Abi_yao_Vidal.wav", 'rb')
data = {"utt_1": utt_1, "utt_2": utt_2}

req = requests.get(URL, files=data)
print(req.json())
```
> Code extracted from `client.py`

