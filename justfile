run +ARGS:
    python -m venv ./venv
    source ./venv/bin/activate
    python -m pip install -r requirements.txt
    python ./main.py {{ARGS}}
