from flask import Flask, request, jsonify

app = Flask(__name__)

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
