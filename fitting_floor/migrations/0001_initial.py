# Generated by Django 4.2.4 on 2024-03-06 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_alter_project_options'),
        ('timesheets', '0004_alter_tasktime_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FittingTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elapsed_time', models.DurationField(blank=True, null=True)),
                ('time_started', models.DateTimeField(blank=True, null=True)),
                ('time_stopped', models.DateTimeField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now=True)),
                ('is_running', models.BooleanField(default=False)),
                ('is_ongoing', models.BooleanField(default=True)),
                ('ancillary_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='timesheets.ancillaryjobcode')),
                ('job_code', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.PROTECT, to='projects.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fitting_task', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date_created', 'user'],
            },
        ),
    ]
