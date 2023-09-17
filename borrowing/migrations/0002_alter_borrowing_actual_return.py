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