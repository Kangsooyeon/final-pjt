from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import requests
from .serializer import *
from .models import *
from django.db.models import Max
# Create your views here.

API_KEY='b485257240fd200014c237dd7e0b6479'
BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

@api_view(['GET'])
def index(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth' : API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()
    return JsonResponse(response)

@api_view(['GET'])
def save_deposit_products(reqeust):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth' : API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()

    baseList=response.get('result').get('baseList')
    optionList=response.get('result').get('optionList')

    for li in baseList:
        fin_prdt_cd = li.get('fin_prdt_cd')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = li.get('join_deny')
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spcl_cnd = li.get('spcl_cnd')

        save_data = {
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd,
        }

        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save() 

    for li in optionList:
        fin_prdt_cd=li.get('fin_prdt_cd')
        intr_rate_type_nm=li.get('intr_rate_type_nm')
        intr_rate=li.get('intr_rate')
        intr_rate2=li.get('intr_rate2')
        save_trm=li.get('save_trm')

        product_instance = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)

        save_data = {
            'product': product_instance.pk,
            'fin_prdt_cd' : fin_prdt_cd,
            'intr_rate_type_nm' : intr_rate_type_nm,
            'intr_rate' : intr_rate,
            'intr_rate2' : intr_rate2,
            'save_trm' : save_trm,
        }

        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse({'message':'저장완료'})


@api_view(['GET'])
def deposit_products(reqeust):
    depositProducts=DepositProducts.objects.all()
    serializer = DepositProductsSerializer(depositProducts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deposit_product(reqeust, id):
    depositProducts=DepositProducts.objects.filter(id=id)
    serializer = DepositProductsSerializer(depositProducts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deposit_product_options(reqeust, fin_prdt_cd):
    depositOption=DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(depositOption, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def top_rate(reqeust):
    max_intr_rates = DepositOptions.objects.order_by('-intr_rate2')[:5]

    top_rate_data = []
    for option in max_intr_rates:
        product_detail = DepositProducts.objects.get(fin_prdt_cd=option.fin_prdt_cd)
        product_serializer = DepositProductsSerializer(product_detail)
        option_serializer = DepositOptionsSerializer(option)
        top_rate_data.append({
            'deposit_product': product_serializer.data,
            'option': option_serializer.data
        })

    return Response(top_rate_data)