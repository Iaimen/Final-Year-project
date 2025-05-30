# Generated by Django 5.1.1 on 2025-04-24 22:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_report_delete_submitreport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatsession',
            name='session_id',
        ),
        migrations.AddField(
            model_name='chatsession',
            name='ended_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='myapp.chatsession')),
            ],
        ),
    ]
