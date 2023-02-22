from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired

class LeagueFrom(FlaskForm):
  name = StringField("Name", validators=[DataRequired()])
  display_pic = StringField("Image URL")
