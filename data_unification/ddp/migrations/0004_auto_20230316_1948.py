# Generated by Django 3.1.2 on 2023-03-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddp', '0003_alter_files_id_alter_shared_id_alter_temuploads_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='shared',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='temuploads',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='uploads',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
