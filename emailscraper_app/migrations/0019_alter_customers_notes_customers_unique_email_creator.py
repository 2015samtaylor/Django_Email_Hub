# Generated by Django 4.2.11 on 2024-08-30 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emailscraper_app", "0018_customers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customers",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddConstraint(
            model_name="customers",
            constraint=models.UniqueConstraint(
                fields=("email", "creator_id"), name="unique_email_creator"
            ),
        ),
    ]
