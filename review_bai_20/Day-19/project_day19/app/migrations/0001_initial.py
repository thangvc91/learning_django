# Generated by Django 4.0.4 on 2022-05-14 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('published_year', models.IntegerField()),
                ('total_qty', models.IntegerField()),
                ('current_qty', models.IntegerField()),
                ('max_duration', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.author')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image_url', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('fullname', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SaleOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('price_unit', models.IntegerField()),
                ('total', models.IntegerField()),
                ('order_date', models.DateTimeField()),
                ('status', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.productcategory')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.productcategory'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='BookCopy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=30, unique=True)),
                ('buy_date', models.DateField(blank=True, null=True)),
                ('status', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.book')),
            ],
        ),
        migrations.CreateModel(
            name='BookBorrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField()),
                ('deadline', models.DateField()),
                ('return_date', models.DateField()),
                ('status', models.IntegerField()),
                ('book_copy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.bookcopy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.user')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.category'),
        ),
        migrations.AddField(
            model_name='author',
            name='nationality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.country'),
        ),
    ]
