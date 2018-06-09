from flask import Flask, render_template, request, redirect, send_file
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
    
    cleanup.deleteZip()
    
    if request.method == "POST":
        cleanup.deleteZip()
            
        file = request.files['file']
        extension = file.filename.split('.')[-1]
        if extension == 'pdf':
            filename = secure_filename(file.filename)
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            pdf.split(filename)
            zip.makeZip()
            cleanup.resetSource(filename)
            
            return send_file('zipped_results/results.zip', attachment_filename = "results.zip")
            
        else: 
            return redirect(request.url)
        
        cleanup.deleteZip()    
    
    return render_template('index.html')        
        
@app.route('/health', methods=["GET"])
def health():
    app.logger.debug('health check')
    return "OK"
    
if __name__ == "__main__":
    
    app.logger.debug('Server up and running')
    app.run(debug=True, port=3000)