import os
# import serverSlack 
import logging
import ssl as ssl_lib
import certifi
from flask import Flask, jsonify, request, json, Response, make_response
# from flask_restful import Resource, Api 
app = Flask(__name__)   


@app.route('/goodMorning', methods=['POST'])
def goodMorning():

    content = request.get_json(silent=False)
    
    print ("Petición: " + request.method)
    print ("Body: " + str(content))

    # print ("Headers: "+ request.headers)


    return '{ "return": "all right!!!" }', 200

# driver function 
if __name__ == '__main__': 
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    app.run(host="0.0.0.0", port=3000)
