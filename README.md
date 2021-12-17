# sagemaker-logistic-regression
sagemaker studio上でlogistic回帰を動かす

## 環境に入る
```
bash start.sh
```

でdocker containerの中に入る

## 開発環境で学習
docker container上で

```
bash train
```

実行後、/opt/ml/model/model.pth
に学習済モデルができる

## 開発環境で推論
docker container上で

```
bash serve
```

実行後、8080portに推論サーバがたつ。

## request
```bash
curl --location --request GET 'http://127.0.0.1:8080/ping'
```

でhealth checkができる。

```bash
curl -XPOST http://127.0.0.1:8080/invocations -H 'Content-Type: application/json' -d '{"petal_length": 0.4,"petal_width": 1.6}'
```

で推論できる。


## ecrにimage push
```bash
bash deploy.sh
```
