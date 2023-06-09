# Generated by Django 4.2.2 on 2023-06-14 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_guitar_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitar',
            name='for_sale',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Using',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('use', models.CharField(choices=[('R', 'Recording'), ('T', 'Touring'), ('S', 'Storage')], default='R', max_length=1)),
                ('guitar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.guitar')),
            ],
        ),
    ]
