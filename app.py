from flask import Flask, jsonify, request

app = Flask(__name__)

# Liste factice d'items (en mémoire)
items = [
    {"id": 1, "name": "Item 1", "description": "Premier item factice"},
    {"id": 2, "name": "Item 2", "description": "Deuxième item"}
]

@app.route('/', methods=['GET'])
def home():
    return "Hello World ! Bienvenue sur l'API Flask."

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    if not new_item or 'name' not in new_item or 'description' not in new_item:
        return jsonify({"error": "Données item invalides"}), 400
    new_id = max([item['id'] for item in items]) + 1 if items else 1
    new_item['id'] = new_id
    items.append(new_item)
    return jsonify({"message": "Item ajouté", "item": new_item}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items  # On utilise global car items est défini en dehors de la fonction
    original_length = len(items)
    items = [item for item in items if item['id'] != item_id]
    
    if len(items) == original_length:
        return jsonify({"error": f"Item avec l'ID {item_id} non trouvé"}), 404
    
    return jsonify({"message": f"Item {item_id} supprimé avec succès"}), 200
