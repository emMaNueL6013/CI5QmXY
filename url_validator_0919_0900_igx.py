# 代码生成时间: 2025-09-19 09:00:30
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This script provides a simple Bottle application to validate the correctness of a given URL.
It checks for basic URL syntax and returns a success or error message accordingly.
"""

from bottle import route, run, request, response
from urllib.parse import urlparse
import re


# Define a list of allowed schemes for URL validation
ALLOWED_SCHEMES = ["http", "https"]

# Define a regular expression pattern to validate a basic URL structure
URL_PATTERN = re.compile(r"^(https?|ftp)://[^\s/$.?#].[^\s]*$")


def validate_url(url):
    """
    Validate the given URL against a simple regex pattern.
    If the URL is valid, return True; otherwise, return False.
    """
    return bool(URL_PATTERN.match(url))


def is_valid_scheme(url):
    """
    Check if the URL scheme is in the list of allowed schemes.
    Return True if it is; otherwise, return False.
    """
    parsed_url = urlparse(url)
    return parsed_url.scheme in ALLOWED_SCHEMES

\@route('/validate_url', method='POST')
def validate_url_endpoint():
    """
    Endpoint to validate a URL.
    It expects a JSON payload with a 'url' key.
    Returns a JSON response with a success message and validation result.
    """
    try:
        # Get the URL from the request body
        data = request.json
        url = data.get('url')

        # Check if URL is provided and is a string
        if not url or not isinstance(url, str):
            return {
                'error': 'URL is missing or not a string.',
                'valid': False
            }

        # Validate the URL schema and structure
        if not is_valid_scheme(url):
            return {
                'error': 'URL scheme is not allowed.',
                'valid': False
            }

        if not validate_url(url):
            return {
                'error': 'URL is not valid.',
                'valid': False
            }

        # Return a success message
        return {
            'message': 'URL is valid.',
            'valid': True
        }

    except Exception as e:
        # Return an error message in case of any exception
        return {
            'error': 'An error occurred during URL validation.',
            'valid': False,
            'details': str(e)
        }

# Set the response content type to JSON
response.content_type = 'application/json'

# Run the Bottle application on localhost at port 8080
run(host='localhost', port=8080)