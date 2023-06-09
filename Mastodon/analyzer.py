# INFORMATION ----------------------------------------------------------------------------------------
# 
# Authors: COMP90024 Team 54
# This file was created for Mastodon harvesting for COMP90024 Cloud and Cluster Computing Assignment 2
#
# ----------------------------------------------------------------------------------------------------

from textblob import TextBlob
import couchdb
import sys

remote_server = couchdb.Server(sys.argv[1])

count_neutral = 0
count_negative = 0
count_positive = 0

db = remote_server['mast']

# Toots inserted into couchdb are already preprocessed and are all relevant to scenario 
for doc in db.view('_all_docs', include_docs = True):
    toot_sentiment = TextBlob(doc.doc['content']).sentiment.polarity
    if -1< toot_sentiment < -0.1:
        count_negative += 1
    elif toot_sentiment >= -0.1 and toot_sentiment <= 0.1:
        count_neutral += 1
    else:
        count_positive += 1 

print("Positive count: ", count_positive)
print("Neutral count: ", count_neutral)
print("Negative count: ", count_negative)


################### CouchDB x Mastodon troubleshooting code below ###############################
# remote_server.resource.session.disable_ssl_verification()

# db = remote_server.create('test')

# doc = {'foo': 'bar'}
# print(db.save(doc))

# remote_server = couchdb.Server('http://'+host)
# remote_server.resource.session.disable_ssl_verification()
# remote_server.resource.credentials = (username, password)

# db = remote_server['test']

# doc = {'foo': 'bar'}
# # db.delete(doc)
# remote_server.delete('test')
