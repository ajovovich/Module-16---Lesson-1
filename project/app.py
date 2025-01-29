from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost:3306/test_api'
db = SQLAlchemy(app)
migrate = Migrate(app, db) 

class Sum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num1 = db.Column(db.Integer, nullable=False)
    num2 = db.Column(db.Integer, nullable=False)
    result = db.Column(db.Integer, nullable=False)

@app.route('/sum/result/<int:result_filter>', methods=['GET'])
def get_sums_by_result(result_filter):
    sums = Sum.query.filter_by(result=result_filter).all()
    if not sums:
        return jsonify({"message": "No sums found for this result."}), 404 
    sum_list = [{'id': s.id, 'num1': s.num1, 'num2': s.num2, 'result': s.result} for s in sums]
    return jsonify(sum_list)

@app.route('/calculate', methods=['POST'])
def calculate():
    
    data = request.get_json()

    if 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Missing num1 or num2'}), 400

    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
    except ValueError:
        return jsonify({'error': 'Invalid input. num1 and num2 must be numbers'}), 400

    result = num1 + num2
    return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run(debug=True)
