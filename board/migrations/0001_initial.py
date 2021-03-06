# Generated by Django 3.0.8 on 2020-08-01 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_title', models.CharField(max_length=100)),
                ('board_member_name', models.CharField(max_length=100)),
                ('position_value', models.IntegerField()),
                ('image', models.ImageField(upload_to='board/media')),
            ],
        ),
    ]
