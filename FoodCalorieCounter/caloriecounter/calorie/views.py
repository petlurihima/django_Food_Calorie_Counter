from django.shortcuts import render
import requests
import json

# KWCteq0p9W2nDnT5s8yucg==0QTzu7br6NfyxA44

# Create your views here.
def main(request):
    if request.method =="POST":
        query=request.POST['query']
        api_url='https://api.calorieninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query,headers = {'X-Api-key':'KWCteq0p9W2nDnT5s8yucg==Gdl8J0mRs3Lwg8wK'})
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api="Oops! There was an error"
            print(e)
        return render(request,'main.html',{'api':api})
    else:
        return render(request,'main.html',{'query':'Enter valid query'})