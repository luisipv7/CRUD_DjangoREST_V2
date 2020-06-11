# Generated by Django 3.0.6 on 2020-06-09 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(blank=True, default='', max_length=100)),
                ('idade', models.CharField(blank=True, default='', max_length=3)),
                ('telefone', models.CharField(blank=True, default='', max_length=13)),
                ('endereco', models.TextField()),
                ('log', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='contatos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
