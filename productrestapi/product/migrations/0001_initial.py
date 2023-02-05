# Generated by Django 4.1.5 on 2023-01-22 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('pvendor', models.CharField(max_length=30)),
                ('pmodel', models.CharField(max_length=30)),
                ('pqty', models.IntegerField()),
                ('pprice', models.FloatField()),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['pname', 'pvendor'], name='product_pname_a72542_idx'),
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.UniqueConstraint(fields=('pname', 'pvendor'), name='uqnamevendor'),
        ),
    ]
