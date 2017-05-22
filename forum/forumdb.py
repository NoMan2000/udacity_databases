# "Database code" for the DB Forum.

import datetime
import psycopg2

DBNAME = 'michaelsoileau'

def connect():
  return psycopg2.connect(database=DBNAME)

def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = connect()
  c = db.cursor()
  c.execute("SELECT content, time FROM posts ORDER BY time DESC")
  posts = c.fetchall()
  db.close()
  return posts

def add_post(content):
  if not content:
    return get_posts()

  db = connect()
  c = db.cursor()
  c.execute("INSERT INTO posts (content, time)"
            "VALUES (%s, %s)",(content, datetime.datetime.now(),))
  db.commit()
  db.close()
  """Add a post to the 'database' with the current timestamp."""
  return get_posts()


