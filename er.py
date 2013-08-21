from __future__ import division
from temboo.Library.Twitter.Users import Lookup
from temboo.Library.Facebook.Searching import FQL
from temboo.Library.Google.Plus.People import Get
from temboo.core.session import TembooSession
import urllib2 as urllib
import json
import re
import nltk
from unidecode import unidecode
from itertools import combinations,product
import datetime
import networkx as nx
from collections import defaultdict

stopwords = nltk.corpus.stopwords.words('english')

# Configuration
config = json.loads(open('config.json').read())

# Google CSE setup
APIkey = config['cse']['key']
userID = config['cse']['userID']
cseID = config['cse']['cseID']
query = unidecode(u'' + 'cedric warny').lower()
start = 1
num = 10

results = [] # To store Google CSE search results

# To store IDs/URLs grabbed from CSE search results
linkedinURLs = []
facebookIDs = []
twitterIDs = []
googleplusIDs = []

# All fields across all platforms to be fetched
all_fields = {'name','displayName','formattedName','username','profile_url','screen_name','publicProfileUrl','email','emails','emailAddress','current_location','location','currentLocation','placesLived','mainAddress','locale','education','organizations','educations','work','positions','lang','language','languages','about_me','description','aboutMe','tagline','summary','birthday_date','birthday','dateOfBirth','age_range','ageRange','sex','gender','timezone','time_zone','website','url','urls','memberUrlResources'}

session = TembooSession(config['temboo']['userID'], config['temboo']['app']['name'], config['temboo']['app']['key'])

def search(APIkey,userID,cseID,query,start):
    q = "https://www.googleapis.com/customsearch/v1?key=" + APIkey + "&cx=" + userID + ":" + cseID + "&q=" + urllib.quote(query,'') + "&start=" + str(start) + "&num=" + str(num) + "&alt=json"
    response = json.loads(urllib.urlopen(q).read())
    results.append(response)
    if response.get('queries'):
        totalResults = response.get('queries').get('request')[0].get('totalResults',0)
        if int(totalResults) > 100 and int(start) < 21:
            search(APIkey,userID,cseID,query,start+num)

def grabIDs():
    for r in results:
        for item in r.get('items',[]):
            if item.get('link'):
                if 'linkedin.com' in item.get('link') and item.get('pagemap',{}).get('person') and '/dir/' not in item.get('link') and '/directory/' not in item.get('link'):
                    if '?' in item.get('link'):
                        linkedinURLs.append(re.search('(.+)\?',item.get('link')).group(1))
                    else:
                        linkedinURLs.append(item.get('link'))
                elif 'twitter.com' in item.get('link','') and 'dev.twitter.com' not in item.get('link',''):
                    twitterIDs.append(re.search('/([\w.-]+)$',item.get('link','')).group(1))
                elif 'facebook.com' in item.get('link','') and item.get('pagemap',{}).get('person'):
                    facebookIDs.append(re.search('/([\w.-]+)$',item.get('link','')).group(1))
                elif 'plus.google.com' in item.get('link',''):
                    googleplusIDs.append(re.search('/([\w.-]+)$',item.get('link','')).group(1))

def getFacebookData():
    fQLChoreo = FQL(session)
    fQLInputs = fQLChoreo.new_input_set()
    fQLInputs.set_credential('facebook')
    conditions = ""
    for username in facebookIDs[:-1]:
        conditions += "username='" + username + "' OR "
    conditions+= "username='" + facebookIDs[-1] + "'"
    fQLInputs.set_Conditions(conditions)
    fQLInputs.set_Fields("uid,name,username,profile_url,email,current_location,locale,education,work,languages,about_me,birthday_date,age_range,sex,timezone,website,activities,books,friend_count")
    fQLInputs.set_Table("user")
    try:
        response = json.loads(fQLChoreo.execute_with_results(fQLInputs).get_Response()).get('data')
    except:
        response = []

    return response

def getTwitterData():
    lookupChoreo = Lookup(session)
    lookupInputs = lookupChoreo.new_input_set()
    lookupInputs.set_credential('twitter')
    lookupInputs.set_ScreenName(','.join(twitterIDs))
    lookupInputs.set_IncludeEntities("true")
    try:
        response = json.loads(lookupChoreo.execute_with_results(lookupInputs).get_Response())
    except:
        response = []
    
    return response

def getGooglePlusData():
    getChoreo = Get(session)
    getInputs = getChoreo.new_input_set()
    getInputs.set_credential('googleplus')
    #getInputs.set_Fields("id,displayName,emails,currentLocation,placesLived,organizations,language,aboutMe,tagline,birthday,ageRange,gender,urls")
    getResults = []
    for gplusid in googleplusIDs:
        getInputs.set_UserID(gplusid)
        try:
            response = json.loads(getChoreo.execute_with_results(getInputs).get_Response())
            getResults.append(response)
        except:
            pass

    return getResults

def getLinkedInData():
    access_token = config['linkedin']['accessToken']
    fields = "id,formatted-name,email-address,location,main-address,educations,positions,summary,date-of-birth,member-url-resources"
    linkedinResults = []
    for url in linkedinURLs:
        try:
            response = json.loads(urllib.urlopen("https://api.linkedin.com/v1/people/url=" + urllib.quote(url,'') + ":(" + fields + ")?&format=json&oauth2_access_token=" + access_token).read())
            linkedinResults.append(response)
        except:
            pass

    return linkedinResults

def shareOfFieldsAvailable(c):
    if c:
        n = 0.0
        fields_to_check = set(c.keys()).intersection(all_fields) # Only checking fields we are interested in
        if len(fields_to_check) > 0:
            for field in fields_to_check:
                if c.get(field):
                    n += 1.0
            return n/len(fields_to_check)
        else:
            return 0.0
    else:
        return 0.0

def prune(data):
    # Name check
    prune1 = {
                'facebook':[candidate for candidate in data['facebook'] if nltk.metrics.edit_distance(unidecode(candidate.get('name','')).lower(),query) < 2],
                'twitter':[candidate for candidate in data['twitter'] if nltk.metrics.edit_distance(unidecode(candidate.get('name','')).lower(),query) < 2],
                'googleplus':[candidate for candidate in data['googleplus'] if nltk.metrics.edit_distance(unidecode(candidate.get('displayName','')).lower(),query) < 2],
                'linkedin':[candidate for candidate in data['linkedin'] if nltk.metrics.edit_distance(unidecode(candidate.get('formattedName','')).lower(),query) < 2]
             }
    
    # Fields availability
    prune2 = {
                'facebook':[candidate for candidate in prune1['facebook'] if shareOfFieldsAvailable(candidate) > 0.3 and len(set(candidate.keys()).intersection(all_fields)) > 2],
                'twitter':[candidate for candidate in prune1['twitter'] if shareOfFieldsAvailable(candidate) > 0.3 and len(set(candidate.keys()).intersection(all_fields)) > 2],
                'googleplus':[candidate for candidate in prune1['googleplus'] if shareOfFieldsAvailable(candidate) > 0.3 and len(set(candidate.keys()).intersection(all_fields)) > 2],
                'linkedin':[candidate for candidate in prune1['linkedin'] if shareOfFieldsAvailable(candidate) > 0.3 and len(set(candidate.keys()).intersection(all_fields)) > 2]
             }
    
    return prune2

class Profile:
    def __init__(self,d):
        self.data = d

def standardize(data):
    data_standardized = {}
    
    candidates_standardized = []
    for candidate in data['facebook']:
        d = {}
        d['platform'] = 'facebook'
        d['name'] = candidate['name'].lower() if candidate.get('name') else None
        if candidate.get('username'):
            d['username'] = candidate['username'].lower()
        elif candidate.get('profile_url'):
            try:
                d['username'] = re.search('/([\w.-]+)$',candidate['profile_url']).group(1)
            except:
                d['username'] = None
        d['email'] = [candidate['email'].lower()] if candidate.get('email') else None
        d['location1'] = [candidate['current_location'].get('name').lower()] if candidate.get('current_location') else None
        d['location2'] = candidate['locale'].split('_')[1].lower() if candidate.get('locale') else None
        d['education'] = [org['name'].lower() for org in candidate['education'] if org.get('name')] if candidate.get('education') else None
        d['work'] = [org['employer']['name'].lower() for org in candidate.get('work',[]) if org.get('employer') and org['employer'].get('name')]
        d['language1'] = candidate['locale'].split('_')[0].lower() if candidate.get('locale') else None
        d['language2'] = candidate.get('languages')
        d['description'] = candidate['about_me'].lower() if candidate.get('about_me') else None
        if candidate.get('birthday_date'):
            try:
                d['birthday'] = datetime.datetime.strptime(candidate.get('birthday_date'),"%m/%d/%Y")
            except:
                d['birthday'] = datetime.datetime.strptime(candidate.get('birthday_date'),"%m/%d")
        else:
            None
        d['age'] = candidate['age_range'].get('min') if candidate.get('age_range') else None
        d['gender'] = candidate['sex'].lower() if candidate.get('sex') else None
        d['timezone'] = candidate.get('timezone')
        d['url'] = [candidate['website']] if candidate.get('website') else None
        
        candidates_standardized.append(Profile(d))
    
    data_standardized['facebook'] = candidates_standardized
    
    candidates_standardized = []
    for candidate in data['twitter']:
        d = {}
        d['platform'] = 'twitter'
        d['name'] = candidate['name'].lower() if candidate.get('name') else None
        d['username'] = candidate['screen_name'].lower() if candidate.get('screen_name') else None
        d['location1'] = [candidate['location']] if candidate.get('location') else None
        d['language1'] = candidate['lang'].lower() if candidate.get('lang') else None
        d['description'] = candidate['description'].lower() if candidate.get('description') else None
        d['timezone'] = candidate.get('time_zone')
        d['url'] = [candidate['url']] if candidate.get('url') else None
        
        candidates_standardized.append(Profile(d))

    data_standardized['twitter'] = candidates_standardized
    
    candidates_standardized = []
    for candidate in data['googleplus']:
        d = {}
        d['platform'] = 'googleplus'
        d['name'] = candidate['displayName'].lower() if candidate.get('displayName') else None
        d['email'] = candidate.get('emails')
        if candidate.get('currentLocation'):
            if candidate.get('placesLived'):
                d['location1'] = [candidate['currentLocation'].lower()] + [place.get('value').lower() for place in candidate['placesLived']]
            else:
                d['location1'] = [candidate['currentLocation'].lower()]
        else:
            if candidate.get('placesLived'):
                d['location1'] = [place.get('value').lower() for place in candidate['placesLived']]
            else:
                d['location1'] = None
        d['education'] = [org['name'].lower() for org in candidate['organizations'] if org.get('type') == 'school' and org.get('name')] if candidate.get('organizations') else None
        d['work'] = [org['name'].lower() for org in candidate['organizations'] if org.get('type') == 'work' and org.get('name')] if candidate.get('organizations') else None
        d['language1'] = candidate['language'].lower() if candidate.get('language') else None
        d['language2'] = [candidate['language'].lower()] if candidate.get('language') else None
        if candidate.get('aboutMe'):
            if candidate.get('tagline'):
                d['description'] = candidate['aboutMe'].lower() + ' ' + candidate['tagline'].lower()
            else:
                d['description'] = candidate['aboutMe'].lower()
        else:
            if candidate.get('tagline'):
                d['description'] = candidate['tagline'].lower()
            else:
                d['description'] = ''
        d['birthday'] = datetime.datetime.strptime(candidate.get('birthday'),"%Y-%m-%d") if candidate.get('birthday') else None
        d['age'] = candidate['ageRange'].get('min') if candidate.get('ageRange') else None
        d['gender'] = candidate['gender'].lower() if candidate.get('gender') else None
        d['urls'] = [url['value'] for url in candidate['urls'] if url.get('value')] if candidate.get('urls') else None

        candidates_standardized.append(Profile(d))

    data_standardized['googleplus'] = candidates_standardized
    
    candidates_standardized = []
    for candidate in data['linkedin']:
        d = {}
        d['platform'] = 'linkedin'
        d['name'] = candidate.get('formattedName','').lower()
        d['username'] = re.search('/([\w.-]+)$',candidate['publicProfileUrl']).group(1) if candidate.get('publicProfileUrl') else None
        d['email'] = [candidate['emailAddress'].lower()] if candidate.get('emailAddress') else None
        d['location1'] = [candidate['location']['name'].lower()] if candidate.get('location') and candidate['location'].get('name') else None
        d['location2'] = candidate['location']['country']['code'].lower() if candidate.get('location') and candidate['location'].get('country') and candidate['location']['country'].get('code') else None
        d['education'] = [school['schoolName'].lower() for school in candidate['educations']['values'] if school.get('schoolName')] if candidate.get('educations') and candidate['educations'].get('values') else None
        d['work'] = [position['company']['name'].lower() for position in candidate['positions']['values'] if position.get('company') and position.get('company',{}).get('name')] if candidate.get('positions') and candidate['positions'].get('values') else None
        d['description'] = candidate['summary'].lower() if candidate.get('summary') else None
        if candidate.get('dateOfBirth') and candidate['dateOfBirth'].get('year'):
            if candidate['dateOfBirth'].get('month'):
                if candidate['dateOfBirth'].get('day'):
                    d['birthday'] = datetime.date(candidate['dateOfBirth']['year'],candidate['dateOfBirth']['month'],candidate['dateOfBirth']['day'])
                else:
                    d['birthday'] = datetime.date(candidate['dateOfBirth']['year'],candidate['dateOfBirth']['month'],1)
            else:
                d['birthday'] = datetime.date(candidate['dateOfBirth']['year'],1,1)
        else:
            d['birthday'] = None
        d['urls'] = [url['url'] for url in candidate.get('memberUrlResources',{}).get('values',[]) if url.get('url')] if candidate.get('memberUrlResources') and candidate['memberUrlResources'].get('values') else None

        candidates_standardized.append(Profile(d))
    
    data_standardized['linkedin'] = candidates_standardized

    return data_standardized

def string_similarity(s1,s2):
    # Measure between 0 and 1, 1 being perfectly equal strings
    return (1.0 - float(nltk.metrics.edit_distance(s1,s2))/ (float(sum([len(s1),len(s2)])) / 2)) if s1 != '' and s2 != '' else 0.0

def lexical_similarity(s1,s2):
    lexicon1 = set(nltk.word_tokenize(s1)).difference(stopwords)
    lexicon2 = set(nltk.word_tokenize(s2)).difference(stopwords)
    return float(len(lexicon1.intersection(lexicon2))) / (float(sum([len(lexicon1),len(lexicon2)])) / 2)

def score(d):
    G=nx.Graph()
    # Loop through all possible pairwise combination of platforms
    for platform1,platform2 in combinations(d.values(),2):
        # For each pair of platform, loop through the Cartesian product of candidates from each platform, make a match test and adjust the score in function of test results
        for candidate1,candidate2 in product(platform1,platform2):
            score = 0
            c1 = candidate1.data
            c2 = candidate2.data
            if c1.get('name') and c2.get('name'):
                if string_similarity(c1['name'],c2['name']) > 0.8:
                    score += 1
                else:
                    score -= 10
                    
            if c1.get('username') and c2.get('username') and string_similarity(c1['username'],c2['username']) > 0.7:
                score += 1
                    
            if c1.get('email') and c2.get('email'):
                for email1,email2 in product(c1['email'],c2['email']):
                    if email1 == email2:
                        score += 8
                        
            if c1.get('location1') and c2.get('location1'):
                matches = 0
                for loc1,loc2 in product(c1['location1'],c2['location1']):
                    loc1 = set(re.findall(r"[\w']+", loc1))
                    loc2 = set(re.findall(r"[\w']+", loc2))
                    if loc1.intersection(loc2): # If there's any word common to both locations, then it's a match
                        matches += 1
                if matches > 0:
                    score += 2
                else:
                    score -= 1
                    
            if c1.get('location2') and c2.get('location2'):
                if c1['location2'] == c2['location2']:
                    score += 1
                else:
                    score -= 5
            
            if c1.get('education') and c2.get('education'):
                matches = 0
                for edu1,edu2 in product(c1['education'],c2['education']):
                    if string_similarity(edu1,edu2) > 0.7:
                        matches += 1
                if matches > 0:
                    score += 2
                else:
                    score -= 1
                                    
            if c1.get('work') and c2.get('work'):
                matches = 0
                for work1,work2 in product(c1['work'],c2['work']):
                    if string_similarity(work1,work2) > 0.7:
                        matches += 1
                if matches > 0:
                    score += 2
                else:
                    score -= 1
                        
            if c1.get('language1') and c2.get('language1'):
                if c1['language1'] == c2['language1']:
                    score += 1
                else:
                    score -= 2
                    
            if c1.get('language2') and c2.get('language2'):
                matches = 0
                for lang1,lang2 in product(c1['language2'],c2['language2']):
                    if string_similarity(lang1,lang2) > 0.7:
                        matches += 1
                if matches > 0:
                    score += 2
                    
            if c1.get('description') and c2.get('description') and lexical_similarity(c1['description'],c2['description']) > 0.5:
                score += 1
                    
            if c1.get('birthday') and c2.get('birthday'):
                if c1['birthday'].year == c2['birthday'].year and c1['birthday'].year != 1900:
                    score += 4
                if c1['birthday'].month == c2['birthday'].month:
                    score += 2
                    
            if c1.get('age') and c2.get('age') and c1['age'] == c2['age']:
                score += 1
                    
            if c1.get('gender') and c2.get('gender') and c1['gender'] != c2['gender']:
                score -= 10
                    
            if c1.get('timezone') and c2.get('timezone') and c1['timezone'] == c2['timezone']:
                score += 1
                    
            if c1.get('url') and c2.get('url'):
                matches = 0
                for url1,url2 in product(c1['url'],c2['url']):
                    if string_similarity(url1,url2) > 0.8:
                        matches += 1
                if matches > 0:
                    score += 5
                else:
                    score -= 0.5
            
            field_overlap = len([field for field in set(c1.keys()).intersection(set(c1.keys())) if c1.get(field) and c2.get(field)])
            
            if score > 0:
                G.add_edge(candidate1,candidate2,score=score,field_overlap=field_overlap)

    return G

def find_shortest_paths(g):
    shortest_paths = []
    for s in [nx.all_shortest_paths(g,n1,n2) for n1,n2 in combinations(g.nodes(),2) if nx.has_path(g,n1,n2)]:
        shortest_paths += [p for p in s]
    return shortest_paths

def paste_paths(paths):
    a = 0
    for p1,p2 in combinations(paths,2):
        if p1[-1] == p2[0] and p1[:-1] + p2 not in paths and set(p1[:-1]).isdisjoint(set(p2)):
            a += 1
            paths += [p1[:-1] + p2]
    return paths if a == 0 else paste_paths(paths)

def regularize(paths):
    edges_to_remove = []
    for p in paths:
        for pf in ['facebook','linkedin','twitter','googleplus']:
            indices = [k for k,n in enumerate(p) if n.data['platform'] == pf]
            if len(indices) > 1:
                for i in range(len(indices)-1):
                    subpath = p[indices[i]:indices[i+1]+1]
                    subG = G.subgraph(subpath)
                    score,edge = min([(subG[e[0]][e[1]]['score'],e) for e in subG.edges()])
                    edges_to_remove.append(edge)
    
    for edge in set(map(frozenset,edges_to_remove)):
        G.remove_edge(*tuple(edge))

class Entity:
    def __init__(self,list):
        self.list = list
        
def rankEntities(paths):
    entities = defaultdict(dict)
    for p in paths:
        e = Entity(p)
        entities[e]['avg_score'] = sum([G[node1][node2]['score'] for node1,node2 in combinations(p,2) if (node1,node2) in G.edges()]) / len(p)
        entities[e]['avg_field_overlap'] = sum([G[node1][node2]['field_overlap'] for node1,node2 in combinations(p,2) if (node1,node2) in G.edges()]) / len(p)

    return sorted(entities.iteritems(), key=lambda (k,v): v['avg_score'], reverse=True)

# 1. Google Search on the target Online Social Networks
search(APIkey,userID,cseID,query,start)
grabIDs()

# 2. Get the data by querying the APIs based on the IDs collected from the Google Search
data = {'facebook':getFacebookData() if facebookIDs else [],'twitter':getTwitterData() if twitterIDs else [],'googleplus':getGooglePlusData() if googleplusIDs else [],'linkedin':getLinkedInData() if linkedinURLs else []}

# 3. Prune the data by making a sanity check comparing the results with the initial query and by dropping candidates with very low information
data_pruned = prune(data)

# 4. Standardize the data fields across platforms
data_standardized = standardize(data_pruned)

# 5. Score the link potential of all possible combinations of candidates
G = score(data_standardized)

# 6. Candidate resolved entities are paths in the resultant graph. However, paths can't go twice through the same platform. Cut edges in order to regularize these paths
regularize(paste_paths(find_shortest_paths(G)))

# 7. Output all paths in the graph. These are the candidate resolved entities
paths = paste_paths(find_shortest_paths(G))

# 8. Rank the candidate entities by calculating the average score and field overlap of the path
ranked_entities = rankEntities(paths)

nx.draw(G)
for i in range(min(3,len(ranked_entities))):
    print "Rank " + str(i) + ": "
    print "\tAverage score: ", ranked_entities[i][1]['avg_score']
    print "\tData: "
    for profile in ranked_entities[i][0].list:
        print "\t\t", profile.data
    print "\n"
    print "*********************************************************"
    print "\n"
