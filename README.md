**Parsing service Quickstart**

`mkdir test_app`

`cd test_app`

`virtualenv -p python3.6 env`

`. env/bin/activate`

`git clone ~repo~`

`cd ~repo~`

`pip install -r requirements.txt`

`export FLASK_APP=app.py`

Enable development mode

`export FLASK_ENV=development`

Enable production mode

`export FLASK_ENV=production`

Run app

`flask run`