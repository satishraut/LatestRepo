# Generated by Django 2.1.5 on 2019-04-07 05:35

import department.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=30)),
                ('dcode', models.CharField(max_length=30)),
                ('dprof', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'dept_info',
            },
        ),
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'hobbies_info',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.TextField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('age', models.IntegerField()),
                ('photo', models.FileField(upload_to=department.models.user_directory_path)),
                ('website', models.URLField(max_length=250)),
                ('dept', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='stud', to='department.Department')),
            ],
            options={
                'db_table': 'stud_info',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('scode', models.CharField(max_length=100)),
                ('sremarks', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'subj_info',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='subjs',
            field=models.ManyToManyField(related_name='studs', to='department.Subject'),
        ),
        migrations.AddField(
            model_name='hobbies',
            name='stud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hobbies', to='department.Student'),
        ),
    ]
