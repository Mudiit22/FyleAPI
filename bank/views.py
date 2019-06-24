from django.http import HttpResponse
from django.shortcuts import render
import psycopg2
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
@api_view(('GET',))
def details(requests,ifsc_code):
    connection = psycopg2.connect(user = "postgres",
                                  password = "Detergent#99",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "banks")
    cursor = connection.cursor()
    # print (connection.get_dsn_parameters(),"\n")
    # print(ifsc_code)
    # print("RESPONSE IS:", ifsc_code)
    cursor.execute("select * from branches where ifsc='{0}';".format(ifsc_code))
    bank_details=cursor.fetchall()
    return Response(status=200, data={"bank_details":bank_details})


@api_view(('GET',))
def branches(requests,city,bank):
    connection = psycopg2.connect(user = "postgres",
                                  password = "Detergent#99",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "banks")
    cursor = connection.cursor()
    cursor.execute("select * from branches where city='{0}' and bank_id in ( select id from banks where name='{1}');".format(city,bank))
    # print (connection.get_dsn_parameters(),"\n")
    # print(city,bank)
    branch_details_all=cursor.fetchall()
    return Response(status=200, data={"branches":branch_details_all})
