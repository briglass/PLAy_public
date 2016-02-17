from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length
    
class UserEditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    favcolor = TextAreaField('favcolor', validators = [Length(min = 0, max = 140)])
    email = TextAreaField('email', validators = [Length(min = 0, max = 140)])
