# Generated by Django 2.1.3 on 2018-11-08 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20181108_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followers',
            name='user_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='is_followed', serialize=False, to='events.Users'),
        ),
        migrations.RemoveField(
            model_name='followers',
            name='id',
        ),
        migrations.AlterUniqueTogether(
            name='followers',
            unique_together={('user_a', 'user_b')},
        ),
    ]
