# Generated by Django 2.1.2 on 2018-11-27 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0003_auto_20181127_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='adress',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='收货地址', to='users.Useradress'),
        ),
    ]