# Generated by Django 2.1.2 on 2018-11-26 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0002_goods_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userorder',
            name='adress',
            field=models.ForeignKey(default="", on_delete=django.db.models.deletion.DO_NOTHING, related_name='收货地址', to='users.Useradress'),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='fruser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='发送者', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='touser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='接受者', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userfavorite',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='收藏商品', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userfavorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='用户', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userdemand',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='应征商品', to='goods.Goods'),
        ),
        migrations.AddField(
            model_name='userdemand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='发起人', to=settings.AUTH_USER_MODEL),
        ),
    ]
