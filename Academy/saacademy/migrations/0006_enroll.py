# Generated by Django 5.0.7 on 2024-08-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saacademy', '0005_faculties_course_sno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('price', models.BigIntegerField()),
            ],
        ),
    ]
