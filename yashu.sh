_yashu () {
    echo "U3BsYm90cy9UZWxldGhvbkFmaw==" | base64 -d
}

_alpha () {
    sudo apt install git
    git clone https://github.com/$(_yashu) AFK
    rm AFK/config.py
    cp config.py AFK/config.py
    cd AFK 
    python3 yashu.py
}

_alpha
