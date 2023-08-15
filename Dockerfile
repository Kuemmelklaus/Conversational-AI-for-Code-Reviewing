FROM python:3.8-slim-bullseye

EXPOSE 5000

WORKDIR /python-docker

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-u", "-m", "flask", "run", "--host", "0.0.0.0", "-p", "5000"]