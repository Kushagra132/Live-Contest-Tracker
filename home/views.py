from django.shortcuts import render
import requests
import json
# Create your views here.
def index(request):
    url = "https://www.kontests.net/api/v1/all"
    response = requests.get(url)
    js = json.loads(response.text)
    print(json.dumps(js))
    l1=[]
    l2=[]
    for contest in js:
        d=dict()
        d['name']=contest['name']
        d['link']=contest['url']
        if('site' in contest):
            d['site']=contest['site']
        else:
            d['site']="Not Available"

        if(contest['start_time']!='-'):
            d['start_date']=contest['start_time'][0:11]
            d['start_time']=contest['start_time'][11:19]
        else:
            d['start_date']="Not Available"
            d['start_time']="Not Available"
        if(contest['end_time']!='-'):
            d['end_date']=contest['end_time'][0:11]
            d['end_time']=contest['end_time'][11:19]
        else:
            d['end_date']="Not Available"
            d['end_time']="Not Available"
        
        if(contest['status']=='CODING'):
            l1.append(d)
        else:
            l2.append(d)

        context={'running':l1 ,'future':l2}
    return render(request,'index.html',context)

        
def about(request):
    return render(request,'about.html')
    
