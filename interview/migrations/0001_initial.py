# Generated by Django 4.2.4 on 2023-08-22 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Interviewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_identity', models.IntegerField(choices=[(1, '候场教室'), (2, '面试教室'), (3, 'observer')])),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='interview.department')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='interview.room')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Interviewee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('student_id', models.CharField(max_length=15)),
                ('majar_text', models.CharField(max_length=30)),
                ('introduction_text', models.TextField()),
                ('interview_status', models.IntegerField(choices=[(1, '未签到'), (2, '已签到候场'), (3, '已分配教室准备出发'), (4, '面试开始'), (5, '面试结束'), (6, '第 一志愿队列'), (7, '第二志愿队列'), (8, '最终队列'), (9, '已录取')])),
                ('accept_adjust', models.BooleanField()),
                ('assigned_datetime', models.DateTimeField()),
                ('admitted_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admitted_department', to='interview.department')),
                ('assigned_room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='interview.room')),
                ('first_preference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='first_preference', to='interview.department')),
                ('second_preference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='second_preference', to='interview.department')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('interviewee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.interviewee')),
                ('interviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
