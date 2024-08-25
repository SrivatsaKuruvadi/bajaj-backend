from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get("data", [])
    user_id = "Kuruvadi_Srivatsa_27082004"  
    email = "srivatsakuruvadi@gmail.com"
    roll_number = "21BCE9062"

    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]

    lowercase_alphabets = [item for item in alphabets if item.islower()]
    highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
