FROM tensorflow/tensorflow:2.3.0
RUN apt-get update
RUN apt-get install -y git
RUN pip install --upgrade pip
RUN pip install sklearn 'boto3>1.0<2.0' 'sagemaker>2.0<3.0'
RUN pip install flask && pip install flask_restful
RUN apt-get install -y nginx
RUN apt-get install -y lsof
RUN pip install gunicorn
ENV PATH="/opt/program:${PATH}"
COPY . /opt/program
WORKDIR /opt/program