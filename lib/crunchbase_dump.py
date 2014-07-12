import urllib
import urllib2
import json
import pdb
import sys
import time
import csv

import tokens
from models import *

class CrunchBaseListener:

    def __init__(self):
        self.global_counter = 0
        self.token = tokens.CRUNCHBASE_TOKEN_1

    def get_all_orgs(self):

        if self.global_counter == 50:
            if self.token == tokens.CRUNCHBASE_TOKEN_1:
                self.token = tokens.CRUNCHBASE_TOKEN_2
            elif self.token == tokens.CRUNCHBASE_TOKEN_2:
                self.token = tokens.CRUNCHBASE_TOKEN_3
            elif self.token == tokens.CRUNCHBASE_TOKEN_3:
                self.token = tokens.CRUNCHBASE_TOKEN_4
            else:
                self.token = tokens.CRUNCHBASE_TOKEN_1            
            self.global_counter = 0

        orgs = []
        for page_num in xrange(268):

            print("pagenum: " + str(page_num))

            url = "http://api.crunchbase.com/v/2/organizations?user_key=" + self.token + "&page=" + str(page_num) + "&order=created_at+DESC"
            resource = urllib2.urlopen(url)
            pages = json.loads(resource.read())
            self.global_counter += 1

            for org in pages['data']['items'][1:]:
                try:                
                    orgs.append(org.get('path',None))
                except ValueError:
                    println("path not found")
                    pass

        return orgs

    def get_all_orgs_csv(self):

        orgs = []

        f = open('orgs.txt', 'rt')    
        reader = csv.reader(f)
        for row in reader:
            orgs += row            

        return orgs

    def get_org_details(self,org_path):

        if self.global_counter == 50:
            if self.token == tokens.CRUNCHBASE_TOKEN_1:
                self.token = tokens.CRUNCHBASE_TOKEN_2
            elif self.token == tokens.CRUNCHBASE_TOKEN_2:
                self.token = tokens.CRUNCHBASE_TOKEN_3
            elif self.token == tokens.CRUNCHBASE_TOKEN_3:
                self.token = tokens.CRUNCHBASE_TOKEN_4
            else:
                self.token = tokens.CRUNCHBASE_TOKEN_1            
            self.global_counter = 0

        url = "http://api.crunchbase.com/v/2" + org_path + "?user_key=" + self.token
        resource = urllib2.urlopen(url)
        org_details = json.loads(resource.read())
        self.global_counter += 1

        return org_details['data']

    def is_valid(self, org_with_details):

        if org_with_details['properties'].get('is_closed', None) == True: 
            return False
        elif not org_with_details['properties'].get('total_funding_usd', None):
            return False
        elif org_with_details['properties']['total_funding_usd'] == 0:
            return False
        elif not org_with_details['relationships'].get('primary_image', None):
            return False

        return True


if __name__ == "__main__":

    cb = CrunchBaseListener()

    org_paths = cb.get_all_orgs_csv()

    for org in org_paths:

        print(cb.global_counter)

        print("org: " + org)        

        org_with_details = cb.get_org_details(org)

        if cb.is_valid(org_with_details):

            print(json.dumps(org_with_details,indent=2))

            try:
                crunchbase_data = CrunchBase(id = org_with_details['uuid'],
                                             name = org_with_details['properties']['name'],
                                             description = org_with_details['properties'].get('short_description', ""),
                                             founded_on = org_with_details['properties'].get('founded_on', ""),
                                             total_funding = org_with_details['properties'].get('total_funding_usd',   ""),
                                             homepage_url = org_with_details['properties'].get('homepage_url', ""),
                                             founders = json.dumps(org_with_details['relationships'].get('founders',   "")),
                                             categories = json.dumps(org_with_details['relationships'].get('categories',   "")),
                                             logo_path = "http://crunchbase.com/" + org_with_details['relationships']['primary_image']['items'][0]['path'],
                                             websites = json.dumps(org_with_details['relationships'].get('websites',   "")),
                                             headquarters = json.dumps(org_with_details['relationships'].get('headquarters',   "")),
                                             news = json.dumps(org_with_details['relationships'].get('news',   "")))                                             
                
                Session.add(crunchbase_data)            
                
                print "Committing.."

                Session.commit()

            except Exception, e:
                print >> sys.stderr, 'Encountered Exception: ', e            
                pass




        

