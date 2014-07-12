import os
from flask import Flask, render_template, send_from_directory, jsonify

#-----------------------------------
# initialization
#-----------------------------------

app = Flask(__name__)

app.config.update(
	DEBUG = True,
)

#-----------------------------------
# controllers
#-----------------------------------

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')

@app.route("/companies", methods=['GET'])
def search():
	sample = {"results":[{"organization":"Buzzfeed",
						  "description":"BuzzFeed is a media company providing social news and entertainment-related information and videos.",
						  "funding":"46.3M",
						  "industries":["News","Media"],
						  "location":"New York,NY",
						  "founders":["Jonah Peretti","John Johnson"],
						  "founded":"2008",
						  "technologies":["Javascript","Python","Perl"],
						  "investors":["Lerer Ventures","RRE Ventures"],
						  "size":"100-500",
						  "stargazers":1000,
						  "twitter-id":"buzzfeed",
						  "github-url":"http://github.com/buzzfeed",
						  "crunchbase-url":"http://crunchbase.com/organization/buzzfeed",
						  "logo-url":"http://a3.images.crunchbase.com/image/upload/c_pad,h_98,w_98/v1397183627/f8f063b7cc03d05841d03a3c764936a6.png"}]}

	return jsonify(sample)

#-----------------------------------
# launch
#-----------------------------------

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
