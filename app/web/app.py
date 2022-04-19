from flask import Flask
from flask_restful import Resource, Api
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import numpy as np
from joblib import dump, load
import json

app = Flask(__name__)

app.logger.setLevel('INFO')

api = Api(app)

class Test(Resource):

    def get(self):
        #r = m.predict(data_s)
        #rj = json.dumps(r.tolist())
        return {'test':'success'}

 

api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
