from flask import Flask, request
from flask.ext import restful
from flask.ext.sqlalchemy import SQLAlchemy
from SO_color_algo import ColorExtractor
import struct
import Image
import scipy
import scipy.misc
import scipy.cluster
from sqlalchemy import create_engine


engine = create_engine('sqlite:///:memory:', echo=True)


app = Flask(__name__)
api = restful.Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images_hexcodes.db'
db = SQLAlchemy(app)

class ImageRequested(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)
    url_given = db.Column(db.Text)
    hexcodes = db.Column(db.Text)

db.create_all()


class ProcessImage(restful.Resource):
#lets do in hash
    def get(self, url_id):
        return {'response': 'are you lost ?'}

    def put(self,url_id):
        response = request.form['data']
        return {'response': response}

    def post(self, url_id):
        print url_id
        all_hex_codes = [ColorExtractor(request.form['data'])]
        u = ImageRequested(0,url_id,all_hex_codes)
        db.add(u)
        # all_hex_codes = None
        return {'response': all_hex_codes}

#lets do in db , two ways
# api.add_resource(ProcessImage, '/')
api.add_resource(ProcessImage, '/<string:url_id>')

if __name__ == '__main__':
    app.run(debug=True) #in debug given error winreg
                #strange error
