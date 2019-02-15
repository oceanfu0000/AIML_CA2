# For app.py
from flask import Flask, request
import sys
import os
import ca2_ridge_model as hdbPrice

app = Flask(__name__)

# return a default response for root folder
@app.route("/")
def root():
	return "<h1>HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO</h1>"

# accept GET/POST methods
# put {webhooklink}/dialogflow
@app.route("/dialogflow", methods=["post"])
def hdb_predict():
	result={"fulfillmentText":"na"}
	try:
		# build a request object
		req = request.get_json(force=True)
		# Fetch parameters
		if req["queryResult"]["intent"]["displayName"] == "Predict":
			parameters = input["queryResult"]["parameters"];
			# get year
			year = int(parameters["year"])
			# get area
			area = parameters["town"]
			# get flat type
			flat = paramters["flat_type"]
			
			print((year, area, flat))
			
			y_pred = hdbPrice.predict_price(year, flat, area)
			
			# prepare output
			output = "The predicted price is {}".format(y_pred)
			
			result = {"fulfillmentText": output}
			
	except Exception as e:
		print("error: ", e)
		
	return json.dumps(result)
	
