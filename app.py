from flask import Flask, request, jsonify

# 1. Initialize the Flask application
app = Flask(__name__)

# 2. In-memory data store for users (stores user objects in a dictionary)
# The key is the user ID.
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
}
# Counter to generate unique IDs for new users
current_id = 3 

# Helper function to find a user by ID
def find_user(user_id):
    return users.get(user_id)

# --- API Endpoints (Routes) ---

# 1. GET - Retrieve all users or a specific user
@app.route('/users', methods=['GET'])
def get_users():
    """
    Handles GET requests to /users
    If 'id' query parameter is present, returns a single user.
    Otherwise, returns all users.
    """
    user_id = request.args.get('id', type=int)
    
    if user_id is not None:
        user = find_user(user_id)
        if user:
            # Return a specific user
            return jsonify({user_id: user}), 200
        else:
            # User not found
            return jsonify({"error": f"User with ID {user_id} not found"}), 404
    else:
        # Return all users
        return jsonify(users), 200

# 2. POST - Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    """
    Handles POST requests to /users
    Creates a new user and assigns a unique ID.
    Requires 'name' and 'email' in the request body.
    """
    global current_id
    
    # Check if request body is JSON
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
        
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    # Validate input
    if not name or not email:
        return jsonify({"error": "Missing 'name' or 'email' field"}), 400

    # Create new user object
    new_user = {"name": name, "email": email}
    
    # Store user and increment ID counter
    users[current_id] = new_user
    current_id += 1
    
    # Return the newly created user object with the assigned ID
    return jsonify({current_id - 1: new_user}), 201 # 201 Created

# 3. PUT - Update an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Handles PUT requests to /users/<user_id>
    Updates an existing user's details.
    Requires 'name' and/or 'email' in the request body.
    """
    user = find_user(user_id)
    
    if not user:
        return jsonify({"error": f"User with ID {user_id} not found"}), 404
    
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400
        
    data = request.get_json()
    
    # Update fields if they are present in the request body
    if 'name' in data:
        user['name'] = data['name']
    if 'email' in data:
        user['email'] = data['email']
        
    # Store the updated user back (in-memory update)
    users[user_id] = user 
    
    return jsonify({user_id: user}), 200

# 4. DELETE - Delete an existing user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Handles DELETE requests to /users/<user_id>
    Deletes the specified user.
    """
    if user_id in users:
        del users[user_id]
        # 204 No Content is often used for successful DELETE requests
        return '', 204 
    else:
        return jsonify({"error": f"User with ID {user_id} not found"}), 404

# Run the application
if __name__ == '__main__':
    # Setting debug=True allows the server to auto-reload on code changes
    # Do not use debug=True in a production environment
    app.run(debug=True)