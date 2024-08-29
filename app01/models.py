from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=18)

    """
    orm会将以上类翻译为如下SQL语句：
    create table app01_userinfo (
        id bigint auto_increment serial primary key,
        name varchar(32),
        password varchar(64),
        age int
    )
    """

class Department(models.Model):
    title = models.CharField(max_length=32)



# # 新增数据-- insert into app01_department (title) value ('销售部')
# Department.objects.create(title = '销售部')
#
# # 删除数据
# Department.objects.filter(id = 1).delete()
# Department.objects.all().delete()
#
# # 获取数据-- 返回结果为QuerySet类型，可类比为列表
# datalist1 = UserInfo.objects.all()
# for obj in datalist1:
#     print(obj.id, obj.name, obj.password, obj.age)
#
# datalist2 = Department.objects.filter(id = 1)
# for obj in datalist2:
#     print(obj.id, obj.name, obj.password, obj.age)
#
# row_obj = UserInfo.objects.filter(id = 1).first()    #    仅获取符合条件的第一行数据
# print(row_obj.name, row_obj.password, row_obj.age)
#
# # 修改数据
# UserInfo.objects.all().update(password = 777)
# UserInfo.objects.filter(name='sun').update(age = 16)
