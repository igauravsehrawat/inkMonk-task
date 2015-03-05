
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

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
# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not

metadata = MetaData()
image_hexcodes = Table('image_hexcodes', metadata,
                    Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
                    Column('count', Integer),
                    Column('url_given', String),
                    Column('hexcodes', String)
                    )
metadata.create_all(engine)
ins = image_hexcodes.insert()

####DON'T MESS UP THE CODE, don't JUMBLE UP.......BAD PRACTICE######



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('frontend.html')
    # return "running me..how fair"


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Check if the file is one of the allowed types/extensions
    if file and allowed_file(file.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
        return redirect(url_for('uploaded_file',
                                filename=filename))

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)



class ProcessImage(restful.Resource):
#lets do in hash


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



api.add_resource(ProcessImage, '/image_handling')

if __name__ == '__main__':
    app.run(debug=True) #in debug given error winreg
                #strange error
            #what is the workflow of flask app
