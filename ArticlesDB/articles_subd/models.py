from django.db import models
from .validators import validate_file_extension

class Journal(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название журнала")
    short_name = models.CharField(max_length=250, blank=True)
    english_form_name = models.CharField(max_length=250, blank=True)
    is_rinc = models.BooleanField(null=True, default=False)
    is_vak = models.BooleanField(null=True, default=False)
    is_scopus = models.BooleanField(null=True, default=False)
    is_wos = models.BooleanField(null=True, default=False)
    email = models.EmailField(blank=True)

    def __str__(self):
        return "Journal is %s or %s" %(self.name, self.english_form_name)


class Author(models.Model):
    ZVANIE_CHOICES = (
    ('not', 'отсутствует'),
    ('ktn', 'к.т.н.'),
    ('kfmn', 'к.ф.м.н.'),
    ('dtn', 'д.т.н.'),
    ('dfmn', 'д.ф.м.н.'),
    )
    family = models.CharField(max_length=250, verbose_name="Фамилия автора")
    name = models.CharField(max_length=250, verbose_name="Имя автора")
    soname = models.CharField(max_length=250, verbose_name="Отчество автора", blank=True)
    english_form_family = models.CharField(max_length=250, verbose_name="family", blank=True)
    english_form_name = models.CharField(max_length=250, verbose_name="name", blank=True)
    english_form_soname = models.CharField(max_length=250, verbose_name="soname", blank=True)
    work_place = models.CharField(max_length=250, verbose_name="Место работы", blank=True)
    zvanie = models.CharField(max_length=20, choices=ZVANIE_CHOICES, default='not')
    email = models.EmailField(blank=True)

    def __str__(self):
        return "Author is %s %s" %(self.name, self.family)


class Article(models.Model):
    name = models.CharField(max_length=250, verbose_name="Название статьи")
    english_form_name = models.CharField(max_length=250, verbose_name="name", blank=True)
    authors = models.ManyToManyField(Author)
    journal = models.ForeignKey(Journal, on_delete=models.PROTECT)
    year = models.IntegerField(verbose_name="Год издания")
    page = models.CharField(max_length=250, verbose_name="страницы", blank=True)
    volume = models.IntegerField(verbose_name="номер", blank=True, null=True)
    grant_ref = models.CharField(max_length=250, verbose_name="ссылки на грант", blank=True)
    abstract = models.TextField(blank=True)
    pdf_file = models.FileField(validators=[validate_file_extension], upload_to='pdf_files/')

    def __str__(self):
        return "Article is %s, authors %s, year: %i" %(self.name, self.authors, self.year)


