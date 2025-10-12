# 代码生成时间: 2025-10-13 03:18:25
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
License Management System using the Bottle framework.
"""

from bottle import route, run, request, response, HTTPError
import json

# 数据库模拟，使用字典存储
licenses = {}

# 定义全局变量
LICENSES_ENDPOINT = '/licenses'
LICENSE_ENDPOINT = '/license/<license_id>'


@route(LICENSES_ENDPOINT, method='GET')
def get_licenses():
    """
    GET /licenses - 获取所有许可证信息。
    """
    return json.dumps(licenses)


@route(LICENSES_ENDPOINT, method='POST')
def create_license():
    """
    POST /licenses - 创建新的许可证。
    """
    try:
        data = request.json
        if not data or 'name' not in data or 'key' not in data:
            raise HTTPError(400, 'Missing required fields')
        license_id = len(licenses) + 1
        licenses[license_id] = data
        response.status = 201
        return {'id': license_id, 'data': data}
    except ValueError:
        raise HTTPError(400, 'Invalid JSON')


@route(LICENSE_ENDPOINT, method='GET')
def get_license(license_id):
    """
    GET /license/<license_id> - 根据ID获取单个许可证信息。
    """
    license = licenses.get(license_id)
    if not license:
        raise HTTPError(404, 'License not found')
    return json.dumps(license)


@route(LICENSE_ENDPOINT, method='PUT')
def update_license(license_id):
    """
    PUT /license/<license_id> - 更新指定ID的许可证信息。
    """
    try:
        data = request.json
        license = licenses.get(license_id)
        if not license:
            raise HTTPError(404, 'License not found')
        licenses[license_id] = data
        return {'id': license_id, 'data': data}
    except ValueError:
        raise HTTPError(400, 'Invalid JSON')


@route(LICENSE_ENDPOINT, method='DELETE')
def delete_license(license_id):
    """
    DELETE /license/<license_id> - 删除指定ID的许可证。
    """
    license = licenses.pop(license_id, None)
    if not license:
        raise HTTPError(404, 'License not found')
    return {'message': 'License deleted'}


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)
