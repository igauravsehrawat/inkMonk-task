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
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Sequence, select

engine = create_engine('sqlite:///:memory:', echo=True)


app = Flask(__name__)
api = restful.Api(app)

#db related code

metadata = MetaData()
image_hexcodes = Table('image_hexcodes', metadata,
                    Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
                    Column('count', Integer),
                    Column('url_given', String),
                    Column('hexcodes', String)
                    )
metadata.create_all(engine)
ins = image_hexcodes.insert()

##################
def root():
  return app.send_static_file('frontend.html')


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

        metadata = MetaData()
        image_hexcodes = Table('image_hexcodes', metadata,
                            Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
                            Column('count', Integer),
                            Column('url_given', String),
                            Column('hexcodes', String)
                            )
        metadata.create_all(engine)
        ins = image_hexcodes.insert()
        conn = engine.connect()

        s = select([image_hexcodes])
        checking_something = conn.execute(s)

        for row in checking_something:
            print "print row subset 4"
            print row[4]
            if row['hexcodes']==request.form['data']:
                print "we found it"
            else:
                conn.execute(ins,count=0, url_given = request.form['data'], hexcodes=str(all_hex_codes))




        # all_hex_codes = None
        return {'response': all_hex_codes}

#lets do in db , two ways
@app.route('/')


api.add_resource(ProcessImage, '/<string:url_id>')

if __name__ == '__main__':
    app.run(debug=True) #in debug given error winreg
                #strange error
