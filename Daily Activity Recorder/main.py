import requests
import datetime as dt

USERNAME = "shubhrima"
URL= "https://pixe.la/v1/users"
TOKEN = " "
GRAPH_ID = "graph1"
PARAMETER={
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
response = requests.post(url=URL, json=PARAMETER)
#print(response.text)

graph_params ={
    "id" : GRAPH_ID,
    "name" : "Skipping Progress",
    "unit" : "commit",
    "type" : "int",
    "color" : "sora",
}


headers = { "X-USER-TOKEN" : TOKEN}         #api headers, keep api a secret
graph =requests.post(url=f"{URL}/{USERNAME}/graphs", json=graph_params, headers=headers)

#TODAY =str(dt.datetime.now()).split(' ')[0].replace('-','')
TODAY= dt.datetime.now().strftime("%Y%m%d")

data_params ={
    "date": TODAY,
    "quantity":"5",
}
graph_data = requests.post(url=f"{URL}/{USERNAME}/graphs/{GRAPH_ID}", json= data_params, headers=headers)
print(graph_data)
