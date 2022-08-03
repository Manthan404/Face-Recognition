from flask import Flask

#WSGI APplication
app=Flask(__name__)

#Decorator
@app.route('/')
def welcome():
    return 'Welcome to the META'

@app.route('/hello')
def hello():
    return 'Hello'

if __name__=='__main__':
    app.run(debug=True)   
