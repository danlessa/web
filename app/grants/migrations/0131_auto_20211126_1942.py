# Generated by Django 2.2.24 on 2021-11-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grants', '0130_grantclr_grant_clr_percentage_cap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grantclr',
            name='type',
            field=models.CharField(choices=[('main', 'Main Round'), ('ecosystem', 'Ecosystem Round'), ('cause', 'Cause Round')], default='main', help_text='Grant CLR Type', max_length=25),
        ),
    ]
