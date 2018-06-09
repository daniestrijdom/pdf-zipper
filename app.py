from flask import Flask, render_template, request, redirect
from werkzeug import secure_filename
import logging
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.abspath('temp_uploads')

@app.route('/', methods=["GET", "POST"])
def index():
    import pdf
    import zip 
    import cleanup
    
    if request.method == "POST":
        
        file = request.files['file']
        extension = file.filename.split('.')[-1]
        if extension == 'pdf':
            filename = secure_filename(file.filename)
            print filename
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            pdf.split(filename)
            zip.makeZip()
            cleanup.resetSource(filename)
            
        else: 
            return redirect(request.url)
            
    return render_template('index.html')        
        
@app.route('/health', methods=["GET"])
def health():
    app.logger.debug('health check')
    return "OK"
    
if __name__ == "__main__":
    
    app.logger.debug('Server up and running')
    app.run(debug=True, port=3000)