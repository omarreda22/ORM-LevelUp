# Generated by Django 4.1.5 on 2023-01-25 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_studentmultitable_delete_multitable'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiTable',
            fields=[
                ('studentmultitable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='students.studentmultitable')),
                ('new_name', models.CharField(blank=True, max_length=125, null=True)),
            ],
            bases=('students.studentmultitable',),
        ),
    ]
