
if [ -d ".venv" ]; then
    echo "Folder exists"
    source .venv/bin/activate
else
    echo "Folder does not exist"
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
fi

sleep 2
python3 app.py