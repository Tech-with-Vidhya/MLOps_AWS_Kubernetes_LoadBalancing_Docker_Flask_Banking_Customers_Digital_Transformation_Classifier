import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, jsonify, request
load_dotenv(Path(".env"))
import os


if os.environ.get("ENV", "dev") == "prod":
    load_dotenv(Path(".env.prod"))
if os.environ.get("ENV", "dev") == "dev":
    load_dotenv(Path(".env.dev"))

from logging_module import logger
from predictor import predictor
app = Flask(__name__)

@app.route("/health-status")
def get_health_status():
    logger.debug("Health check api version 6")
    resp = jsonify({"status": "I am alive, version 6"})
    resp.status_code = 200
    return resp


@app.route("/bank-classification", methods=['POST'])
def bank_classification():
    logger.debug("bank-classification API Called version 6")
    result = predictor()
    print(result)
    resp = jsonify({"result": result})
    resp.status_code = 200
    return resp
    

if __name__ == "__main__":
    app.run(debug=True)
