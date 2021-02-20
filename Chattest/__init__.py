from flask import Flask,request,Blueprint,Response
from flask import g
from datetime import datetime,date
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import config

db = SQLAlchemy()
migrate = Migrate()


app = Flask(__name__)
app.debug = True
app.config.from_object(config)
db.init_app(app)
migrate.init_app(app,db)

from Chattest.models import User

@app.before_request
def before_request():
    print('before_request')


@app.route('/')
def hello_world():
    print('------------------')
    userdata = User(pw='12345',create_data=datetime.now())
    db.session.add(userdata)
    db.session.commit()
    return 'hello world!!'+getattr(g,'str','111')

@app.route('/users')
def Users_get():
    print(User.query.all())
    return 'Sucess'

@app.route('/blog/<blog_page>',methods=['POST','GET'])
def blog(blog_page):
    articleid = request.values.get('test123','1',int)
    print(articleid)
    return '블로그입니다.'+blog_page

@app.route('/dt',methods=['POST'])
def dt():
    res = Response('테스트')
    res.headers.add('test','test123')
    res.set_data('233333')
    return res

def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str,fmt)
    return trans