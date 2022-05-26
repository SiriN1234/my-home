from flask import Blueprint
from flask import Flask, request, jsonify
import pandas as pd

# ----- house_welfare blueprint set ----------------------------------------------------------------------------
app = Blueprint("blue_test", __name__)
#---------------------------------------------------------------------------------------------------------------

# ----- house_welfare root -------------------------------------------------------------------------------------
@app.route("/api/blue_test")
def house_welfare_home():
    return "house_welfare"
# --------------------------------------------------------------------------------------------------------------