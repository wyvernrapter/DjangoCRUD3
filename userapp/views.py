from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import Item
from django.views.decorators.csrf import csrf_protect
from .filters import ItemFilter

class CustomLoginView(LoginView):
    template_name = 'auth/custom_login.html'

@csrf_protect
def my_view(request):
    pass

class ItemFilterView(LoginRequiredMixin, FilterView):
    model = Item

    # デフォルトの並び順を新しい順とする
    queryset = Item.objects.all().order_by('-created_at')

    # django-filter用設定
    filterset_class = ItemFilter
    strict = False

    # 1ページあたりの表示件数
    paginate_by = 30

    # 検索条件をセッションに保存する
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)


# 詳細画面
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item