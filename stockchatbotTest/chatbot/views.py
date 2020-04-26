from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


def keyboard(request):

    return JsonResponse({
        'type': 'buttons',
        'buttons': ['주식검색', '주요공시', '특징주', '관심종목']
    })


@csrf_exempt
def answer(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '주식검색':
        search = "검색하고하는 종목 이름이나 번호를 입력해주십시오 :)"

        return JsonResponse({
            'message': {
                'text': search
            },
            # 키보드로 주식 입력받고, 금융감독원 오픈 API에서 주식가져오기
        })

    elif datacontent == '주요공시':
        news = "어제, 오늘 주요 공시입니다 :)"

        return JsonResponse({
            'message': {
                'text': news
            },
            # 공시라는 글자가 들어있는 어제 오늘 네이버 뉴스 검색통해 크롤링하기
        })

    elif datacontent == '특징주':
        SpecialStock = "어제, 오늘 특징주입니다 :)"

        return JsonResponse({
            'message': {
                'text': SpecialStock
            },
            # [특징주]라는 글자가 들어있는 어제 오늘 네이버 뉴스 검색통해 크롤링하기
        })
    elif datacontent == '관심종목':
        interestStock = "관심주 목록입니다 :)"

        return JsonResponse({
            'message': {
                'text': interestStock
            }, 'message': {
                'text': '삼성전자,\n'
            }, 'edit': {
                'type': 'buttons',
                'buttons': ['추가', '삭제']
            }
        })
