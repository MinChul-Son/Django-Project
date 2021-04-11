from django import forms


# 클라이언트 화면에 입력 폼을 만듦
# 클라이너트가 입력한 데이터에 대한 전처리

# 이미 만들어져있는 모델에 대한 정보를 입력 받을 때는 ModelForm
class AddProductForm(forms.Form):
    quantity = forms.IntegerField()
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
