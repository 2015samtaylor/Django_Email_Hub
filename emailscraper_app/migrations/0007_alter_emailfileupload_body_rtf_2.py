# Generated by Django 4.2.11 on 2024-06-03 03:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("emailscraper_app", "0006_remove_emailfileupload_body_rtf"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailfileupload",
            name="body_rtf_2",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
