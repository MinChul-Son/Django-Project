import requests


def get_token():  # 키와 시크릿 키를 가지고 토큰을 가져옴
    pass


def payments_prepare(order_id, amount, *args, **kwargs): # 어떤 order_id로 얼마나 주문할 것인지 미리 아임포트에 알려주는 역할
    pass


def find_transaction(order_id, *args, **kwargs):  # 결제 완료 메시지가 오면 제대로 주문이 완료되었는지 확인
    pass
