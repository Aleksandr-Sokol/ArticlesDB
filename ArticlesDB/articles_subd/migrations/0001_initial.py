# Generated by Django 3.1.5 on 2021-01-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название журнала')),
                ('short_name', models.CharField(max_length=250, null=True)),
                ('english_form_name', models.CharField(max_length=250, null=True)),
                ('is_rinc', models.BooleanField(default=False, null=True)),
                ('is_vak', models.BooleanField(default=False, null=True)),
                ('is_scopus', models.BooleanField(default=False, null=True)),
                ('is_wos', models.BooleanField(default=False, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]
