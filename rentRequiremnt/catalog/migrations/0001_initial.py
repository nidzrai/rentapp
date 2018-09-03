# Generated by Django 2.1.1 on 2018-09-01 21:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('date_of_additon', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ['brand_name', 'company_name'],
            },
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a Memory size (e.g. 1Tb,Gbs)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a Processor type)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief description of the Product', max_length=1000)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Brand')),
                ('memory', models.ManyToManyField(help_text='Enter a Memory size', to='catalog.Memory')),
                ('processor', models.ManyToManyField(help_text='Enter a Processor type', to='catalog.Processor')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular product across whole catalog', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('d', 'Done'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='d', help_text='prdoduct quotation availability', max_length=1)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Product')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a RAM', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='ram',
            field=models.ManyToManyField(help_text='Enter a RAM', to='catalog.RAM'),
        ),
    ]