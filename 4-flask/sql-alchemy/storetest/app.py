from flask import Flask
from models import Base, Store
from flask_sqlalchemy import SQLAlchemy

app =  Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.before_first_request
def setup():
    # Recreate database each time for demo
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    db.session.add(Store('Calculator', 'Bobs Electronics', 89, "electronics"))
    db.session.add(Store('Sour Patch Kids', 'Candy4U', 4, "food"))
    db.session.commit()

@app.route('/')
def root():
    itempage = db.session.query(Store).all()
    return u"<br>".join([u"Name: {0} Price: {1} Seller: {2} Type: {3}".format(item.itemname, item.price, item.seller, item.itemtype) for item in itempage])

if __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1', 5000)
