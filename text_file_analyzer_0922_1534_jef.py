# 代码生成时间: 2025-09-22 15:34:04
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Text File Analyzer using Bottle framework.
This program analyzes the content of a text file and provides basic statistics.
"""

from bottle import route, run, request, response, static_file
import os
import statistics
import textwrap


# Define the path to the directory where uploaded files will be stored
UPLOAD_FOLDER = './uploads/'

# Define the path to the directory where static files are located
STATIC_FOLDER = './static/'

# Create the uploads directory if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Define the maximum file size in bytes (25MB)
MAX_FILE_SIZE = 25 * 1024 * 1024

@route('/')
def index():
    # Serve the index.html file
    return static_file('index.html', root=STATIC_FOLDER)

@route('/upload', method='POST')
def upload_file():
    # Check if the request contains a file
    if 'file' not in request.files:
        return {"error": "No file part"}

    file = request.files['file']
    if file.file.length > MAX_FILE_SIZE:
        return {"error": "File too large"}

    # Save the file to the uploads directory
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Analyze the file content
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()
            # Calculate basic statistics
            length = len(file_content)
            line_count = file_content.count('
') + 1
            word_count = len(file_content.split())
            sentence_count = len(textwrap.wrap(file_content, break_on_hyphens=False))
            mean_word_length = statistics.mean(len(word) for word in file_content.split())

        # Return the analysis results
        return {
            "length": length,
            "line_count": line_count,
            "word_count": word_count,
            "sentence_count": sentence_count,
            "mean_word_length": mean_word_length
        }
    except Exception as e:
        # Handle any exceptions that occur during file analysis
        return {"error": str(e)}

# Run the Bottle server
run(host='localhost', port=8080, debug=True)