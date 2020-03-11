import os
import logging
import ssl as ssl_lib
import certifi
from flask import Flask, jsonify, request, json, Response, make_response

app = Flask(__name__)   



@app.route("/flaskServer", methods=["POST"])
def flaskServer():

    # Parse the request payload
    form_json = json.loads(request.form["payload"])

    print ("aaaa")
    print(form_json)

    return make_response("", 200)

# driver function 
if __name__ == '__main__': 
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
    app.run(host="0.0.0.0", port=3000)
