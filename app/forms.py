from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re
from .models import Item
import requests
import json
from django.conf import settings





class ItemForm(forms.ModelForm):
    postcode = forms.CharField(label='郵便番号', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='住所', widget=forms.TextInput(attrs={'class': 'form-control'}))

    phone_regex = RegexValidator(
        regex=r'^0\d{1,4}-\d{1,4}-\d{4}$',
        message="正しい電話番号を入力してください。"
    )
    section = forms.ChoiceField(choices=(
        ('管理本部', '管理本部'),
        ('財務部', '財務部'),
        ('法務部', '法務部'),
        ('人事部', '人事部'),
        ('営業一部', '営業一部'),
        ('営業二部', '営業二部'),
        ('IT一部', 'IT一部'),
        ('IT二部', 'IT二部'),
        ('広報部', '広報部')
    ), widget=forms.Select(attrs={'class': 'form-control'}), label='部署')
    rank = forms.ChoiceField(choices=(
        ('代表取締役社長', '代表取締役社長'),
        ('常務取締役', '常務取締役'),
        ('専務取締役', '専務取締役'),
        ('本部長', '本部長'),
        ('部長', '部長'),
        ('次長', '次長'),
        ('課長', '課長'),
        ('課長代理', '課長代理'),
        ('係長', '係長'),
        ('社員', '社員')
    ), widget=forms.Select(attrs={'class': 'form-control'}), label='役職')


    class Meta:
        model = Item
        fields = ('employee_number', 'name', 'age', 'section', 'rank', 'email_add', 'phone', 'postcode', 'address', 'station1', 'sex', 'memo')
        widgets = {
            'employee_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '記入例：12345'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email_add': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '記入例：xxx@example.com'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'station1': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.RadioSelect(choices=(('male', '男'), ('female', '女'))),
            'memo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '記入例：自由記述欄'}),
        }
        labels = {
            'email_add': 'Eメールアドレス',
            'phone': '電話番号',
            'postcode': '郵便番号',
            'address': '住所',
        }
        error_messages = {
            'sex': {'required': '性別を選択してください。'},
        }

    def clean_age(self):
        age = str(self.cleaned_data['age'])
        if int(age) < 18 or int(age) > 70:
            raise ValidationError('年齢は18歳から70歳までの範囲で入力してください。')
        return age

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            phone = phone.replace('-', '')
            if not re.match(r'^0\d{1,4}\d{1,4}\d{4}$', phone):
                raise forms.ValidationError("正しい電話番号を入力してください。")
        return phone

    #住所が入力された後にAPIを始動させ郵便番号が自動入力される
    # def clean_address(self):
    #     address = self.cleaned_data.get('address')
    #     if address:
    #         url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address, API_KEY)
    #         response = requests.get(url)
    #         data = json.loads(response.text)
    #         if data['status'] == 'OK':
    #             postcode = data['results'][0]['address_components'][-1]['long_name']
    #             self.cleaned_data['postcode'] = postcode[:3] + '-' + postcode[3:]
    #             self.cleaned_data['address'] = address
    #     return address
    #
    # def clean_postcode(self):
    #     address = self.cleaned_data.get('address')
    #     postcode = self.cleaned_data.get('postcode')
    #     if not postcode and address:
    #         url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(address, API_KEY)
    #         response = requests.get(url)
    #         data = json.loads(response.text)
    #         if data['status'] == 'OK':
    #             postcode = data['results'][0]['address_components'][-1]['long_name']
    #             self.cleaned_data['postcode'] = postcode[:3] + '-' + postcode[3:]
    #     return postcode
    #
    # 住所が存在しない場合のバリデーションチェック
    class YourForm(forms.ModelForm):
        API_KEY = 'AIzaSyCqiYNAANuvDuzEBy7R4Fr1svipbfpxc-Y'

        def clean_address(self):
            address = self.cleaned_data.get('address')
            if address:
                url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={self.API_KEY}'
                response = requests.get(url)
                if response.ok:
                    json_data = response.json()
                    if json_data['status'] == 'OK':
                        return address
                raise forms.ValidationError('存在する住所を入力してください。')
            else:
                raise forms.ValidationError('住所を入力してください。')