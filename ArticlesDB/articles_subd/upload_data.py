from .models import Journal
import django

django.setup()

class upload_data_test():

    model = Journal

    def __init__(self, file):
        self.file = file
        self.creating()

    def creating(self):
        d1 = {'name' : 'Polymer testing', 'short_name' : '', 'english_form_name' : '', 'is_rinc' : False, 'is_vak' : True,\
              'is_scopus' : True, 'is_wos' : True, 'email' : '---'}
        d2 = {'name' : 'Polymer', 'short_name' : '', 'english_form_name' : '', 'is_rinc' : True, 'is_vak' : True,\
              'is_scopus' : True, 'is_wos' : True, 'email' : '---'}
        d3 = {'name' : 'Вестник ПНИПУ', 'short_name' : '', 'english_form_name' : 'PNIPU', 'is_rinc' : True, 'is_vak' : True,\
              'is_scopus' : True, 'is_wos' : False, 'email' : 'pmipu@perm.ru'}

        for d in [d1, d2, d3]:
            Journal.objects.create(**d)