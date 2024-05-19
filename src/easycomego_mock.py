import sys
import json
from flask import Flask, request, jsonify, make_response, Response
import pprint
import logging
from logging.handlers import TimedRotatingFileHandler, RotatingFileHandler
import uuid
import socket
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# CONSTANTS
api_host = socket.gethostname()
api_port = 39000
api_id = "easycomego_mock_ws"

# Work directory setup
script_dir = os.path.dirname(os.path.realpath(__file__))
home_dir = "/".join(script_dir.split("/")[:-1])
log_dir = "{home_dir}/logs".format(home_dir=home_dir)

DEP_CODE_LIST = [
   "EASY-MY-PRT-KLANG",
   "EASY-MY-BU",
   "EASY-SG-HF",
   "EASY-SG-BV"
]

DEST_CODE_LIST = [
   "EASY-MY-PRT-KLANG",
   "EASY-MY-BU",
   "EASY-SG-HF",
   "EASY-SG-BV"
]

TRANS_TYPE_LIST = [
   "BUS",
   "SHIP",
   "VAN",
   "MPV",
   "EXEC_TAXI"
]

ROUTES_LIST = []
for i in DEP_CODE_LIST:
   for j in DEST_CODE_LIST:
      for k in TRANS_TYPE_LIST:
         if i != j:
           ROUTES_LIST.append({
              "transportCode": k,
              "departureCode": i,
              "destinationCode": j
           })
         # end if
      # end for
   # end for
# end for

@app.route('/getRoutes', methods=['GET'])
def getRoutes():
  return jsonify(ROUTES_LIST)
# end def

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=api_port)
# end if