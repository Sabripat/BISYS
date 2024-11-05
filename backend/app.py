from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_folder='../frontend', template_folder='../templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('../frontend', path)

if __name__ == '__main__':
    app.run(debug=True)
    
