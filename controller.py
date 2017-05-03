import web
web.config.debug = False

from model import RegisterModel
from model import LoginModel

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/login', 'Login',
    '/logout', 'Logout',
    '/postregistration', 'Postregistration',
    '/checklogin', 'Checklogin'
)


app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'user': None})

#session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'user': None})

session_data = session._initializer

render = web.template.render('view/templete', base='mainlayout', globals={'session' : session_data,'user':session_data['user']})

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run(port=8888)

# classes
class Home:
    def GET(self):
        return render.home()

class Register:
    def GET(self):
        return render.register()

class Login:
    def GET(self):
        return render.login()

class Logout:
    def GET(self):
        session['user']= None
        session_data['user'] = None

        session.kill()
        return 'sucess'


class Postregistration:
    def POST(self):
        data = web.input()
        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)
        return data.name

class Checklogin:
    def POST(self):
        data = web.input()
        login_model = LoginModel.LoginModel()
        iscorrent =login_model.check_user(data)

        if iscorrent:
            session_data['user'] = iscorrent
            return iscorrent
        return 'error'


if __name__ == '_main_':
    app.run()