# Generated by Django 4.2.7 on 2024-02-15 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date of payment')),
                ('amount', models.PositiveIntegerField(verbose_name='Amount')),
                ('method', models.CharField(choices=[('C', 'Cash'), ('T', 'Translation')], max_length=1)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='materials.course', verbose_name='Course')),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='materials.lesson', verbose_name='Lesson')),
            ],
        ),
    ]
