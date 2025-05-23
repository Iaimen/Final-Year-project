# Generated by Django 5.1.1 on 2025-04-15 05:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_chatmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='chatmessage',
            old_name='bot_response',
            new_name='bot',
        ),
        migrations.RenameField(
            model_name='chatmessage',
            old_name='created_at',
            new_name='timestamp',
        ),
        migrations.RenameField(
            model_name='chatmessage',
            old_name='user_query',
            new_name='user',
        ),
    ]
