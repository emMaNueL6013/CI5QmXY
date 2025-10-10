# 代码生成时间: 2025-10-11 03:01:25
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Management Tool
A simple Bottle-based web application to manage projects.
"""

from bottle import Bottle, run, request, response, template
import json

# Initialize the Bottle application
app = Bottle()

# In-memory project storage for simplicity
projects = []

# Route to get all projects
@app.get("/projects")
def get_projects():
    """
    Retrieves a list of all projects.
    """
    response.content_type = 'application/json'
    return json.dumps(projects)

# Route to create a new project
@app.post("/projects")
def create_project():
    """
    Creates a new project.
    """
    try:
        data = request.json
        if not data or 'name' not in data:
            response.status = 400
            return json.dumps({'error': 'Invalid project data'})
        project = {'name': data['name'], 'id': len(projects) + 1}
        projects.append(project)
        response.status = 201
        return json.dumps(project)
    except Exception as e:
        response.status = 500
        return json.dumps({'error': 'Internal Server Error'})

# Route to get a specific project by ID
@app.get("/projects/<id:int>")
def get_project(id):
    """
    Retrieves a project by its ID.
    """
    for project in projects:
        if project['id'] == id:
            return json.dumps(project)
    response.status = 404
    return json.dumps({'error': 'Project not found'})

# Route to update a project
@app.put("/projects/<id:int>")
def update_project(id):
    "