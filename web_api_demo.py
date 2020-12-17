import requests
import json
import datetime
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status Code: {r.status_code}")
response_dict = r.json()
# with open("text_folder/web_api_data.json", 'w') as file:
# json.dump(r.json(), file)
print(response_dict.keys())
print(f"Total count: {response_dict['total_count']}")
print(f"Items size is {len(response_dict['items'])}")
print("Header of each item is :")
print(response_dict['items'][0].keys())

print("\r\n\r\n going to print each item details")

names, stars, labels, links = [], [], [], []
for item in response_dict['items']:
    # print(f"Name : {item['name']}")
    # print(f"Owner : {item['owner']['login']}")
    # print(f"Stars : {item['stargazers_count']}")
    # print(f"Respository : {item['html_url']}")
    # print(f"Created : {item['created_at']}")
    owner = item['owner']['login']
    names.append(item['name'])
    link = f"<a href='{item['html_url']}'>{item['name']}</a>"
    stars.append(item['stargazers_count'])
    labels.append(f"{owner}<br />{item['description']}")
    links.append(link)

# plotly
#data = [{'type': 'bar', 'x': names, 'y': stars,'hovertext':labels,'marker':{'color':'rgb(60,100,150)','line':{'width':1.5,'color':'rgb(25,25,25)'}},'opacity':0.6}]
data = [{'type': 'bar', 'x': links, 'y': stars,'hovertext':labels,'marker':{'color':'rgb(60,100,150)','line':{'width':1.5,'color':'rgb(25,25,25)'}},'opacity':0.6}]
my_layout = {'title': 'github favorite python project', 'xaxis': {'title': 'Repository'}, 'yaxis': {'title': 'starts'}}
fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='text_folder/python_fav.html')
