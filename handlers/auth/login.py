from handlers.bloghandler import BlogHandler
from models.model_users import User


class Login(BlogHandler):
    def get(self):
        self.render('loginForm.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect('/')
        else:
            msg = 'Invalid login'
            self.render('loginForm.html', error = msg)
