_yashu () {
    echo "U3BsYm90cy9UZWxldGhvbkFmaw==" | base64 -d

_alpha () {
    pip install -r requirements.txt
    python3 env_vars.py
    git clone https://github.com/$(_yashu) AFK
    cd AFK
    python3 yashu.py

_alpha
