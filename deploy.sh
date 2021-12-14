REGION=us-east-1
REPOSITORY_NAME=sagemaker-ecr-images
ACCOUNT_ID=111111111111

aws ecr get-login-password | docker login --username AWS --password-stdin https://${ACCOUNT_ID}.dkr.ecr.us-east-1.amazonaws.com/sagemaker-ecr-images
docker build . -t demo -t ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REPOSITORY_NAME}:demo --no-cache
docker push ${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REPOSITORY_NAME}:demo