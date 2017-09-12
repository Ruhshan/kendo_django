# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import serializers, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *

class ClientPageNumberPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'pageSize'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ClientJsonView(generics.ListAPIView):
    serializer_class = ClientSerializer
    pagination_class = ClientPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        return Client.objects.all()


class ClientListView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "mainApp/client_list.html")
