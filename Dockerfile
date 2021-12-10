FROM tensorflow/tensorflow:2.3.0
RUN apt-get update
RUN apt-get install -y git
RUN pip install --upgrade pip
RUN pip install sklearn 'boto3>1.0<2.0' 'sagemaker>2.0<3.0'
RUN pip install flask && pip install flask_restful
ENV PATH $PATH:./
COPY . /root/sagemaker-logistic-regression
WORKDIR /root/sagemaker-logistic-regression