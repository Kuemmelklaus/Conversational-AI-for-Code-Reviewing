FROM python:3.8-slim-bullseye

EXPOSE 5000
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