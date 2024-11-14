# lead-timeout-responce
### Installation Guide
1) **Copy repository to your machine:**
```bash
git clone https://github.com/InWamos/lead-timeout-responce
```

2) **Create virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

3) **Install dependencies**
```bash
pip3 install -r requirements.txt
```
4) **Add your .session files to the data/sessions directory**

5) **Launch bot**
```bash
python3 ./src/__main__.py
```

### Utils Guide
**Add User's session**
1) Edit variables in **_/src/utils/add_user.py_** and pass your 
API_ID and API_HASH
2) Run the script from project's root dir:
`python3 /src/utils/add_user.py`
3) Follow the instructions on terminal

**Find broken sessions**
_In case you face Error[401] you might have broken sessions is your session folder. To find them do the following:_
1) Run the script from project's root directory:
`python3 /src/utils/find_broken_sessions.py`

__Script will print you the names of sessions you have to remove__