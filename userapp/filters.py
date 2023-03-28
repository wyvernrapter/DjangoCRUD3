from django_filters import FilterSet
from django_filters import filters

from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    name = filters.CharFilter(label='氏名', lookup_expr='contains')
    rank = filters.CharFilter(label='役職', lookup_expr='contains')
    section = filters.CharFilter(label='部署', lookup_expr='contains')

    order_by = MyOrderingFilter(
        fields=(
            ('name', 'name'),
            ('employee_number', 'employee_number'),
        ),
        field_labels={
            'name': '氏名',
            'employee_number': '社員番号',
        },
        label='並び順'
    )

    class Meta:
        model = Item
        fields = ('name', 'section' , 'rank',)