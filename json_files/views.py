from urllib.request import urlopen

from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib
from rest_framework.generics import GenericAPIView

class JsonOperations(GenericAPIView):
    def get(self,request):

        with open('EmployeeData.json','r') as json_file:
            data = json.load(json_file)
            return HttpResponse(data)

    def post(self,request):
        #postId = request.data['postId']
        #name = request.data['name']
        #email = request.data['email']
        #body = request.data['body']
        url = "https://jsonplaceholder.typicode.com/posts/1/comments"
        json_url = urlopen(url)
        data = json.loads(json_url.read())
        print(data)
        #request_dict = {"postId":id,"name":name,"email":email,"body":body}

        #with open('EmployeeData.json') as json_file:
            #data = json.load(json_file)
            #data.append(request_dict)

        with open('EmployeeData.json','w') as f:
            json.dump(data,f,indent=4)

        return HttpResponse("Added Successfully")

class JsonUpdate(GenericAPIView):
    def put(self,request,id):

        name = request.data['name']
        email = request.data['email']
        body = request.data['body']

        with open('EmployeeData.json') as json_file:
            data = json.load(json_file)
            for i in range(len(data)):
                if str(data[i]['id']) == id:
                    data[i]['name'] = name
                    data[i]['email']=email
                    data[i]['body']=body
                    break
            print(data)

            with open("EmployeeData.json",'w+') as f :
                json.dump(data,f)

        return HttpResponse("Updated Successfully")


    def delete(self,request,id):
        with open('EmployeeData.json') as json_file:
            data = json.load(json_file)
            for i in range(len(data)):
                if str(data[i]['id']) == id:
                    del data[i]
                    break
            print(data)

            with open("EmployeeData.json",'w') as f :
                json.dump(data,f)

        return HttpResponse("Deleted Successfully")