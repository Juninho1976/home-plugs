from flask import 	(Flask, render_template, abort, jsonify, request,
					redirect, url_for)

import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def welcome():
	if request.method == "POST":
		# do something!
		
		print("Here we go!")
		print("value of plug1", request.form['plug1']) 
		'''
		print("value of plug2", request.form['plug2']) 
		print("value of plug3", request.form['plug3']) 
		print("value of plug4", request.form['plug4']) 
		print("value of plug5", request.form['plug5']) 
		
		'''
		'''
		if request.form['plug1ON'] == "Plug1On":
			os.system('sudo python /home/pi/RakPython/Energenie/pyenergenie-master/src/switch1on.py')
			print("Turning on Plug 1")
			
		if request.form['plug2'] == "Plug2On":
			os.system('sudo python /home/pi/RakPython/Energenie/pyenergenie-master/src/switch2on.py')
			print("Turning on Plug 2 Coffee")
		'''
		
		
		
		return render_template("home.html")
	else:
		return render_template("home.html")
	
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)