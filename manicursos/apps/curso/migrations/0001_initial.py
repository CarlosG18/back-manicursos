# Generated by Django 5.0.3 on 2024-03-30 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('nivel', models.IntegerField(choices=[(1, 'superior'), (2, 'técnico')])),
                ('modalidade', models.IntegerField(choices=[(1, 'presencial'), (2, 'semipresencial'), (3, 'online')])),
                ('carga_horaria', models.IntegerField()),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(upload_to='.')),
            ],
        ),
    ]
