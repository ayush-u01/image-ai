import db
import os
import json
from flask import Flask, request, render_template,redirect, url_for
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from dotenv import load_dotenv


app = Flask(__name__)
load_dotenv()


app.config['CLOUDINARY_CLOUD_NAME'] = os.environ.get('CLOUDINARY_CLOUD_NAME')
app.config['CLOUDINARY_API_KEY'] = os.environ.get('CLOUDINARY_API_KEY')
app.config['CLOUDINARY_API_SECRET'] = os.environ.get('CLOUDINARY_API_SECRET')

@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("signin.html")

@app.route('/creator', methods = ['GET', 'POST'])
def creator():
    return render_template("creator.html")



@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    return render_template("signup.html")



@app.route('/signin', methods = ['GET', 'POST'])
def signin():
    status, username = db.check_user()

    data = {
        "username": username,
        "status": status
    }

    return json.dumps(data)



@app.route('/register', methods = ['GET', 'POST'])
def register():
    status = db.insert_data()
    return json.dumps(status)

@app.route('/upload', methods=['POST'])
def upload_image():
    image = request.files['image']

    if image:

        result = upload(image, use_filename=True, unique_filename=True)

        cloudinary_url = result['secure_url']

        return True

    return False

if __name__ == '__main__':
    app.run(debug = True)