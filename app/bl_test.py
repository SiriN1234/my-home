from flask import Blueprint
from flask import Flask, request, jsonify
import pandas as pd

# ----- house_welfare blueprint set ----------------------------------------------------------------------------
blue_test = Blueprint("blue_test", __name__)
#---------------------------------------------------------------------------------------------------------------

# ----- house_welfare root -------------------------------------------------------------------------------------
@blue_test.route("/api/blue_test")
def house_welfare_home():
    return "house_welfare"
# --------------------------------------------------------------------------------------------------------------