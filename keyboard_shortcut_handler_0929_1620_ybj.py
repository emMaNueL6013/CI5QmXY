# 代码生成时间: 2025-09-29 16:20:26
#!/usr/bin/env python

"""
A simple Bottle web application to handle keyboard shortcuts.
Usage:
    Press 'q' to quit the server.
    Press 'r' to restart the server.
"""

from bottle import route, run, request, response
import sys

# A dictionary to handle shortcuts
shortcuts = {
    # Quit server
    'q': lambda: sys.exit(0),
    # Restart server
    'r': lambda: run(host='localhost', port=8080),
}


# Route for handling keyboard input
@route('/shortcut', method='POST')
def handle_shortcut():
    # Get the input from the POST request
    data = request.json
    if data is None or 'key' not in data:
        response.status = 400
        return {'error': 'Invalid input, key is missing.'}

    key = data['key']
    if key not in shortcuts:
        response.status = 400
        return {'error': 'Unknown shortcut.'}

    # Execute the associated function for the shortcut
    try:
        shortcuts[key]()
    except Exception as e:
        response.status = 500
        return {'error': f'An error occurred: {e}'}

    # Return a success message if the shortcut is executed
    return {'message': f'Shortcut for {key} executed successfully.'}


def start_server():
    # Start the Bottle server
    run(host='localhost', port=8080)

# Entry point of the application
if __name__ == '__main__':
    start_server()
