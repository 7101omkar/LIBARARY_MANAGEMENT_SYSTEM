# Generated by Django 4.2.5 on 2023-09-19 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_transaction_is_returned'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryBook',
            fields=[
                ('book_id', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('average_rating', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('isbn13', models.CharField(max_length=200)),
                ('language_code', models.CharField(max_length=200)),
                ('num_pages', models.IntegerField()),
                ('ratings_count', models.IntegerField()),
                ('text_reviews_count', models.IntegerField()),
                ('publication_date', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('fee', models.IntegerField()),
            ],
        ),
    ]
