from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from restaurant.models import Restaurant
from rest_framework import serializers
from restaurant.serializer import RestaurantSerializer
from restaurant.serializer import RequestSerializer
import os.path, subprocess
from subprocess import STDOUT, PIPE


class RestaurantViewList(APIView):
    serializer_class = RestaurantSerializer

    def get(self, request):
        restaurant = Restaurant.objects.all()
        response = self.serializer_class(restaurant, many=True)
        return Response(response.data)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetRestaurant(APIView):
    # serializer_class = RequestSerializer

    def post(self, request):
        serializer_class = RestaurantSerializer
        user_input = request.data['res_type'] + ',' + request.data['price'] + ',' + request.data['user_x'] + ',' + request.data['user_y']
        # print user_input
        a = self.execute_java('rule.jar', user_input)
        # a = "INFO: Rule 'Vote rule' has been evaluated to false, it has not been executed.\n|-result-| = 0,"
        if a.find("|-result-| = ") == -1:
            return Response("Rule is broken", status=status.HTTP_200_OK)
        a = a.split("|-result-| = ")
        a = a[1].split(",")
        a.pop()
        if len(a) < 2:
            return Response("No restaurant is suitable now", status=status.HTTP_200_OK)
        restaurant = Restaurant.objects.filter(id__in=a)
        response = serializer_class(restaurant, many=True)
        return Response(response.data)


    def execute_java(self, java_file, stdin):
        java_class, ext = os.path.splitext(java_file)
        cmd = ['java', '-jar', java_file]
        print cmd
        proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        stdout, stderr = proc.communicate(stdin)
        print ('This was "' + stdout + '"')
        return stdout
