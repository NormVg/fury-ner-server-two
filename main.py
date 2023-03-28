from flask import Flask ,request,jsonify
from IRS import reco_intent
from cus_ner import NER

app = Flask(__name__)
 

@app.route('/')
def index():
    return '<-- thefury intent reco system -->'

@app.route('/irs',methods=['GET', 'POST'])
def irs():
    ner = ""
    command = ["movie-command","music-command"]
    inp = request.args.get("input")
    out = reco_intent(inp)
    
    if out in command:
        ner = NER(inp)
        # print(out)
    dictn = {"exe":out,"ner":ner}
    return jsonify(dictn)

if __name__ == '__main__':
    app.run(debug=True)