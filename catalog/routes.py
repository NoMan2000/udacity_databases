from flask import Flask, render_template, request, session, redirect, url_for
from models import db, Articles, Author
from forms import ArticlesForm, AuthorsForm
import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/michaelsoileau'
db.init_app(app)

app.secret_key = "development-key"

route_list = dict(
  index = '/',
  about = '/about',
  articles = '/articles',
  authors = '/authors',
)

@app.route(route_list.get('index', '/'))
@app.route('/index')
@app.route('/index.html')
def index():
  return render_template("index.html", route_list=route_list)

@app.route(route_list.get('about'))
def about():
  return render_template("about.html")

@app.route(route_list.get('articles'), methods=["GET", "POST"])
def articles_list():

  form = ArticlesForm()

  all_articles = Articles.query.all()
  all_authors = Author.query.all()
  if request.method == "POST":
    if form.validate() != False:
      newArticle = Articles(
        request.form.get('author'),
        form.title.data,
        form.slug.data,
        form.lead.data,
        form.body.data,
        datetime.datetime.now()
      )
      print(newArticle)
      db.session.add(newArticle)
      db.session.commit()

  return render_template('articles.html', form=form, all_articles=all_articles, all_authors=all_authors)

@app.route(route_list.get('authors'), methods=["GET", "POST"])
def login():
  if 'email' in session:
    return redirect(url_for('home'))

  form = AuthorsForm()

  if request.method == "POST":
    if form.validate() == False:
      return render_template("authors.html", form=form)
    else:
      name = form.name.data

      form = AuthorsForm.query.filter_by(name=name).first()

      return redirect(url_for('authors.html'), form=form)

  elif request.method == 'GET':
    return render_template('authors.html', form=form)


if __name__ == "__main__":
  app.run(debug=True)