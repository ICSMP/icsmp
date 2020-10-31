# Generated by Django 3.1.2 on 2020-10-31 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img3d',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('nome', models.CharField(max_length=32, unique=True)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('trabalhos_utilizados', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('arquivo', models.FileField(upload_to='')),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
