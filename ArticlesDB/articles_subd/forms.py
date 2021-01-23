from django. forms import ModelForm

from .models import Author, Article, Journal

class JournalForm(ModelForm):
    class Meta:
        model = Journal
        fields = ('name', 'short_name', 'english_form_name', 'is_rinc', 'is_vak', 'is_scopus', 'is_wos', 'email')


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('family', 'name', 'soname', 'english_form_family', 'english_form_name', 'english_form_soname', \
                  'work_place', 'zvanie', 'email')


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('name', 'english_form_name', 'authors', 'journal', 'year', 'page', 'volume', 'grant_ref', 'abstract', 'pdf_file')
