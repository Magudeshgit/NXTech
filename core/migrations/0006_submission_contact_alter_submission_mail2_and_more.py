# Generated by Django 5.0.7 on 2024-08-07 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_submission_participant2_submission_participant3'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='contact',
            field=models.CharField(default='test', max_length=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submission',
            name='mail2',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='mail3',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='participant2',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='participant3',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='teamname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
