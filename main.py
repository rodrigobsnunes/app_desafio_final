from app.app import app,db

with app.app_context():
    db.create_all()
app.run('0.0.0.0',port=8080,debug=True)