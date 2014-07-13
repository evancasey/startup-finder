import os
from flask import Flask, render_template, send_from_directory, jsonify, url_for, redirect, request
import pdb
import json

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

@app.route("/companies", methods=['POST'])
def search():
	
	locations = request.json['data']['locations']
	languages = request.json['data']['languages']

	companies = [{"organization":"Buzzfeed",
				"description":"BuzzFeed is a media company providing social news and entertainment-related information and videos.",
				"funding":"46.3M",
				"industries":["News","Media"],
				"location":"New York, New York",
				"founders":["Jonah Peretti","John Johnson"],
				"founded":"2008",
				"technologies":[{"name":"Javascript","lines": 14131},
								  {"name":"Python","lines": 6104},
								  {"name":"Perl","lines": 4251}],						  						  
				"size":"100-500",
				"stargazers":1000,
				"twitter-id":"buzzfeed",
				"github-url":"http://github.com/buzzfeed",
				"crunchbase-url":"http://crunchbase.com/organization/buzzfeed",
				"logo-url":"http://a3.images.crunchbase.com/image/upload/c_pad,h_98,w_98/v1397183627/f8f063b7cc03d05841d03a3c764936a6.png"},

				{"organization":"Clever",
				"description":"With unique experiences in education and technology, the Clever team understands the data challenges that schools and developers face. Our mission is to make powerful educational software easy to build and easy to deploy.",							
				"funding":"13.3M",
				"industries":["Education"],
				"location":"San Francisco, California",
				"founders":["Rafael Garcia","Tyler Bosmeny","Daniel Carroll"],
				"founded":"2012",
				"technologies":[{"name":"Go","lines": 3189},
								  {"name":"Javascript","lines": 2414},
								  {"name":"Python","lines": 1251}],						  						  
				"size":"10-50",
				"stargazers":1000,						  
				"github-url":"http://github.com/clever",						  
				"logo-url":"http://a2.images.crunchbase.com/image/upload/c_pad,h_98,w_98/v1399399847/axakmjpu1rupw8dtwqns.png"},

				{"organization":"Nextdoor",
				"description":"Nextdoor is a private social network that enables members to communicate with neighbors.",
				"funding":"100.2M",
				"industries":["Privacy","Social Media"],
				"location":"San Francisco, California",
				"founders":["Nirav Tolia", "Prakash Janakiraman", "Sarah Leary"],
				"founded":"2010",
				"technologies":[{"name":"Javascript","lines": 1131},
								  {"name":"Python","lines": 5532},
								  {"name":"Java","lines": 1251}],						  						  
				"size":"100-500",
				"stargazers":1000,
				"twitter-id":"buzzfeed",
				"github-url":"http://github.com/nextdoor",						  
				"logo-url":"http://a3.images.crunchbase.com/image/upload/c_pad,h_98,w_98/v1397201003/b3d7d46bf95a047a2374723c2ebc8c0c.png"},

				{"organization":"Sift Science",
				"description":"Sift Science offers large-scale machine-learning technology services that help e-commerce businesses detect and fight fraud.",
				"funding":"23.6M",
				"industries":["Big Data", "Fraud Detection"],
				"location":"San Francisco, California",
				"founders":["Jonah Peretti","John Johnson"],
				"founded":"2008",
				"technologies":[{"name":"Python","lines": 3790},
								  {"name":"Go","lines": 125},
								  {"name":"Scala","lines": 1431}],						  						  
				"size":"10-50",
				"stargazers":1000,						  
				"github-url":"http://github.com/siftscience",						  
				"logo-url":"http://a5.images.crunchbase.com/image/upload/c_pad,h_98,w_98/v1397181705/929fa82cea7960b34c1a681e0d75279e.png"},

				{"organization":"Foursquare",
				"description":"Foursquare is a location-based social network where users receive points and virtual badges for 'checking in' at selected venues.",
				"funding":"162.4M",
				"industries":["Location Based Services", "Mobile"],
				"location":"New York, New York",
				"founders":["Naveen Selvadurai", "Dennis Crowley"],
				"founded":"2009",
				"technologies":[{"name":"Scala","lines": 14131},
								  {"name":"Python","lines": 6104},
								  {"name":"Perl","lines": 4251}],						  						  
				"size":"100-500",						  						  
				"crunchbase-url":"http://crunchbase.com/organization/foursquare",
				"logo-url":"http://a3.images.crunchbase.com/image/upload/c_pad,h_98,w_98/v1397751280/bab97d5ef0ed2d12e5257688cf56eb6a.png"}]


	companies_filtered_on_location = [company for company in companies if company['location'] in locations]
	technologies = [(company['organization'],company['technologies']) for company in companies_filtered_on_location]

	all_tech = []

	for (n,t) in technologies:

		technologies_names = [technology['name'] for technology in t]
		all_tech.append((n,technologies_names))

	tech_names = [tn[0] for tn in all_tech if intersect(tn[1],languages)]	
	companies_filtered_on_technology = [company for company in companies if company['organization'] in tech_names]	

	result = {"results": companies_filtered_on_technology} 

	return jsonify(result)

	
def intersect(a, b):
	return list(set(a) & set(b))

@app.route("/results", methods=['GET'])
def results():
	return redirect(url_for('index'))

#-----------------------------------
# launch
#-----------------------------------

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
