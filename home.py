from flask import 	(Flask, render_template, abort, jsonify, request,
					redirect, url_for)


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def welcome():
	if request.method == "POST":
		# do something!
		print("hmmm")
		return render_template("home.html")
	else:
		return render_template("home.html")
	
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)