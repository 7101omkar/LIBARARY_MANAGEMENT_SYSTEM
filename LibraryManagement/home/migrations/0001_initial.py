# Generated by Django 4.2.5 on 2023-09-16 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('publisher', models.CharField(max_length=200)),
                ('page', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('members_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email_id', models.CharField(max_length=200)),
                ('mobile_no', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members_id', models.IntegerField()),
                ('book_isbn', models.CharField(max_length=200)),
                ('issue_date', models.DateField()),
                ('return_date', models.DateField()),
                ('number_of_days', models.IntegerField()),
                ('total_rental_fees', models.IntegerField()),
            ],
        ),
    ]