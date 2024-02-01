# Generated by Django 5.0.1 on 2024-02-01 15:59

import blog.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, validators=[blog.validators.validate_email_domain]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.userprofile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.userprofile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=255, validators=[blog.validators.validate_title]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(validators=[blog.validators.validate_author_age]),
        ),
    ]
