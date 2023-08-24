#!/bin/bash

FLASK=src/api/app.py
REACT=src/webapp

if [[ ${1,,} = start ]]; then
    echo starting ...
    source env/bin/activate
    npm start --prefix $REACT & flask -A $FLASK run --reload && fg
elif [[ ${1,,} = stop ]]; then
    echo stopping ...
else
    echo use start or stop as the first argument
fi
