import os
import logging
from logging import Formatter, FileHandler
from flask import Flask, request, jsonify, redirect, url_for, Markup, send_from_directory, make_response
from werkzeug.utils import secure_filename

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract



from ocr2 import process_image, get_date

UPLOAD_FOLDER = 'C:/Projects/flask_server/Receipts'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET","POST"])

def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))


    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>', methods=["GET","POST"])

def uploaded_file(filename):
    
    fila = os.path.join(app.config['UPLOAD_FOLDER'],filename)
    output = process_image(fila)
    output1 = get_date(fila)
    if output1 == None:
        DATE = 'null'
        return jsonify('Date: '+ str(DATE))
    else:
        DATE = output1
        return jsonify('Date: '+ str(DATE))
    resp = make_response(DATE)
    
    
    return jsonify({'DATE ': str(resp)})
app.run(debug=True)
