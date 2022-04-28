from django_filters import FilterSet, CharFilter, DateFilter, ModelMultipleChoiceFilter
from django.forms import DateInput
from .models import Author, Category, Ad, AdCategory, Response
from django.utils.translation import gettext as _
from django_filters import FilterSet, CharFilter, DateFilter
from django.forms import DateInput
from .models import Response


# создаём фильтр
class AdFilter(FilterSet):
    author = CharFilter(
        field_name='author_id__authorUser_id__username',
        lookup_expr='icontains',
        label=_('Author')
    )

    headline = CharFilter(
        field_name='headline',
        lookup_expr='icontains',
        label=_('Headline')
    )

    ad_time_in = DateFilter(
        field_name='ad_time_in',
        widget=DateInput(attrs={'type': 'date'}),
        lookup_expr='gt',
        label=_('Later dates')
    )

    class Meta:
        model = Ad
        fields = []


class ResponseFilter(FilterSet):
    # добавлю виджет для ввода даты
    resp_time_in = DateFilter(
        lookup_expr='gt',
        widget=DateInput(
            attrs={
                'type': 'date'
            }
        )
    )

    class Meta:
        model = Response
        fields = {
            'resp_user': ['exact'],
            'resp_post': ['exact'],
        }
