import wtforms as f

from ..base.forms import BaseForm

class PostCreateForm(BaseForm):
    title = f.StringField('Title', [
                             f.validators.Length(min=2, max=25)])
    body = f.TextAreaField('Body', [f.validators.Required()])
