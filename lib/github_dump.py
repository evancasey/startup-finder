import urllib
import urllib2
import json
import pdb
import sys
import time
import csv

import tokens
from models import *

class GithubListener:

    def get_all_repos(self,org):

        url = "https://api.github.com/orgs/" + org + "/repos?client_id=" + tokens.GITHUB_ID + "&client_secret=" + tokens.GITHUB_SECRET        

        try:
            resource = urllib2.urlopen(url)             
            pages = json.loads(resource.read())
            return pages
        except:
            print("path not found")
            pass        

    def get_all_orgs_csv(self):

        orgs = []

        f = open('all_orgs.txt', 'rt')    
        reader = csv.reader(f)
        for row in reader:
            orgs += row            

        return orgs



if __name__ == "__main__":

    gl = GithubListener()
    orgs = gl.get_all_orgs_csv()

    counter = 0

    for org in orgs[100:]:

        repos = gl.get_all_repos(org)

        if repos:

            for repo in repos:

                print(json.dumps(repo,indent=2))
                counter +=1

                try:
                    github_data = Github(id = str(counter),
                                         organization = org,
                                         repos = json.dumps(repos))                                            
                    
                    Session.add(github_data)            
                    
                    print "Committing.."

                    Session.commit()

                except Exception, e:
                    print >> sys.stderr, 'Encountered Exception: ', e            
                    pass




        


       