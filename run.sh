#!/usr/bin/env bash

usage() {
    echo "Usage:
    $0 webapp - starts webapp at port 3000
    $0 server - starts linter server at port 5000"
}

# Starts the server. Assumes all dependencies to be installed:
#   pip install -r requirements.txt
start_server() {
    flask -A src/api/app.py run --reload
}

# Starts the webapp. Assumes all dependencies to be installed:
#   cd src/webapp && npm i
start_webapp() {
    npm start --prefix src/webapp
}

case "$1" in
-h|--help)
    usage
    ;;
server)
    start_server
    ;;
webapp)
    start_webapp
    ;;
*)
    usage >&2
    exit 1
esac