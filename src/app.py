from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_todos = jsonify(todos)
    return json_todos

@app.route('/todos', methods=['POST'])
def add_new_todo():
    # print("Incoming request with the following body", request_body)
    # return 'Response for the POST todo'
    # Usando json.loads:
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)
    return jsonify(todos)
    
    #Usando request.json de flask:
    # request_body = request.json
    # todos.append(request_body)
    # return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)
    # return 'something'

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)