from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
#1# from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie



class MpesaDetail(APIView):
    #1# @csrf_exempt 
    @ensure_csrf_cookie
    def test_send_stk_push(self):
        response = self.client.post(
            path='http://127.0.0.1:8000/mpesa/request-stk-push/',
            data={
                'account_number': '174379', # replace with the account number that is to receive funds
                'amount': '1',
                'phone_number': '797292290', # replace with user phone number. Notice that '+254' is not included. It is hardcoded in the app
                'description': 'Testing my mpesa', # replace with adequate description
            }
        )
        data = response.json()
        self.assertEqual(data['ResponseCode'], "0")
        self.assertEqual(data['ResponseDescription'], "Success. Request accepted for processing")
        self.assertEqual(data['CustomerMessage'], "Success. Request accepted for processing")