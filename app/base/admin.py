from flask_admin import BaseView, expose
from flask_login import current_user


class HelloView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/base/hello.html')

