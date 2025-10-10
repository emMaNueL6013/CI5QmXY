# 代码生成时间: 2025-10-10 22:04:38
from bottle import route, run, template, request
from random import randint
import json

# Generate a list of random numbers for demonstration purposes.
# In a real scenario, you would fetch this data from a database or other source.
def generate_sample_data():
    return [randint(1, 100) for _ in range(10)]

# Route to serve the main page with the drag and drop sorting component.
@route('/')
def index():
    return template('drag_and_drop_sorting_template')

# Route to handle the AJAX request to save the new order of items.
@route('/save_order', method='POST')
def save_order():
    try:
        # Get the new order from the request body in JSON format.
        new_order = json.loads(request.body.read())
        # Process the new order here.
        # For this example, we will just print it to the console.
        print('New order:', new_order)
        # Return a success message.
        return json.dumps({'status': 'success', 'message': 'Order saved successfully.'})
    except Exception as e:
        # Handle any errors that occur during processing.
        return json.dumps({'status': 'error', 'message': str(e)})

# Start the Bottle.py application.
# By default, it runs on localhost port 8080.
# You can specify host and port as needed.
if __name__ == '__main__':
    run(host='localhost', port=8080)
