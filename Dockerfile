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
<<<<<<< HEAD
CMD ./run.sh server & ./run.sh webapp
=======
EXPOSE 3000

WORKDIR /caial

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

FROM node:20-slim

WORKDIR /caial

COPY src/webapp/package*.json ./src/webapp/

RUN cd src/webapp/
RUN npm install
RUN cd ../../

COPY . .

CMD ["./server.sh", "start"]
>>>>>>> f3ebe9aae66282ba9150ef82ce7e317b22b09ba4
