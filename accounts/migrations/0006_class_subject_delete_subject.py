# Generated by Django 5.2 on 2025-05-09 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_name_subject_subject_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
