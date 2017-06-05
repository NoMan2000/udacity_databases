# SQL/Flask App

First, you need to have the correct python version, see `.python-version` and run `pip install -r requirements.txt`.
 
This will download the files used.

You *must* have the postgres files installed.  If you do not, this will not work.

Line 8 in `routes.py` has this line:

`app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/michaelsoileau'`

Change that line to whatever your database is.  The unzipped .sql file is over a hundred megabytes, and that isn't allowed for uploads to Git.

To run the app, type 

    export FLASK_APP=routes.py
    flask run

Then visit `localhost:5000` and you should be up and running.