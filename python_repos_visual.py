#make interactive bar chart to show the popularity of most starred python projects on github.
#page 366

import requests
from plotly.graph_objs import bar
from plotly import offline

#Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept':'application/vnd.github.v3+json'}
r = requests.get(url,headers=headers)
#print(f'status code is : {r.status_code}')

#store API response in a variable
response_dict = r.json()
repo_dicts = response_dict['items'] #repo_dicts is a list of dictionaries, where each dict has info about 1 python repository
repo_links, stars,labels = [],[],[]
for repo_dict in repo_dicts:
    #repo_names.append(repo_dict['name'])
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner'] ['login']
    description = repo_dict['description']
    label = f'{owner}<br />{description}'
    labels.append(label)

#make visualization
data = [{
    'type': 'bar',
    'x' : repo_links,
    #'x': repo_names,
    'y': stars, 
    'marker':{
        'color': 'rgb(60,100,150)',
        'line': {'width':1.5, 'color': 'rgb(25,25,25)'},

    } ,
    'hovertext':labels,
    'opacity': .6,

    }
]
my_layout = {
    'title': 'Most-starred python projects on GitHub' ,
    'titlefont': {'size':28 },
    'xaxis':{
        'title':'Repository',
        'titlefont': {'size':24},
        'tickfont':{'size':14},
     } ,
    'yaxis':{
        'title':'Stars',
        'titlefont': {'size':24},
        'tickfont':{'size':14},
        } ,
}

fig = {'data': data, 'layout':my_layout}
offline.plot (fig,filename = 'python_repos.html')

