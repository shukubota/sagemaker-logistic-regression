#!/usr/bin/env python
from flask import Flask, request, jsonify, make_response
import pickle
from model import LogisticRegressionGD

app = Flask(__name__)

# 学習済modelの読み込み
with open('/opt/ml/model/model.pth', mode='rb') as f:
  model = pickle.load(f)

@app.route("/ping", methods=['GET'])
def ping():
  return { "status": 200 }

@app.route("/invocations", methods=['POST'])
def post():
  # 前処理
  params = jsonify(request.json)
  input = model.input_fn(request.json)
  
  # 推論
  _output = model.predict(input)

  # 後処理
  output = model.output_fn(_output)
  
  return { "category": output }

if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0', debug=True, port=8080)
