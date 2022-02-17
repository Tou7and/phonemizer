from flask import Flask
from flask import request, jsonify
# from flask import render_template
from phonemizer import phonemize
from phonemizer.backend import EspeakBackend
from phonemizer.separator import Separator

# zh_backend = EspeakBackend('cmn')
pro_separator = Separator(phone='-', word=' ')

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "<h1> G2P service (/api/v1/g2p) </h1>"

@app.route("/api/v1/g2p", methods=['POST'])
def api_g2p():
    if request.method == 'POST':
        graphemes = request.form.get('graphemes')
    else:
        return "Error: No graphemes field provided."
    
    results = []
    # phonemized = backend.phonemize([graphemes])
    
    try:
        phonemized = phonemize([graphemes], backend='espeak', language='cmn', separator=pro_separator)
        phones = phonemized[0]
    except Exception as error:
        phones = "[error={}]".format(error)

    results = [phones]

    return jsonify(results)


if __name__ == "__main__":  
    app.run(debug=True)
