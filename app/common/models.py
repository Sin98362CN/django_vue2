from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Menu(models.Model):
    type_name = models.CharField(max_length=100, null=True, blank=True, help_text='菜单是哪种类型，功能的还是某个模型上的')
    field_name = models.CharField(max_length=100, null=True, blank=True, help_text='对应的字段名')
    oneMenu = models.CharField(max_length=100, null=True, blank=True, help_text='一级菜单名')
    twoMenu = models.CharField(max_length=100, null=True, blank=True, help_text='二级菜单名，没有可以为空')
    is_delete = models.CharField(max_length=100, default=False, help_text='是否删除，其实就是是否可用')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='createName',
                               null=True, blank=True, help_text='创建人')
    lastModifyBy = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='changeName',
                                     null=True, blank=True, help_text='最后修改人')
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    value = models.CharField(max_length=100, null=True, blank=True, help_text='真正的值')
    order_num = models.PositiveIntegerField(default=100, help_text='查询的时候排序')

    class Meta:
        ordering = ['-order_num']


# 附件表
class FileForm(models.Model):
    source_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100, help_text='附件的名称')
    size = models.PositiveIntegerField()
    url = models.CharField(max_length=500, help_text='文件存放路径')
    create_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='file_form_create_user')
    modify_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='file_form_modify_user')
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_time']








