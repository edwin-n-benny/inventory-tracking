from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/inventory', methods=['GET'])
def get_inventory():
        # Sample inventory data
            inventory_data = {
                            "items": [
                                            {"id": 1, "name": "Item A", "quantity": 100},
                                                        {"id": 2, "name": "Item B", "quantity": 50},
                                                                    {"id": 3, "name": "Item C", "quantity": 200},
                                                                            ]
                                }
                return jsonify(inventory_data)

            if __name__ == '__main__':
                    app.run(host='0.0.0.0', port=8080)

