# Bootstrap system
FROM python:3.11-bullseye
RUN apt update -y
RUN apt install -y npm
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
ENV NVM_DIR /root/.nvm
RUN . ~/.bashrc && nvm install 18.14.2
ENV PATH $NVM_DIR/versions/node/v18.14.2/bin:$PATH

# Bootstrap application
WORKDIR /app
COPY assets/ ./assets
COPY src/ ./src
COPY requirements.txt run.sh ./
RUN cd ./src/webapp/ && npm i
RUN pip3 install --no-cache-dir -r ./requirements.txt

EXPOSE 3000
EXPOSE 5000

CMD ./run.sh server & ./run.sh webapp
