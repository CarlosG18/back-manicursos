# Generated by Django 5.0.3 on 2024-03-30 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=300)),
                ('criador', models.CharField(max_length=200)),
                ('datatime_da_pub', models.DateTimeField(auto_now=True)),
                ('conteudo', models.TextField()),
                ('imagem', models.ImageField(upload_to='noticias/')),
            ],
        ),
    ]
