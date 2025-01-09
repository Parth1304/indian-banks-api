from flask import Flask, jsonify
import os
from dotenv import load_dotenv
from models import db, Bank, Branch


load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Initializing the database 
db.init_app(app)

#Routes
@app.route('/')
def home():
    return jsonify({
        "message": "Above are the API endpoints for getting bank details",
        "endpoints": {
            "Get all banks": "/get/banks",
            "Get branch by IFSC": "/get/branch/{ifsc}",
        }
    })

# get all banks
@app.route('/get/banks')        
def get_banks():
    try:
        banks = Bank.query.order_by(Bank.name).all()
        return jsonify([{
            'id': bank.id,
            'name': bank.name
        } for bank in banks])
    except Exception as e:
        return jsonify({'error': str(e)}), 500
  
# get specific branch details by providing ifsc  
@app.route('/get/branch/<ifsc>')
def get_branch_by_ifsc(ifsc):
    try:
        branch = db.session.query(Branch, Bank.name.label('bank_name'))\
            .join(Bank, Branch.bank_id == Bank.id)\
            .filter(Branch.ifsc == ifsc.upper())\
            .first()
        
        if not branch:
            return jsonify({'error': 'Branch not found'}), 404
        branch_data, bank_name = branch
        return jsonify({
            'ifsc': branch_data.ifsc,
            'bank_id': branch_data.bank_id,
            'branch': branch_data.branch,
            'address': branch_data.address,
            'city': branch_data.city,
            'district': branch_data.district,
            'state': branch_data.state,
            'bank_name': bank_name
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
