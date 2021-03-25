from django.db import models


# Create your models here.
# DB를 SQL 없이 다루려고 모델을 사용
# 우리가 데이터를 객체화해서 다루기위해(ORM 사용)
# 모델 = 테이블
# 모델의 필드 = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터값
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
# 필드의 종류가 결정하는 것
# 1. 데이터베이스의 컬럼 종류
# 2. 제약 사항 (몇 글자까지, 한글도 들어갈 수 있다 등등)
# 3. Form 의 종류
# 4. Form 에서의 제약 사항
