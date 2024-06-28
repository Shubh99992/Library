# Generated by Django 5.0.6 on 2024-06-28 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_user_recent_reads"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="followers",
            field=models.ManyToManyField(related_name="following", to="app.user"),
        ),
    ]
