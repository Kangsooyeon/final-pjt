from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.conf import settings
import requests
from .serializer import *
from .models import *

import pandas as pd
import requests
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from PIL import Image

font_path = 'C:/Windows/Fonts/malgunbd.ttf'
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# Create your views here.

API_KEY='kHJV65CK0uTFRVoV0cdQ5xNGhnHZ742f'
BASE_URL='https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'

@api_view(['GET'])
def index(request):
    URL = BASE_URL
    params = {
        'authkey' : API_KEY,
        'data': 'AP01',
    }
    response = requests.get(URL, params=params).json()
    return Response(response)

@api_view(['GET'])
def save_ER(request):
    URL = BASE_URL
    params = {
        'authkey' : API_KEY,
        'data': 'AP01',
    }
    response = requests.get(URL, params=params).json()

    for er in response:
        cur_unit=er.get('cur_unit')
        #쉼표 제거하여 float형으로 변환
        ttb = float(er.get('ttb').replace(',', '')) if er.get('ttb') else None
        tts = float(er.get('tts').replace(',', '')) if er.get('tts') else None
        cur_nm=er.get('cur_nm')

        save_data={
            'cur_unit':cur_unit,
            'ttb':ttb,
            'tts':tts,
            'cur_nm':cur_nm,
        }

        serializer=ExchangeRateSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    return JsonResponse({'message':'저장완료'})


@api_view(['GET'])
def ER_graph(request):
    codes = ['0000001', '0000002', '0000003', '0000053']
    countries = ['미국 USD', '일본 JPY', '유럽 EUR', '중국 CNY' ]
    names = ['USD', 'JPY', 'EUR', 'CNY']
 
    API_KEY='HSYHTREWFIJQ9TKHK8ES'

    for c in range(len(codes)):
        url='https://ecos.bok.or.kr/api/StatisticSearch/'+API_KEY+'/json/kr/1/100/731Y001/D/20240101/20240516/'+codes[c]+'/'

        response = requests.get(url)
        result = response.json()

        list_total_count=int(result['StatisticSearch']['list_total_count'])
        list_count=int(list_total_count/100) + 1

        rows=[]
        for i in range(0,list_count):
            start = str(i * 100 + 1)
            end = str((i + 1) * 100)
            url='https://ecos.bok.or.kr/api/StatisticSearch/'+API_KEY+'/json/kr/'+ start +'/'+ end +'/731Y001/D/20240101/20240501/'+codes[c]+'/'
            response = requests.get(url)
            result = response.json()
            rows = rows + result['StatisticSearch']['row']
            
        dfwon=pd.DataFrame(rows)

        dfwon['datetime']=pd.to_datetime(dfwon['TIME'].str[:4] + '-' + \
                        dfwon['TIME'].str[4:6] + '-' + dfwon['TIME'].str[6:8])
        dfwon=dfwon.astype({'DATA_VALUE':'float'})

        plt.figure(figsize=(6, 6))
        plt.plot(dfwon['datetime'], dfwon['DATA_VALUE'], color='limegreen', alpha=0.5)
        plt.fill_between(dfwon['datetime'], dfwon['DATA_VALUE'], color='limegreen', alpha=0.1)
        plt.ylim(min(dfwon['DATA_VALUE'])*0.99, max(dfwon['DATA_VALUE'])*1.03)
        plt.xticks(dfwon['datetime'][::len(dfwon)//3])

        plt.gca().spines['bottom'].set_alpha(0)  
        plt.gca().spines['top'].set_alpha(0)
        plt.gca().spines['left'].set_alpha(0)
        plt.gca().spines['right'].set_alpha(0)

        plt.xticks(alpha=0)
        plt.yticks(alpha=0)

        plt.gca().tick_params(axis='x', colors='white')
        plt.gca().tick_params(axis='y', colors='white')


        final_1 = dfwon['DATA_VALUE'].iloc[-1]
        final_2 = dfwon['DATA_VALUE'].iloc[-2]
        diff = abs(final_1 - final_2)

        plt.text(70, 400, countries[c], fontsize=20, transform=None)
        plt.text(70, 360, final_1, fontweight='bold', fontsize=18, transform=None)

        if final_1 > final_2:
                plt.text(70, 320, '▲ '+ str(round(diff,2))+ ' ('+ str(round(diff/final_1*100,2))+'%)', fontsize=12, transform=None, color='red')
        else:
                plt.text(70, 320, '▼ '+ str(round(diff,2))+ ' (-'+ str(round(diff/final_1*100,2))+'%)', fontsize=12, transform=None, color='blue')


        save_path = settings.STATICFILES_DIRS[0] / 'ER-graph' / (names[c] + '.png')
        plt.savefig(save_path, format='png', bbox_inches='tight')

    return JsonResponse({'message':'그래프 저장 완료'})