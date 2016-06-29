#coding=utf-8
from django.shortcuts import render_to_response,render
from django.template import loader,Context
from django.http import HttpResponse,Http404,HttpResponseRedirect
import datetime,random,re
# Create your views here.
from django.http import HttpResponse
from main.models import Achievement,AchievementTeacherRelation,Article,CooperationProject,CooperationProjectTeacherRelation
from main.models import Course,CourseTeacherRelation,EducationalRelation,Project,ProjectTeacherRelation,Sign,Student,Teacher


def hello(request):
    return HttpResponse("Hello world")

def benke(request):
    posts = 123
    t =loader.get_template('benke.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def boshi(request):
    posts = 123
    t =loader.get_template('boshi.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def chart(request):
    posts = 123
    t =loader.get_template('chart.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def gonggongxiaoxi(request):
    posts = 123
    t =loader.get_template('gonggongxiaoxi.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def guojihezuo(request):
    posts = CooperationProject.objects.all()
    t =loader.get_template('guojihezuo.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def jiaoxuechengguo(request):
    posts = Achievement.objects.all()
    t =loader.get_template('jiaoxuechengguo.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def jiaoxuelunwen(request):
    posts = Achievement.objects.all()
    t =loader.get_template('jiaoxuelunwen.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def jiaoxuejiaocai(request):
    posts = Achievement.objects.all()
    t =loader.get_template('jiaoxuejiaocai.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def jiaoxuejiaogai(request):
    posts = Achievement.objects.all()
    t =loader.get_template('jiaoxuejiaogai.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def jiaoxuegongzuo(request):
    posts = Course.objects.all()
    t =loader.get_template('jiaoxuegongzuo.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def keyanchengguo(request):
    posts = Achievement.objects.all()
    t =loader.get_template('keyanchengguo.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def keyanlunwen(request):
    posts = Achievement.objects.all()
    t =loader.get_template('keyanlunwen.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def keyanzhuanli(request):
    posts = Achievement.objects.all()
    t =loader.get_template('keyanzhuanli.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def keyanzhuzuoquan(request):
    posts = Achievement.objects.all()
    t =loader.get_template('keyanzhuzuoquan.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def keyangongzuo(request):
    posts = Project.objects.all()
    t =loader.get_template('keyangongzuo.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def login(request):
    posts = 123
    t =loader.get_template('login.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def lianxiwomen(request):
    posts = 123
    t =loader.get_template('lianxiwomen.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def liuxuesheng(request):
    posts = 123
    t =loader.get_template('liuxuesheng.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def shiyanshijianjie(request):
    posts = 123
    t =loader.get_template('shiyanshijianjie.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def shiziduiwu(request):
    posts = Teacher.objects.all()
    t =loader.get_template('shiziduiwu.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def shouye(request):
    posts =  Article.objects.all()
    t =loader.get_template('shouye.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def shuoshi(request):
    posts = 123
    t =loader.get_template('shuoshi.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def tongzhi(request,param1):
    tempArticle=Article
    tempArticle.article_id= param1
    tempArticle2 = tempArticle.objects.get(article_id=tempArticle.article_id)
    t =loader.get_template('tongzhi.html')
    c =Context({'posts':tempArticle2})
    return HttpResponse(t.render(c))

def tianjiadongtaixiaoxi(request):
    posts = 123
    t =loader.get_template('tianjiadongtaixiaoxi.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def jiaoshiguanli(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = Teacher.objects.filter(name_cn__icontains=q)
        return render_to_response('jiaoshiguanli.html',
                {'posts': posts, 'query': q})
    posts = Teacher.objects.all()
    t =loader.get_template('jiaoshiguanli.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def xueshengguanli(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = Student.objects.filter(name_cn__icontains=q)
        return render_to_response('xueshengguanli.html',
                {'posts': posts, 'query': q})
    posts = Student.objects.all()
    t =loader.get_template('xueshengguanli.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def quanxianguanli(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts1 = Teacher.objects.filter(name_cn__icontains=q)
        posts2 = Student.objects.filter(name_cn__icontains=q)
        t =loader.get_template('quanxianguanli.html')
        c =Context({'posts1':posts1,'posts2':posts2})
        return HttpResponse(t.render(c))
#         return render_to_response('xueshuhuodong.html',
#                 {'posts1':posts1,'posts2':posts2, 'query': q})
    posts1 = Teacher.objects.all()
    posts2 = Student.objects.all()
    t =loader.get_template('quanxianguanli.html')
    c =Context({'posts1':posts1,'posts2':posts2})
    return HttpResponse(t.render(c))

def tianjiajiaoxuegongzuo(request):
    posts = 123
    t =loader.get_template('tianjiajiaoxuegongzuo.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def tianjiakeyangongzuo(request):
    posts = 123
    t =loader.get_template('tianjiakeyangongzuo.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))


def tianjiaquanxianguanli(request,param1,param2):
    if param1=='teacher':
        tempQuanXian=Teacher
        tempQuanXian.teacher_id= param2
        tempQuanXian2 = Teacher.objects.get(teacher_id=tempQuanXian.teacher_id)
        #tempQuanXian2.valid=0  
        t =loader.get_template('tianjiaquanxianguanli.html')
        c =Context({'posts':tempQuanXian2})
        return HttpResponse(t.render(c))
    if param1=='student':
        tempQuanXian=Student
        tempQuanXian.student_id= param2
        tempQuanXian2 = Student.objects.get(student_id=tempQuanXian.student_id)
        #tempQuanXian2.valid=0  
        t =loader.get_template('tianjiaquanxianguanli.html')
        c =Context({'posts':tempQuanXian2})
        return HttpResponse(t.render(c))
    return HttpResponse('error')


def tianjiajiaoshi(request):
    posts = 123
    t =loader.get_template('tianjiajiaoshi.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))


def tianjiaxuesheng(request):
    posts = 123
    t =loader.get_template('tianjiaxuesheng.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def tianjiachengguo(request):
    posts = 123
    t =loader.get_template('tianjiachengguo.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def tongzhitonggao(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = Article.objects.filter(title__icontains=q)
        return render_to_response('tongzhitonggao.html',
                {'posts': posts, 'query': q})
    posts = Article.objects.all()
    t =loader.get_template('tongzhitonggao.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def xiaoxi(request):
    posts = Article.objects.all()
    t =loader.get_template('xiaoxi.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def xinwendongtai(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = Article.objects.filter(title__icontains=q)
        return render_to_response('xinwendongtai.html',
                {'posts': posts, 'query': q})
    posts = Article.objects.all()
    t =loader.get_template('xinwendongtai.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))
   

def xueshengxinxi(request):
    posts = Student.objects.all()
    t =loader.get_template('xueshengxinxi.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def xueshuhuodong(request):
    if 'q' in request.GET:
        q = request.GET['q']
        posts = Article.objects.filter(title__icontains=q)
        return render_to_response('xueshuhuodong.html',
                {'posts': posts, 'query': q})
    posts = Article.objects.all()
    t =loader.get_template('xueshuhuodong.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def addNewsResualt(request):
    tempNews=Article()
    tempNews.cat= request.GET['cat']
    tempNews.teacher_id= 1
    tempNews.title= request.GET['title']
    tempNews.tag= request.GET['tag']
    tempNews.text= request.GET['news']
    tempNews.activity_start_date= request.GET['fromdate']
    tempNews.activity_end_date= request.GET['todate']  
    tempNews.valid=1
    tempNews.date=(datetime.datetime.now())
    tempNews.save()
    posts = tempNews.__class__.objects.all()
    t =loader.get_template('xinwendongtai.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))


def addKeyanResualt(request):
    
    tempNews=Project()
    tempNews.name= request.GET['name']
    tempNews.project_type= request.GET['project_type']
    tempNews.remarks= request.GET['remarks']
    tempNews.start_date= request.GET['fromdate']
    tempNews.end_date= request.GET['todate']
    tempNews.valid=1
    tempNews.save()
    posts = tempNews.__class__.objects.all()
    t =loader.get_template('keyangongzuo.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))


def addCourseResualt(request):
    
    tempNews=Course()
    tempNews.course_no= request.GET['course_no']
    tempNews.name= request.GET['name']
    tempNews.course_type= request.GET['course_type']
    tempNews.student_level= request.GET['student_level']
    tempNews.semester= request.GET['semester']
    tempNews.start_week= request.GET['start_week']
    tempNews.end_week= request.GET['end_week']
    tempNews.remarks= request.GET['remarks']
    tempNews.valid=1
    tempNews.save()
    posts = tempNews.__class__.objects.all()
    t =loader.get_template('jiaoxuegongzuo.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))


def addAchievementResualt(request):
    tempNews=Achievement()
    tempNews.name='null'
    tempNews.achievement_type= 'null'
    tempNews.achievement_subtype='null'
    tempNews.level= 'null'
    tempNews.date= '2015-09-18'
    tempNews.journal= 'null'
    tempNews.journal_no= 'null'
    tempNews.award= 'null'
    tempNews.patent_no= 'null'
    tempNews.patent_applicant= 'null'
    tempNews.copyright_reg_no= 'null'
    tempNews.copyright_owner= 'null'
    tempNews.conference= 'null'
    tempNews.valid=1
    if 'name' in request.GET:
        tempNews.name= request.GET['name']
    if 'achievement_type' in request.GET:
        tempNews.achievement_type= request.GET['achievement_type']
    if 'achievement_subtype' in request.GET:
        tempNews.achievement_subtype= request.GET['achievement_subtype']
    if 'level' in request.GET:
        tempNews.level= request.GET['level']
    if 'date' in request.GET:
        tempNews.date= request.GET['date']
    if 'journal' in request.GET:
        tempNews.journal= request.GET['journal']
    if 'journal_no' in request.GET:
        tempNews.journal_no= request.GET['journal_no']
    if 'award' in request.GET:
        tempNews.award= request.GET['award']
    if 'patent_no' in request.GET:
        tempNews.patent_no= request.GET['patent_no']
    if 'patent_applicant' in request.GET:
        tempNews.patent_applicant= request.GET['patent_applicant']
    if 'copyright_reg_no' in request.GET:
        tempNews.copyright_reg_no= request.GET['copyright_reg_no']
    if 'copyright_owner' in request.GET:
        tempNews.copyright_owner= request.GET['copyright_owner']
    if 'conference' in request.GET:
        tempNews.conference= request.GET['conference']
    tempNews.save()
    posts = tempNews.__class__.objects.all()
    t =loader.get_template('jiaoxuechengguo.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))

def deleNews(request):
    errors = '删除通知成功！'
    tempNews=Article
    tempNews.article_id= request.GET['article_id']
    tempNews2 = Article.objects.get(article_id=tempNews.article_id)
    tempNews2.valid=0  
    tempNews2.save()
    posts = Article.objects.all()
    t =loader.get_template('shouye.html')
    c =Context({'posts':posts,'errors': errors})
    return HttpResponse(t.render(c))

def editNews(request):
    tempNews=Article
    tempNews.article_id= request.GET['article_id']
    tempNews2 = Article.objects.get(article_id=tempNews.article_id)
    t =loader.get_template('editNews.html')
    c =Context({'posts':tempNews2})
    return HttpResponse(t.render(c))

def editNewsResult(request):  
    error = '修改消息信息成功！'
    tempNews=Article
    tempNews.article_id= request.GET['article_id']
    tempNews2 = Article.objects.get(article_id=Article.article_id)
    tempNews2.title= request.GET['title']   
    tempNews2.cat= request.GET['cat']
    tempNews2.teacher_id= 1
    tempNews2.text= request.GET['news'] 
    tempNews2.tag= request.GET['tag'] 
    tempNews2.activity_start_date= request.GET['fromdate'] 
    tempNews2.activity_end_date= request.GET['todate'] 
    tempNews2.valid=1
    tempNews2.date=(datetime.datetime.now())
    tempNews2.save()
    posts = Article.objects.all()
    t =loader.get_template('shouye.html')
    c =Context({'posts':posts,'errors': error})
    return HttpResponse(t.render(c))


def delTeacher(request,param1):
    errors = '删除教师成功！'
    tempTeacher=Teacher
    tempTeacher.teacher_id= param1
    tempTeacher2 = tempTeacher.objects.get(teacher_id=tempTeacher.teacher_id)
    tempTeacher2.valid=0
    tempTeacher2.save()
    posts = Teacher.objects.all()
    t =loader.get_template('jiaoshiguanli.html')
    c =Context({'posts':posts,'errors': errors})
    return HttpResponse(t.render(c))
    
def delStudent(request,param1):
    errors = '删除学生成功！'
    tempStudent=Student
    tempStudent.student_id= param1
    tempStudent2 = tempStudent.objects.get(student_id=tempStudent.student_id)
    tempStudent2.valid=0
    tempStudent2.save()
    posts = Student.objects.all()
    t =loader.get_template('xueshengguanli.html')
    c =Context({'posts':posts,'errors': errors})
    return HttpResponse(t.render(c))


# def quanxianguanliResult(request,param1,param2):
def quanxianguanliResult(request):
    id_type = request.GET['id_type']
    if id_type=='teacher':
        tempQuanXian=Teacher
        tempQuanXian.teacher_id= request.GET['id']
        tempQuanXian2 = Teacher.objects.get(teacher_id=tempQuanXian.teacher_id)
        if 'add_checkbox' in request.GET:
            tempQuanXian2.auth_info_add= 1
        else:
            tempQuanXian2.auth_info_add= 0
        if 'delete_checkbox' in request.GET:
            tempQuanXian2.auth_info_delete= 1
        else:
            tempQuanXian2.auth_info_delete= 0
        if 'modify_checkbox' in request.GET:
            tempQuanXian2.auth_info_modify= 1
        else:
            tempQuanXian2.auth_info_modify= 0
        if 'auth_student_checkbox' in request.GET:
            tempQuanXian2.auth_student= 1
        else:
            tempQuanXian2.auth_student= 0
        tempQuanXian2.save()
        t =loader.get_template('tianjiaquanxianguanli.html')
        c =Context({'posts':tempQuanXian2})
        return HttpResponse(t.render(c))
    if id_type =='student':
        tempQuanXian=Student
        tempQuanXian.student_id= request.GET['id']
        tempQuanXian2 = Student.objects.get(student_id=tempQuanXian.student_id)
        if 'add_checkbox' in request.GET:
            tempQuanXian2.auth_info_add= 1
        else:
            tempQuanXian2.auth_info_add= 0
        if 'delete_checkbox' in request.GET:
            tempQuanXian2.auth_info_delete= 1
        else:
            tempQuanXian2.auth_info_delete= 0
        if 'modify_checkbox' in request.GET:
            tempQuanXian2.auth_info_modify= 1
        else:
            tempQuanXian2.auth_info_modify= 0
        tempQuanXian2.save()
        t =loader.get_template('tianjiaquanxianguanli.html')
        c =Context({'posts':tempQuanXian2})
        return HttpResponse(t.render(c))
    error='error'
    return HttpResponse(error)

def addStudentResualt(request):
    tempStudent=Student()
    tempStudent.teacher_id= 1
    tempStudent.name_pinyin= 'null'
    tempStudent.family_name= 'null'
    tempStudent.given_name= 'null'
    tempStudent.nickname= 'null'
    tempStudent.admission_date= 'null'
    tempStudent.graduation_date= 'null'
    tempStudent.mentor= 'null'
    tempStudent.vice_mentor= 'null'
    tempStudent.birthdate= '2015-09-21'
    tempStudent.email= 'null'
    tempStudent.cellphone= 'null'
    tempStudent.photo= 'null'
    tempStudent.auth_info_modify= 0
    tempStudent.auth_info_add= 0
    tempStudent.auth_info_delete= 0
    tempStudent.valid=1
    if 'name_cn' in request.GET:
        tempStudent.name_cn= request.GET['name_cn']
    if 'grade' in request.GET:
        tempStudent.grade= request.GET['grade']
    if 'student_no' in request.GET:
        tempStudent.student_no= request.GET['student_no']
    if 'account' in request.GET:
        tempStudent.account= request.GET['account']
    if 'password' in request.GET:
        tempStudent.password= request.GET['password']
    if 'sex' in request.GET:
        tempStudent.sex= request.GET['sex']
    tempStudent.save()
    posts = tempStudent.__class__.objects.all()
    t =loader.get_template('xueshengguanli.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))


def addTeacherResualt(request):
    tempTeacher=Teacher()
    tempTeacher.teacher_id= 1
    tempTeacher.name_pinyin= 'null'
    tempTeacher.family_name= 'null'
    tempTeacher.given_name= 'null'
    tempTeacher.nickname= 'null'
    tempTeacher.unit= 'null'
    tempTeacher.title= 'null'
    tempTeacher.mentor_qual= 'null'
    tempTeacher.position_lab= 'null'
    tempTeacher.position_social= 'null'
    tempTeacher.position_school= 'null'
    tempTeacher.birthdate= '2015-09-21'
    tempTeacher.email= 'null'
    tempTeacher.cellphone= 'null'
    tempTeacher.tel= 'null'
    tempTeacher.photo= 'null'
    tempTeacher.auth_teacher= 0
    tempTeacher.auth_student= 1
    tempTeacher.auth_info_modify= 1
    tempTeacher.auth_info_add= 1
    tempTeacher.auth_info_delete= 1
    tempTeacher.valid=1
    if 'name_cn' in request.GET:
        tempTeacher.name_cn= request.GET['name_cn']
    if 'teacher_type' in request.GET:
        tempTeacher.grade= request.GET['teacher_type']
    if 'nation' in request.GET:
        tempTeacher.grade= request.GET['nation']
    if 'teacher_no' in request.GET:
        tempTeacher.student_no= request.GET['teacher_no']
    if 'account' in request.GET:
        tempTeacher.account= request.GET['account']
    if 'password' in request.GET:
        tempTeacher.password= request.GET['password']
    if 'sex' in request.GET:
        tempTeacher.sex= request.GET['sex']
    tempTeacher.save()
    posts = tempTeacher.__class__.objects.all()
    t =loader.get_template('jiaoshiguanli.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))


def baobiaotongji(request):
    posts = 123
    t =loader.get_template('baobiaotongji.html')
    c =Context({'posts':posts})
    return HttpResponse(t.render(c))