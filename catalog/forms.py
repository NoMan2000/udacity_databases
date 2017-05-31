from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class Articles(Form):
  title = StringField('Article Title', validators=[DataRequired("Please enter a valid title.")])
  slug = StringField('Article Slug', validators=[DataRequired("Please enter an article slug.")])
  lead = StringField('Lead', validators=[DataRequired("Please Enter the lead field.")])
  body = PasswordField('Body', validators=[DataRequired("Please enter what you want this article to say.")])
  submit = SubmitField('Add Article')

class Authors(Form):
  name = StringField('Name', validators=[DataRequired("Please enter the Author's name.")])
  bio = PasswordField('Bio', validators=[DataRequired("Please enter a Bio for the Author.")])
  submit = SubmitField('Add Author')
