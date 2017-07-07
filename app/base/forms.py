from flask_wtf import FlaskForm
from flask_babel import gettext as _
from wtforms.validators import ValidationError


class BaseForm(FlaskForm):
    class Meta:
        # csrf = True
        # csrf_secret = 'aa'
        # locales = ('ru_RU', 'ru')
        locales = ['ru']


# def unique(model, message=None):
#     def _unique(form, field):
#         user = model.query.filter(getattr(model, field.name) == field.data).first()
#         if user:
#             raise ValidationError(message or 'Такое название уже занято.')
#     return _unique

class Unique:
    def __init__(self, model, message=None):
        self.model = model
        self.message = message or _('Такое название уже занято.')

    def __call__(self, form, field):
        user =  self.model.query.filter(getattr(self.model, field.name) == field.data).first()
        if user:
            raise ValidationError(self.message)
