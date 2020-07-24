from flask import Flask, send_from_directory
import os

app = Flask(
    __name__,  
    static_folder='./web/dist',
    static_url_path='', 
    )
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web", "dist")

@app.route('/')
def index():
    return send_from_directory(root, 'index.html')

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=False)