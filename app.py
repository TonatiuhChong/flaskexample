from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (acting as a database)
items = []

# Create an item (POST request)
@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json()  # Get JSON data from the request body
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    
    if not name or not description or not price:
        return jsonify({"error": "Missing data"}), 400
    
    item = {
        'id': len(items) + 1,
        'name': name,
        'description': description,
        'price': price
    }
    items.append(item)
    return jsonify(item), 201  # Return the created item with a 201 status

# Get all items (GET request)
@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Get a single item by ID (GET request)
@app.route('/api/items/<int:id>', methods=['GET'])
def get_item(id):
    item = next((item for item in items if item['id'] == id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

# Update an item by ID (PUT request)
@app.route('/api/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = next((item for item in items if item['id'] == id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    
    data = request.get_json()
    item['name'] = data.get('name', item['name'])
    item['description'] = data.get('description', item['description'])
    item['price'] = data.get('price', item['price'])
    
    return jsonify(item)

# Delete an item by ID (DELETE request)
@app.route('/api/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = next((item for item in items if item['id'] == id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    
    items.remove(item)
    return jsonify({"message": "Item deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)