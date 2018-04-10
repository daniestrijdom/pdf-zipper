from flask import Flask, render_template, request
import logging

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/health', methods=["GET"])
def health():
    app.logger.debug('health check')
    return "OK"
    
if __name__ == "__main__":
    app.logger.debug('Server up and running')
    app.run(debug=True, host='0.0.0.0', port=3000)