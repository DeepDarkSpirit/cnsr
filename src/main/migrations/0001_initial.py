# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('achievement_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=101)),
                ('achievement_type', models.CharField(max_length=2)),
                ('achievement_subtype', models.CharField(max_length=3)),
                ('level', models.CharField(max_length=2)),
                ('date', models.DateField()),
                ('journal', models.CharField(max_length=101)),
                ('journal_no', models.CharField(max_length=41)),
                ('conference', models.CharField(max_length=101)),
                ('award', models.CharField(max_length=101)),
                ('patent_no', models.CharField(max_length=41)),
                ('patent_applicant', models.CharField(max_length=61)),
                ('copyright_no', models.CharField(max_length=41)),
                ('copyright_reg_no', models.CharField(max_length=41)),
                ('copyright_owner', models.CharField(max_length=61)),
            ],
            options={
                'db_table': 'achievement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AchievementTeacherRelation',
            fields=[
                ('achievement_teacher_relation_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'achievement_teacher_relation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat', models.CharField(max_length=4)),
                ('title', models.CharField(max_length=101)),
                ('tag', models.CharField(max_length=21)),
                ('date', models.DateTimeField()),
                ('text', models.CharField(max_length=10002)),
                ('activity_start_date', models.DateField()),
                ('activity_end_date', models.DateField()),
            ],
            options={
                'db_table': 'article',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CooperationProject',
            fields=[
                ('cooperation_project_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=21)),
                ('nation', models.CharField(max_length=2)),
                ('cooperator', models.CharField(max_length=21)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'db_table': 'cooperation_project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CooperationProjectTeacherRelation',
            fields=[
                ('cooperation_project_teacher_relation_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'cooperation_project_teacher_relation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_no', models.CharField(max_length=21)),
                ('name', models.CharField(max_length=21)),
                ('course_type', models.CharField(max_length=21)),
                ('student_level', models.CharField(max_length=21)),
                ('semester', models.CharField(max_length=21)),
                ('start_week', models.CharField(max_length=21)),
                ('end_week', models.CharField(max_length=21)),
                ('remarks', models.CharField(max_length=101)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CourseTeacherRelation',
            fields=[
                ('course_teacher_relation_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'course_teacher_relation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EducationalRelation',
            fields=[
                ('educational_relation_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'educational_relation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=101)),
                ('project_type', models.CharField(max_length=101)),
                ('remarks', models.CharField(max_length=101)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'db_table': 'project',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectTeacherRelation',
            fields=[
                ('project_teacher_relation_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'project_teacher_relation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('sign_id', models.AutoField(primary_key=True, serialize=False)),
                ('sign_date', models.DateTimeField()),
                ('sign_place', models.CharField(max_length=21)),
            ],
            options={
                'db_table': 'sign',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_no', models.CharField(max_length=11)),
                ('account', models.CharField(max_length=21, unique=True)),
                ('password', models.CharField(max_length=21)),
                ('name_cn', models.CharField(max_length=21)),
                ('name_pinyin', models.CharField(max_length=41)),
                ('family_name', models.CharField(max_length=21)),
                ('given_name', models.CharField(max_length=21)),
                ('nickname', models.CharField(max_length=21)),
                ('sex', models.CharField(max_length=1)),
                ('student_type', models.CharField(max_length=2)),
                ('admission_date', models.CharField(max_length=21)),
                ('graduation_date', models.CharField(max_length=21)),
                ('grade', models.CharField(max_length=11)),
                ('mentor', models.CharField(max_length=21)),
                ('vice_mentor', models.CharField(max_length=21)),
                ('birthdate', models.DateField()),
                ('email', models.CharField(max_length=41)),
                ('cellphone', models.CharField(max_length=21)),
                ('tel', models.CharField(max_length=21)),
                ('photo', models.CharField(max_length=101)),
                ('auth_info_add', models.IntegerField()),
                ('auth_info_modify', models.IntegerField()),
                ('auth_info_delete', models.IntegerField()),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('teacher_no', models.CharField(max_length=11)),
                ('account', models.CharField(max_length=21, unique=True)),
                ('password', models.CharField(max_length=21)),
                ('name_cn', models.CharField(max_length=11)),
                ('name_pinyin', models.CharField(max_length=41)),
                ('family_name', models.CharField(max_length=21)),
                ('given_name', models.CharField(max_length=21)),
                ('nickname', models.CharField(max_length=21)),
                ('sex', models.CharField(max_length=1)),
                ('teacher_type', models.CharField(max_length=2)),
                ('nation', models.CharField(max_length=2)),
                ('unit', models.CharField(max_length=61)),
                ('title', models.CharField(max_length=41)),
                ('mentor_qual', models.CharField(max_length=41)),
                ('position_lab', models.CharField(max_length=61)),
                ('position_social', models.CharField(max_length=61)),
                ('position_school', models.CharField(max_length=61)),
                ('birthdate', models.DateField()),
                ('email', models.CharField(max_length=41)),
                ('cellphone', models.CharField(max_length=21)),
                ('tel', models.CharField(max_length=21)),
                ('photo', models.CharField(max_length=101)),
                ('auth_teacher', models.IntegerField()),
                ('auth_student', models.IntegerField()),
                ('auth_info_add', models.IntegerField()),
                ('auth_info_modify', models.IntegerField()),
                ('auth_info_delete', models.IntegerField()),
            ],
            options={
                'db_table': 'teacher',
                'managed': False,
            },
        ),
    ]
