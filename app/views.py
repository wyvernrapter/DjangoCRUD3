# import sys
# sys.path.append(r'C:\Users\8100w\AppData\Local\Programs\Python\Python311\Lib\site-packages\django')
#
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from .filters import ItemFilter
from .forms import ItemForm
from .models import Item
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.views.generic.base import RedirectView

class CustomLoginView(LoginView):
    template_name = 'auth/custom_login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return reverse_lazy('index')
        else:
            return reverse_lazy('Userindex')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


def search_clear(request):
    if 'query' in request.session.keys():
        del request.session['query']
    if 'page' in request.session.keys():
        del request.session['page']
    return HttpResponseRedirect(reverse_lazy('index'))

@csrf_protect
def my_view(request):
    pass

from django.urls import reverse_lazy

class ItemFilterView(FilterView):
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

    def get_success_url(self):
        return reverse_lazy('item_filter') + '?' + self.request.GET.urlencode()

    def form_valid(self, form):
        self.object = form.save()
        return redirect(self.get_success_url())

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            if 'username' in request.session and 'password' in request.session:
                username = request.session['username']
                password = request.session['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)

        if request.method == 'POST':
            request.session['username'] = request.POST.get('username')
            request.session['password'] = request.POST.get('password')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clear_url'] = reverse_lazy('search_clear')
        return context

class SearchClearView(RedirectView):
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        if 'query' in self.request.session:
            del self.request.session['query']
        return reverse_lazy('index')

# 詳細画面
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item


# 登録画面
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')



# 更新画面
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # request.COOKIESを使用する場合はself.request.COOKIESを使用する
        cookies = self.request.COOKIES
        # その他の処理
        return super().form_valid(form)


# 削除画面
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('index')

