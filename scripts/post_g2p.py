import sys
import requests
import json

URL = "http://localhost:5566/api/v1/g2p"

def post_g2p(url=URL, graphemes="你好阿朋友"):
    x = requests.post(url, data={"graphemes": graphemes})

    phonemes = json.loads(x.text)
    print(phonemes[0])
    return


if __name__  == "__main__":
    text = sys.argv[1]
    post_g2p(graphemes=text)

