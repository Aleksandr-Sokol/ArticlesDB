from django.shortcuts import render
from django.views.generic import CreateView
# from upload_data import upload_data_test
from .upload_data import upload_data_test

from .models import Article, Author, Journal
from .forms import JournalForm, AuthorForm, ArticleForm

def index(request):
    art = Article.objects.all()
    avt = Author.objects.all()
    context = {'art': art, 'avt': avt}
    return render(request, 'articles_subd/index.html', context)

def add_files(request):
    print('OK')
    d1 = {'name': 'Polymer testing', 'short_name': '', 'english_form_name': '', 'is_rinc': False, 'is_vak': True, \
          'is_scopus': True, 'is_wos': True, 'email': '---'}
    d2 = {'name': 'Polymer', 'short_name': '', 'english_form_name': '', 'is_rinc': True, 'is_vak': True, \
          'is_scopus': True, 'is_wos': True, 'email': '---'}
    d3 = {'name': 'Вестник ПНИПУ', 'short_name': '', 'english_form_name': 'PNIPU', 'is_rinc': True, 'is_vak': True, \
          'is_scopus': True, 'is_wos': False, 'email': 'pmipu@perm.ru'}
    if request.method == 'POST':
        file = request.FILES['file']
        # data = upload_data_test(file)
        for d in [d1, d2, d3]:
            Journal.objects.create(**d)
    return render(request, 'articles_subd/add_files.html')

class JournalCreateView(CreateView):
    template_name = 'articles_subd/create_journal.html'
    form_class = JournalForm
    success_url = '/add/journal/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journals'] = Journal.objects.all()
        return context


class AuthorCreateView(CreateView):
    template_name = 'articles_subd/create_author.html'
    form_class = AuthorForm
    success_url = '/add/author/'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['author'] = Author.objects.all()
    #     return context


class ArticleCreateView(CreateView):
    template_name = 'articles_subd/create_article.html'
    form_class = ArticleForm
    success_url = '/add/article/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.all()
        return context
