from flask import Flask, request
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = restful.Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///image_processing.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

db.create_all()


class ProcessImage(restful.Resource):
    def get(self, url_id):
        return {'response': 'are you lost ?'}

    def put(self,url_id):
        response = request.form['data']
        return {'response': response}

    def post(self, url_id):
        return {'response': "from post request"}


#lets do in hash
#lets do in db , two ways
# api.add_resource(ProcessImage, '/')
api.add_resource(ProcessImage, '/<string:url_id>')

if __name__ == '__main__':
    app.run(debug=True)
