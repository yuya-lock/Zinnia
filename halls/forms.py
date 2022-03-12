from django import forms

from .models import Hall, Review


class HallCreateForm(forms.ModelForm):
    name = forms.CharField(label='会場名')
    picture = forms.FileField(label='写真', required=False)
    info = forms.CharField(label='詳細情報', widget=forms.Textarea)
    industry_type = forms.CharField(label='業種')
    business_hours = forms.CharField(label='営業時間', required=False)
    capacity = forms.IntegerField(label='キャパシティ')
    address = forms.CharField(label='住所')
    phone_number = forms.CharField(label='電話番号')
    website = forms.URLField(label='ホームページ')
    region = forms.CharField(label='地域')
    prefecture = forms.CharField(label='都道府県')
    area = forms.CharField(label='都市')
    is_able = forms.BooleanField(label='空き状況')
    buss = forms.CharField(label='アクセス（バス）', required=False)
    train = forms.CharField(label='アクセス（電車）', required=False)

    class Meta:
        model = Hall
        fields = ['name', 'picture', 'info', 'industry_type', 'business_hours', 'capacity', 'address', 'phone_number', 'website', 'region', 'prefecture', 'area', 'buss', 'train', 'is_able']


class ReviewCreateForm(forms.ModelForm):
    title = forms.CharField(label='レビュー')
    body = forms.CharField(label='詳細内容', widget=forms.Textarea, required=False)
    rate = forms.fields.ChoiceField(
        choices = (
            ('0', '0'),
            ('1', '1'),
            ('2', '3'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5')
        ),
        label='評価',
        required=False,
        widget=forms.widgets.RadioSelect
    )

    class Meta:
        model = Review
        fields = ['title', 'body', 'rate']
