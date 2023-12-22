from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def hello():
    name={'username':'tester'}
    title='bark'
    posts=[
        {
            'author':{'username':'root'},
            'body':"hi i'm root"
        },
        {
            'author':{'username':'test'},
            'body':"hi i'm test"
        },
    ]
    # datas=[
    #     {'name':'a','age':'8'},
    #     {'name':'b','age':'7'},
    #     {'name':'b','age':'8'},
    #     {'name':'f','age':'9'},
    #     {'name':'d','age':'11'},
    #     {'name':'e','age':'12'},
    # ]
    return render_template('index.html',name=name,title=title,posts=posts)


if __name__=="__main__":
    app.run(host='0.0.0.0')