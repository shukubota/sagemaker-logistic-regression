from flask import Flask
from flask_restful import Api, Resource, abort, reqparse
import pickle
from main import LogisticRegressionGD

class Server(Resource):
  def get(self):
    # リクエストパラメータをparse
    parser = reqparse.RequestParser()
    parser.add_argument("petal_length", type=float, required=True, help="petal_length required!")
    parser.add_argument("petal_width", type=float, required=True, help="petal_width required!")
    args = parser.parse_args()

    # 前処理
    input = model.input_fn(args)

    # 推論
    _output = model.predict(input)

    # 後処理
    output = model.output_fn(_output)
    
    return { "catetory": output }

app = Flask(__name__)
api = Api(app)
api.add_resource(Server, "/")

if __name__ == "__main__":
  # 学習済modelの読み込み
  with open('estimator.pickle', mode='rb') as f:
    model = pickle.load(f)

  app.run(host='0.0.0.0', debug=True, port=5000)
