from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.generics import GenericAPIView

class JsonOperations(GenericAPIView):
    def get(self,request):
        with open('EmployeeData.json','r') as json_file:
            data = json.load(json_file)
            return HttpResponse(data)

    def post(self,request):
        id = request.data['id']
        name = request.data['name']
        email = request.data['email']
        password = request.data['password']
        request_dict = {"id":id,"name":name,"email":email,"password":password}
        with open('EmployeeData.json') as json_file:
            data = json.load(json_file)
            data.append(request_dict)

            with open('EmployeeData.json','w') as f:
                json.dump(data,f,indent=4)

            return HttpResponse("Added Successfully")

class JsonUpdate(GenericAPIView):
    def put(self,request,id):
        name = request.data['name']
        email = request.data['email']
        password = request.data['password']
        with open('EmployeeData.json') as json_file:
            data = json.load(json_file)
            for i in range(len(data)):
                if str(data[i]['id']) == id:
                    data[i]['name'] = name
                    data[i]['email']=email
                    data[i]['password']=password
                    break
            print(data)

            with open("EmployeeData.json",'w') as f :
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