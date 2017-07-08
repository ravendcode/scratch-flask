import os
from flask_script import Command, Option


class TranslateCommand(Command):
    "Translate content"

    def __init__(self, lang=['ru', 'en']):
        self.lang = lang

    def get_options(self):
        return [
            Option('-l', '--lang', dest='lang', default=self.lang),
        ]

    def run(self, lang):
        clear_lang = lang if type(lang) == list else lang.split(',')
        os.system('pybabel extract -F babel.cfg -k lazy_gettext -o translations/messages.pot app templates')
        for l in clear_lang:
            os.system('pybabel init -i translations/messages.pot -d translations -l ' + l)
        os.system('pybabel compile -d translations')
        print('done')
