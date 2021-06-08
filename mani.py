import requests

common = []
obj = ['http://localhost:5003','http://localhost:5001','http://localhost:5002','https://www.google.com/']
for j,i in enumerate(obj):
    total =  {}
    try:
        data = requests.get(i)
        data = True
    except requests.ConnectionError:
        data = False
    total['id']=j+1
    total['name']=i
    total['status']=data
    common.append(total)

print (common)