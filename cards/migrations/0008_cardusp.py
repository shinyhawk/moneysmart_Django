# Generated by Django 4.2.1 on 2023-05-23 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardUsp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dd', models.CharField(max_length=30)),
                ('dt', models.CharField(max_length=200)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.card')),
            ],
        ),
    ]
