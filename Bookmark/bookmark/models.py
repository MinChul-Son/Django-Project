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

    def __str__(self):
        return "사이트 명 : " + self.site_name + ", url: " + self.url

# 모델을 만들었다 ==> 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정!
# makemigrations ==> 모델의 변경사항을 추적해서 기록
# 마이그레이션(migrate) ==> 데이터베이스에 모델의 내용을 반경(테이블 생성)
