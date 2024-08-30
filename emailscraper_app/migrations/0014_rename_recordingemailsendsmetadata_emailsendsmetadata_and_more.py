# Generated by Django 4.2.11 on 2024-08-24 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("emailscraper_app", "0013_alter_emailfileupload_creator_id"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="RecordingEmailSendsMetaData", new_name="EmailSendsMetaData",
        ),
        migrations.CreateModel(
            name="RecordingEmailRecipients",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email_recipient", models.EmailField(max_length=254)),
                ("date_sent", models.DateTimeField()),
                ("subject", models.CharField(max_length=255)),
                ("position", models.CharField(max_length=255)),
                ("from_email", models.EmailField(max_length=254)),
                ("email_campaign_tag", models.CharField(max_length=255)),
                (
                    "creator_id",
                    models.ForeignKey(
                        db_column="creator_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]