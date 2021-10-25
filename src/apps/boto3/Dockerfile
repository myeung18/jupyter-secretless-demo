FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y \
    && apt-get clean 
    # && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    # && unzip awscliv2.zip \
    # && ./aws/install \
    # && rm -rf awscliv2.zip

RUN pip install boto3
RUN pip install -r requirements.txt

COPY *.py ./

EXPOSE 3800

CMD python hello.py