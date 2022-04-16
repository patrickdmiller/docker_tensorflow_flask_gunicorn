from flask import Flask
from flask_restful import Resource, Api
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
import numpy as np
from joblib import dump, load
import json

data_dir='/data'

m = load_model(os.path.join(data_dir,'model_classify_no_reset_after.h5'))
scaler = load(os.path.join(data_dir,'scaler.bin'))

data = [[116.   ,        0.      ,     0.        ],
        [116.97674419  , 0.      ,     0.        ],
        [113.08026756  , 0.      ,     0.        ],
        [109.08     ,    0.      ,     0.        ],
        [107.04     ,    0.      ,     0.        ],
        [106.02     ,    0.      ,     0.        ],
        [106.98     ,    0.      ,     0.        ],
        [107.98       ,  0.      ,     0.        ],
        [108.97674419 ,  0.      ,     0.        ],
        [108.02006689 ,  0.      ,     0.        ],
        [106.04       ,  0.      ,     0.        ],
        [104.04651163 ,  0.      ,     0.        ],
        [103.02006689 ,  0.      ,     0.        ],
        [101.04651163 ,  0.      ,     0.        ],
        [100.02333333 ,  0.      ,     0.        ],
        [ 99.02006689 ,  0.      ,     0.        ],
        [ 99.         ,  0.      ,     0.        ],
        [ 97.04651163 ,  0.      ,     0.        ],
        [ 96.02333333 ,  0.      ,     0.        ],
        [ 94.04666667 ,  0.      ,     0.        ],
        [ 92.04013378 ,  0.      ,     0.        ],
        [ 91.02325581 ,  0.      ,     0.        ],
        [ 90.02006689 ,  0.      ,     0.        ],
        [ 88.04651163 ,  0.      ,     0.        ]]

data_s = scaler.transform(data)
data_s = np.expand_dims(data_s, axis=0)

app = Flask(__name__)
app.logger.setLevel('INFO')

api = Api(app)

class Test(Resource):

    def get(self):
        r = m.predict(data_s)
        rj = json.dumps(r.tolist())
        return {'r':rj}

 

api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
