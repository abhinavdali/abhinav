# Generated by Django 4.0.3 on 2022-03-08 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_driveruser_vehicle_number_user_vehicle_number'),
        ('shipment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='username',
            field=models.CharField(default='lol', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ship',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customeruser'),
        ),
    ]