from django.db import models


# Create your models here.
# >python manage.py makemigrations
# >python manage.py migrate
# 如果失败则追加app名python manage.py makemigrations ORM

class Teacher(models.Model):
    """讲师信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name='昵称')  # verbose_name：备注
    introduction = models.TextField(default='这位讲师很懒，什么也没有留下~', verbose_name='简介')
    fans = models.PositiveIntegerField(default='0', verbose_name='粉丝数')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # auto_now_add 新增时的时间
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')  # auto_now 修改时的时间

    class Meta:
        """元数据：可对表信息进行修改"""
        verbose_name = '讲师信息表'
        verbose_name_plural = verbose_name  # 英文中的复数，中文中可以verbose_name一样

    def __str__(self):
        return self.nickname


class Course(models.Model):
    """课程信息表"""
    title = models.CharField(max_length=100, primary_key=True, db_index=True, verbose_name='课程名')
    teacher = models.ForeignKey(Teacher, null=Teacher, blank=True, on_delete=models.CASCADE,
                                verbose_name='课程教师')  # 删除级联，多对一的关系
    type = models.CharField(choices=(('1', '实战课'), ('2', '免费课'), ('0', '其他')), max_length=1, default='0',
                            verbose_name='课程类型')  # choices 相当于枚举
    price = models.PositiveSmallIntegerField(verbose_name='价格')  # 小一点的int类型
    volume = models.BigIntegerField(verbose_name='销量')
    online = models.DateField(verbose_name='上线时间')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '课程信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        # f就是format,相当于{}-{}.format(self.get_type_display(),self.title)
        return f'{self.get_type_display()}-{self.title}'


class Student(models.Model):
    """学生信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name='昵称')
    course = models.ManyToManyField(Course,verbose_name='课程')  # 多对多
    age = models.PositiveSmallIntegerField(verbose_name='年龄')
    gender = models.CharField(choices=(('1', '男'), ('2', '女'), ('0', '保密')), max_length=1, default='0', verbose_name='性别')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '学生信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class TeacherAssistant(models.Model):
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name='昵称')
    teacher = models.OneToOneField(Teacher, null=True, blank=True, on_delete=models.SET_NULL,
                                   verbose_name='讲师')  # 一对一关系，级联关系为置空
    hobby = models.CharField(max_length=100, null=True, blank=True, verbose_name='爱好')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name = '助教信息表'
        db_table = 'course_assistant'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname
