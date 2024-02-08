from flask import Flask, request, jsonify
import mysql.connector
import atexit
from classifier import get_prediccion

app = Flask(__name__)

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="atc"
)

my_cursor = db_connection.cursor()

@app.route('/predict_category', methods=['POST'])
def predict_category():
    try:
        input_data = request.get_json()
        if not validate_input_data(input_data):
            return jsonify({"error": "Invalid json format",}), 400
        
        client_id = input_data["client_id"]
        if check_un_payment(client_id):
            return jsonify({"exito": False, "razon": "El cliente tiene impagos"}), 200
        
        predicted_category = get_prediccion(input_data["email_body"])
        return jsonify({"exito": True, "prediccion": predicted_category}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
#Close database connection when app server stops
def close_database_connections():
    try:
        if db_connection.is_connected():
            db_connection.close()

    except Exception as e:
        print(f"Error closing database connections: {str(e)}")

atexit.register(close_database_connections)


# Validate the format of the input data
def validate_input_data(input_data):
    required_keys = ["client_id", "fecha_envio", "email_body"]
    if not all(key in input_data for key in required_keys):
        return False
    if not isinstance(input_data["client_id"], int) or not isinstance(input_data["fecha_envio"], str) or not isinstance(input_data["email_body"], str):
        return False
    return True

# Check if a client has un-payments in the database
def check_un_payment(client_id):
    impagos_query = f"SELECT * FROM impagos WHERE client_id={client_id}"
    my_cursor.execute(impagos_query)
    result = my_cursor.fetchall()
    if result:
        return True
    return False
