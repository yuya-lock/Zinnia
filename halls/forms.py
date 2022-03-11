from django import forms

from .models import Hall, Review, Rating


class HallCreateForm(forms.ModelForm):
    name = forms.CharField(label='会場名')
    picture = forms.FileField(label='写真')
    info = forms.CharField(label='詳細情報', widget=forms.Textarea)
    industry_type = forms.CharField(label='業種')
    genre = forms.CharField(label='ジャンル')
    business_hours = forms.CharField(label='営業時間')
    capacity = forms.IntegerField(label='キャパシティ')
    address = forms.CharField(label='住所')
    phone_number = forms.CharField(label='電話番号')
    website = forms.URLField(label='ホームページ')
    region = forms.CharField(label='地域')
    prefecture = forms.CharField(label='都道府県')
    area = forms.CharField(label='都市')
    is_able = forms.BooleanField(label='空き状況')
    buss = forms.CharField(label='アクセス（バス）')
    train = forms.CharField(label='アクセス（電車）')

    class Meta:
        model = Hall
        fields = ['name', 'picture', 'info', 'industry_type', 'genre', 'business_hours', 'capacity', 'address', 'phone_number', 'website', 'region', 'prefecture', 'area', 'is_able', 'buss', 'train']


class ReviewCreateForm(forms.ModelForm):
    title = forms.CharField(label='タイトル')
    body = forms.CharField(label='内容', widget=forms.Textarea)

    class Meta:
        model = Review
        fields = ['title', 'body']
