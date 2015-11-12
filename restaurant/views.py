from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from restaurant.models import Restaurant
from restaurant.serializer import RestaurantSerializer
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


class TestJava(APIView):
    serializer_class = RestaurantSerializer

    def get(self, request):
        # self.compile_java('java/rule/HelloWorld.java')
        a = self.execute_java('java/rule/test.jar', '')
        return Response(a)

    def compile_java(self, java_file):
        subprocess.check_call(['javac', java_file])

    def execute_java(self, java_file, stdin):
        java_class, ext = os.path.splitext(java_file)
        cmd = ['java', '-jar', java_file]
        print cmd
        proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        stdout, stderr = proc.communicate(stdin)
        print ('This was "' + stdout + '"')
        return stdout
