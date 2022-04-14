# Generated by Django 4.0.2 on 2022-04-14 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_issue_time_estimate_issuetype_needseverity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuetype',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='issuewithtitles',
            name='isComplete',
            field=models.BooleanField(default=True),
        ),
    ]
