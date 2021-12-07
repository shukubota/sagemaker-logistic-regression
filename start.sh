#!/bin/bash
# docker build -t logistic-regression .
# docker run -it logistic-regression /bin/bash
docker-compose build
docker-compose up -d
docker-compose exec app /bin/bash
