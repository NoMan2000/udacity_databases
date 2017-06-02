from flask import Flask, render_template, request, session, redirect, url_for
from models import db, Articles, Author
from forms import ArticlesForm, AuthorsForm
import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/michaelsoileau'
db.init_app(app)

app.secret_key = "development-key"

route_list = dict(
    index='/',
    about='/about',
    articles='/articles',
    authors='/authors',
    top_articles='/articles/top',
    top_authors='/authors/top',
    errors_per_day='/errors'
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
            db.session.add(newArticle)
            db.session.commit()
            form = ArticlesForm()  # Re-render the form

    return render_template('articles.html', form=form, all_articles=all_articles, all_authors=all_authors)


@app.route(route_list.get('top_articles'))
def top_articles():
    grouped = db.engine.execute('''
                    SELECT 
                    COUNT(log.path) AS totalViews,
                    articles.slug,
                    articles.title,
                    authors.name
                    FROM log, articles, authors
                    WHERE log.path != '/' AND 
                    articles.slug = SUBSTR(log.path, LENGTH('/article/') + 1)
                    AND articles.author = authors.id
                    GROUP BY 
                    articles.slug, 
                    authors.name,
                    articles.title
                    ORDER BY totalViews DESC
                
                    ''').fetchall()

    return render_template('articles-top.html', top_articles=grouped)


@app.route(route_list.get('top_authors'))
def top_authors():
    grouped = db.engine.execute('''
                    SELECT 
                    COUNT(authors.id) AS totalViews,
                    authors.name
                    FROM log, authors, articles
                    WHERE log.path != '/' AND 
                    articles.slug = SUBSTR(log.path, LENGTH('/article/') + 1)
                    AND articles.author = authors.id
                    GROUP BY 
                  	authors.name,
                    authors.id
                   
                    ORDER BY totalViews DESC

                    ''').fetchall()

    return render_template('authors-top.html', top_articles=grouped)


#  Begin date check
@app.route(route_list.get('errors_per_day'))
def error_route():
    errors = db.engine.execute('''
                        WITH t AS 
                        (SELECT DATE(log.time) AS failureDate,
                        ROUND((SUM(CASE WHEN 
                            SUBSTRING(log.status, 0, 4)::integer >= 400
                            THEN 1
                            ELSE 0
                            END
                        )  * 100.0)::decimal / (COUNT(log.status)),1) AS totalFailures
                        FROM log GROUP BY DATE(log.time)
                        )
                        SELECT t.totalFailures AS failure, to_char(t.failureDate, 'Month DD, YYYY') AS date
                        FROM t
                        GROUP BY t.totalFailures, t.failureDate
                        HAVING t.totalFailures > 1

                        ''').fetchall()

    return render_template('errors.html', errors=errors)


@app.route('/articles/delete/<int:article_id>', methods=['POST'])
def delete_routes(article_id):
    article = Articles.query.filter_by(id=article_id).first()
    db.session.delete(article)
    db.session.commit()
    return articles_list()


@app.route(route_list.get('authors'), methods=["GET", "POST"])
def authors():
    form = AuthorsForm()
    all_authors = Author.query.all()
    if request.method == "POST":
        if form.validate() == False:
            return render_template("authors.html", form=form, all_authors=all_authors)
        else:
            newAuthor = Author(
                request.form.get('author'),
                form.name.data,
                form.bio.data,
            )
            db.session.add(newAuthor)
            db.session.commit()
            form = AuthorsForm()  # Re-render the form

            return render_template('authors.html', form=form, all_authors=all_authors)

    elif request.method == 'GET':
        return render_template('authors.html', form=form, all_authors=all_authors)


if __name__ == "__main__":
    app.run(debug=True)
