from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/webservice',methods=["GET",])
@cross_origin()
def webservice():
    data =[{
        "nome":"shelly",
        "livello":11,
        "grado":25
    },
    {
        "nome":"tick",
        "livello":8,
        "grado":22
    }]
    return jsonify(data)


app.run(host='0.0.0.0', port=81, debug=True) 