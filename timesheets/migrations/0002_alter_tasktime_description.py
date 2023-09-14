# Generated by Django 4.2.4 on 2023-09-14 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktime',
            name='description',
            field=models.CharField(choices=[('Adm', 'Admin'), ('Des', 'Design'), ('Doc', 'Documentation'), ('Dwg', 'Drawings'), ('Gen', 'General'), ('Mod', 'Modifications')], default='Gen', max_length=3),
        ),
    ]
