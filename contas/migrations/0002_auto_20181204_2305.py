# Generated by Django 2.1.3 on 2018-12-05 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={'ordering': ['nome', 'ra'], 'verbose_name': 'aluno', 'verbose_name_plural': 'alunos'},
        ),
    ]