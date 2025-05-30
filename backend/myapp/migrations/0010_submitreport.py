# Generated by Django 5.1.1 on 2025-04-24 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('High Pollution Level', 'High Pollution Level'), ('Illegal Waste Dumping', 'Illegal Waste Dumping'), ('Industrial Emissions', 'Industrial Emissions'), ('Other Environmental Issue', 'Other Environmental Issue')], max_length=50)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
