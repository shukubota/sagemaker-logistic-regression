# sagemaker-logistic-regression
sagemaker studio上でlogistic回帰を動かす

## 環境に入る
```
bash start.sh
```

でdocker containerの中に入る

## request
```bash
curl --location --request GET 'http://127.0.0.1:5000?petal_length=0.4&petal_width=1.6'
```

```bash
curl --location --request GET 'http://127.0.0.1:5000?petal_length=4.6&petal_width=1.3'
```