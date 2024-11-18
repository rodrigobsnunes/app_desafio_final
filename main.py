from app.app import app,db

with app.app_context():
    db.create_all()
app.run('127.0.0.1',port=5000,debug=True)