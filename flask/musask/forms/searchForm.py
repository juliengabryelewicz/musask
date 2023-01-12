from wtforms import Form, StringField, SubmitField, validators

class SearchForm(Form):
    search = StringField('Search', [validators.Length(min=2, max=255)])
    submit = SubmitField('Search')