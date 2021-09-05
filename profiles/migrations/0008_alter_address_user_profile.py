# Generated by Django 3.2.6 on 2021-09-05 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_alter_address_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='profiles.userprofile'),
        ),
    ]
