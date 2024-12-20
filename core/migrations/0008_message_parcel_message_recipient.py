# Generated by Django 5.0.7 on 2024-11-17 06:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_remove_message_parcel_remove_message_recipient_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="parcel",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.parcel",
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="recipient",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="received_messages",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
