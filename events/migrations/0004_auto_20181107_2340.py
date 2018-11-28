# Generated by Django 2.1.3 on 2018-11-08 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20181107_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='followers',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='followers',
            name='user_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_followed', to='events.Users'),
        ),
    ]
