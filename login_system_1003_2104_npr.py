# 代码生成时间: 2025-10-03 21:04:48
# login_system.py

"""
A simple user login system using the Bottle framework.

This script creates a basic web application that allows users to log in.
It includes error handling and follows Python best practices for clarity and maintainability.
"""

from bottle import route, run, request, response, redirect, template

# Dummy database for demonstration purposes
USER_DATABASE = {
    "user1": "password1",
    "user2": "password2"
}

# Route for the login page
@route('/login')
def login_page():
    return template("""
    <form action="/login" method="post">
        Username: <input type="text" name="username"/><br/>
        Password: <input type="password" name="password"/><br/>
        <input type="submit" value="Login"/>
    </form>
    """)

# Route for the login POST request
@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    user_pass = USER_DATABASE.get(username)
    
    # Error handling for non-existent user
    if user_pass is None:
        return template("""
            <p>Login failed: User not found.</p>
            <a href="/login">Try again</a>
            """)
    
    # Check if the password is correct
    if user_pass == password:
        response.set_cookie('username', username)
        return redirect('/home')
    else:
        return template("""
            <p>Login failed: Incorrect password.</p>
            <a href="/login">Try again</a>
            """)

# Route for the home page
@route('/home')
def home_page():
    # Check if the user is authenticated by checking the cookie
    if request.get_cookie('username'):
        return template("""
            <p>Welcome, {{username}}! You are now logged in.</p>
            <a href="/logout">Logout</a>
            """, username=request.get_cookie('username'))
    else:
        return redirect('/login')

# Route for logging out
@route('/logout')
def logout():
    response.delete_cookie('username')
    return redirect('/login')

if __name__ == '__main__':
    run(host='localhost', port=8080)