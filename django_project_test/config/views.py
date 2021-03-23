# 뷰 : 기능을 담당(페이지 단위)
# 화면이 나타나는 뷰, 화면이 없는 뷰 ==> 사용자가 뷰를 볼 수 있느냐 없느냐
# 주소 URL은 무조건 있어야 함

# 뷰 내용(함수, 클래스), URL이 있으면 동작함.

# 뷰의 코드 형식 : 함수형, 클래스형
# 함수형 : request를 매개변수로 받고(추가 매개변수 가능), 모양은 함수
#   내가 원하는대로 동작들을 설계하고 만들고 싶을 때
# 클래스형 : CRUD 같은 기존에 많이 사용하는 기능을 미리 클래스로 만들어두고 상속받아 사용
#   장고에서 미리 만들어놓은 클래스형 뷰 ==> 제네릭 뷰
#   제네릭 뷰를 많이 사용함

from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # request에는 사용자가 웹브라우져를 통해 요청한 정보들이 들어가있음.
    # 어떤 계산이나, 데이터베이스 조회, 수정, 등록
    # 응답 메시지를 만들어 반환
    # html 변수를 대신해서 템플릿을 사용함.
    html = "<html><body>Hello</body></html>"
    return HttpResponse(html)


# 뷰의 이름은 : welcome
# 뷰의 접속 주소 : welcome/
# 내용은 : Welcome to Django.
def welcome(request):
    html = "<html><body>Welcome to Django</body></html>"
    return HttpResponse(html)


def template_test(request):
    return render(request, 'test.html')
