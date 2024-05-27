#!/usr/bin/python3
""" Index file for the api"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


# @app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False)
