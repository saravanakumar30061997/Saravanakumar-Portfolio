# Generated by Django 5.1.6 on 2025-02-25 03:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_image'),
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='skill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='skills.skills'),
        ),
    ]
