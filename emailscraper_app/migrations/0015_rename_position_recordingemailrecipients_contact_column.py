# Generated by Django 4.2.11 on 2024-08-24 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "emailscraper_app",
            "0014_rename_recordingemailsendsmetadata_emailsendsmetadata_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="recordingemailrecipients",
            old_name="position",
            new_name="contact_column",
        ),
    ]