# Generated by Django 3.1.5 on 2021-01-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles_subd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(max_length=250, verbose_name='Фамилия автора')),
                ('name', models.CharField(max_length=250, verbose_name='Имя автора')),
                ('soname', models.CharField(blank=True, max_length=250, verbose_name='Отчество автора')),
                ('english_form_family', models.CharField(blank=True, max_length=250, verbose_name='family')),
                ('english_form_name', models.CharField(blank=True, max_length=250, verbose_name='name')),
                ('english_form_soname', models.CharField(blank=True, max_length=250, verbose_name='soname')),
                ('work_place', models.CharField(blank=True, max_length=250, verbose_name='Место работы')),
                ('zvanie', models.CharField(choices=[('not', 'отсутствует'), ('ktn', 'к.т.н.'), ('kfmn', 'к.ф.м.н.'), ('dtn', 'д.т.н.'), ('dfmn', 'д.ф.м.н.')], default='not', max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='journal',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='journal',
            name='english_form_name',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='journal',
            name='short_name',
            field=models.CharField(blank=True, default=1, max_length=250),
            preserve_default=False,
        ),
    ]
