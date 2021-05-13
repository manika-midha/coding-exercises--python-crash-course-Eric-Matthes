#print a summary of top 30 articles from hacker news website

from operator import itemgetter
import requests 

#make an API call and store response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
#print(f'status code : {r.status_code}')

#process information about each submission
submission_ids = r.json() #list of ids of all articles
submission_dicts = [] #list of dictionaries, where 1 dic is for individual article
for submission_id in submission_ids [:10] : #take top 30 articles
    #make a separate call for each API
    #print({submission_id})
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r=requests.get(url)
    #print(f'id:{submission_id} status:{r.status_code}')
    response_dict = r.json()
    
    #build a dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link':f"https://news.ycombinator.com/item?id={submission_id}" ,
       'comments': response_dict['score'],
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts,key=itemgetter('comments'),reverse=True) #sort by score

for submission_dict in submission_dicts [:30] :
    print(f"\ntitle : {submission_dict['title']}")
    print(f"link : {submission_dict['hn_link']}")
    print(f"comments : {submission_dict['comments']}")