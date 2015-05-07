from flask import Flask, request, session, escape, redirect, url_for, send_from_directory, render_template
from werkzeug import secure_filename
import os
import sys
import logging

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

app.config.from_object('setup')
myColor = os.environ['COLOR']
myLogo=myColor + '.logo'

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', color=myColor, filename=myLogo)
    
@app.route('/deploy', methods=['POST', 'GET'])
def deploy():
    """This calls dns registration to switch production to me
    """
    if request.method == 'POST':
        setConfd()
    return render_template('deploy.html', color=myColor, filename=myLogo)
    
def setConfd():
    cmd = 'curl ' \
        + os.environ['ETCD'] \
        + r'/v2/keys/confd/services/servers/blue-green -XPUT -d value="\"' \
        + os.environ['SERVER'] \
        + r'\""'
    os.system( cmd )  
      
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
              
@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], myLogo))
    return render_template('upload.html', filename=myLogo)

@app.route('/uploaded_file/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], secure_filename(filename))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)