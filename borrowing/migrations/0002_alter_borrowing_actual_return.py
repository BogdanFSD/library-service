# Generated by Django 4.2.5 on 2023-09-14 05:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("borrowing", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="borrowing",
            name="actual_return",
            field=models.DateField(default=None, null=True),
        ),
    ]