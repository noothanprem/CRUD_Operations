from django.shortcuts import render
from django.http import HttpResponse
import csv
from rest_framework.generics import GenericAPIView

class CsvOperations(GenericAPIView):

    def get(self,request):
        with open('studentdetails.csv','r') as csv_file:
            #csv_content = csv.reader(csv_file)
            csv_content = csv.DictReader(csv_file)
            #data = list(csv_content)
            return HttpResponse(csv_content)


    def post(self,request):
        try:
            username = request.data['username']
            identifier = request.data['identifier']
            firstname = request.data['firstname']
            lastname = request.data['lastname']

            with open('studentdetails.csv','a',newline='') as csv_file:
                writer = csv.writer(csv_file,delimiter=',')
                writer.writerow([username,identifier,firstname,lastname])
                #fieldnames = ["Username","Identifier","First name","Last name"]
                #writer = csv.DictWriter(csv_file,fieldnames=fieldnames,delimiter=' ')
                #writer.writerow({"Username":username,"Identifier":identifier,"First name":firstname,"Last name":lastname})
                #writer.writerow({"Username":username,"Identifier":identifier,"First name":firstname,"Last name":lastname})
        except Exception as e:
            error_response = "Please check whether you have given all the fields or not"
            return HttpResponse(error_response,status=404)
        if username == "" or identifier == "" or firstname == "" or lastname == "":
            error_response = "Empty fields are not allowed"
            return HttpResponse(error_response,status=404)
        with open('studentdetails.csv','r') as csv_file:
            #csv_content = csv.reader(csv_file)
            csv_content = csv.DictReader(csv_file)
            #data = list(csv_content)
            return HttpResponse(csv_content)

class UpdateOperation(GenericAPIView):

    def put(self,request,username):

        user_details = []

        user_details.append(request.data['username'])
        user_details.append(request.data['identifier'])
        user_details.append(request.data['firstname'])
        user_details.append(request.data['lastname'])

        with open('studentdetails.csv','r') as csv_file:
            csv_content = csv.reader(csv_file)
            #csv_content = csv.DictReader(csv_file)
            data = list(csv_content)
            list_len = len(data)
            for i in range(list_len):
                if data[i][0] == username:
                    for j in range(len(data[i])):
                        data[i][j] = user_details[j]
                    break
            print(data)
            with open('studentdetails.csv','w+',newline='') as csv_file:
                writer = csv.writer(csv_file,delimiter=',')
                for i in data:
                    writer.writerow(i)
            return HttpResponse("updated successully")

    def delete(self,request,username):

        with open('studentdetails.csv','r') as csv_file:
            csv_content = csv.reader(csv_file)
            #csv_content = csv.DictReader(csv_file)
            data = list(csv_content)
            list_len = len(data)
            for i in range(list_len):
                if data[i][0] == username:
                    del data[i]
                    break
            with open('studentdetails.csv','w+',newline='') as csv_file:
                writer = csv.writer(csv_file,delimiter=',')
                for i in data:
                    writer.writerow(i)
        return HttpResponse("Deleted Successully")


