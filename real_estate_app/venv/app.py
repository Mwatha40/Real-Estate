from flask import Flask, request, jsonify
from database import SessionLocal
from models import User, Property
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# Database session
db = SessionLocal()

@app.route('/register', methods=['POST'])
def register():
    # Your registration logic here
    pass

@app.route('/login', methods=['POST'])
def login():
    # Your login logic here
    pass

@app.route('/properties', methods=['GET'])
@jwt_required()
def list_properties():
    # Your property listing logic here
    pass
