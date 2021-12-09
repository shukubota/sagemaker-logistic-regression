from flask import Flask
from flask_restful import Api, Resource, abort, reqparse

class Server(Resource):
  def get(self):
    return {"name": "Hello {}!".format(args["name"]), "age": args["age"]}

  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument(
      "q_param", type=int, location="args", help="q_param is numbers"
    )
    parser.add_argument("f_param", location="form")
    args = parser.parse_args()
    return {
      "post": "Hello World!",
      "qParam": args["q_param"],
      "fParam": args["f_param"],
    }

app = Flask(__name__)
api = Api(app)


api.add_resource(Server, "/")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=5000)