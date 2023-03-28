from django_filters import FilterSet
from django_filters import filters

from .models import Item


class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s （降順）'


class ItemFilter(FilterSet):

    name = filters.CharFilter(label='氏名', lookup_expr='contains')
    RANK_CHOICES = (
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
    )
    rank = filters.ChoiceFilter(label='役職', choices=Item.RANK_CHOICES, lookup_expr='contains')
    SECTION_CHOICES = (
        ('管理本部', '管理本部'),
        ('財務部', '財務部'),
        ('法務部', '法務部'),
        ('人事部', '人事部'),
        ('営業一部', '営業一部'),
        ('営業二部', '営業二部'),
        ('IT一部', 'IT一部'),
        ('IT二部', 'IT二部'),
        ('広報部', '広報部')
    )
    section = filters.ChoiceFilter(label='部署', choices=Item.SECTION_CHOICES, lookup_expr='contains')

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
