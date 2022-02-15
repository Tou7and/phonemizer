from flask import Flask
from flask import request, jsonify
# from flask import render_template
from phonemizer import phonemize
from phonemizer.backend import EspeakBackend

backend = EspeakBackend('cmn')

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
    phonemized = backend.phonemize([graphemes])
    phones = phonemized[0]
    results = [phones]

    return jsonify(results)


if __name__ == "__main__":  
    app.run(debug=True)
