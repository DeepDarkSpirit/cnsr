#coding=utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
    
class Achievement(models.Model):
    achievement_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=101)
    achievement_type = models.CharField(max_length=2)
    achievement_subtype = models.CharField(max_length=3)
    level = models.CharField(max_length=2)
    date = models.DateField()
    journal = models.CharField(max_length=101)
    journal_no = models.CharField(max_length=41)
    conference = models.CharField(max_length=101)
    award = models.CharField(max_length=101)
    patent_no = models.CharField(max_length=41)
    patent_applicant = models.CharField(max_length=61)
    copyright_no = models.CharField(max_length=41)
    copyright_reg_no = models.CharField(max_length=41)
    copyright_owner = models.CharField(max_length=61)
    valid = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'achievement'


class AchievementTeacherRelation(models.Model):
    achievement_teacher_relation_id = models.AutoField(primary_key=True)
    achievement = models.ForeignKey(Achievement, models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)
    valid = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'achievement_teacher_relation'


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    cat = models.CharField(max_length=4)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)
    title = models.CharField(max_length=101)
    tag = models.CharField(max_length=21)
    date = models.DateTimeField()
    text = models.CharField(max_length=10002)
    activity_start_date = models.DateField()
    activity_end_date = models.DateField()
    valid = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'article'


class CooperationProject(models.Model):
    cooperation_project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=21)
    nation = models.CharField(max_length=2)
    cooperator = models.CharField(max_length=21)
    start_date = models.DateField()
    end_date = models.DateField()
    valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cooperation_project'


class CooperationProjectTeacherRelation(models.Model):
    cooperation_project_teacher_relation_id = models.AutoField(primary_key=True)
    cooperation_project = models.ForeignKey(CooperationProject, models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)
    valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cooperation_project_teacher_relation'


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_no = models.CharField(max_length=21)
    name = models.CharField(max_length=21)
    course_type = models.CharField(max_length=21)
    student_level = models.CharField(max_length=21)
    semester = models.CharField(max_length=21)
    start_week = models.CharField(max_length=21)
    end_week = models.CharField(max_length=21)
    remarks = models.CharField(max_length=101)
    valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course'


class CourseTeacherRelation(models.Model):
    course_teacher_relation_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)
    valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course_teacher_relation'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()
    valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EducationalRelation(models.Model):
    educational_relation_id = models.AutoField(primary_key=True)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)
    student = models.ForeignKey('Student', models.DO_NOTHING)
    valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'educational_relation'


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=101)
    project_type = models.CharField(max_length=101)
    remarks = models.CharField(max_length=101)
    start_date = models.DateField()
    end_date = models.DateField()
    valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'project'


class ProjectTeacherRelation(models.Model):
    project_teacher_relation_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)
    valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'project_teacher_relation'


class Sign(models.Model):
    sign_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING)
    sign_date = models.DateTimeField()
    sign_place = models.CharField(max_length=21)
    valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sign'


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_no = models.CharField(max_length=11)
    account = models.CharField(unique=True, max_length=21)
    password = models.CharField(max_length=21)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)
    name_cn = models.CharField(max_length=21)
    name_pinyin = models.CharField(max_length=41)
    family_name = models.CharField(max_length=21)
    given_name = models.CharField(max_length=21)
    nickname = models.CharField(max_length=21)
    sex = models.CharField(max_length=1)
    admission_date = models.CharField(max_length=21)
    graduation_date = models.CharField(max_length=21)
    grade = models.CharField(max_length=11)
    mentor = models.CharField(max_length=21)
    vice_mentor = models.CharField(max_length=21)
    birthdate = models.DateField()
    email = models.CharField(max_length=41)
    cellphone = models.CharField(max_length=21)
    tel = models.CharField(max_length=21)
    photo = models.CharField(max_length=101)
    auth_info_add = models.IntegerField()
    auth_info_modify = models.IntegerField()
    auth_info_delete = models.IntegerField()
    valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'student'


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    teacher_no = models.CharField(max_length=11)
    account = models.CharField(unique=True, max_length=21)
    password = models.CharField(max_length=21)
    name_cn = models.CharField(max_length=11)
    name_pinyin = models.CharField(max_length=41)
    family_name = models.CharField(max_length=21)
    given_name = models.CharField(max_length=21)
    nickname = models.CharField(max_length=21)
    sex = models.CharField(max_length=1)
#     teacher_type = models.CharField(max_length=2)
#     nation = models.CharField(max_length=2)
    unit = models.CharField(max_length=61)
    title = models.CharField(max_length=41)
    mentor_qual = models.CharField(max_length=41)
    position_lab = models.CharField(max_length=61)
    position_social = models.CharField(max_length=61)
    position_school = models.CharField(max_length=61)
    birthdate = models.DateField()
    email = models.CharField(max_length=41)
    cellphone = models.CharField(max_length=21)
    tel = models.CharField(max_length=21)
    photo = models.CharField(max_length=101)
    auth_teacher = models.IntegerField()
    auth_student = models.IntegerField()
    auth_info_add = models.IntegerField()
    auth_info_modify = models.IntegerField()
    auth_info_delete = models.IntegerField()
    valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'teacher'
