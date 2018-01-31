#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .business import Business

class Server(models.Model):

    TYPE_CHOICES = (
        ('Server', _('物理机')),
        ('Xen', _('Xen虚拟机')),
    )

    ENV_CHOICES = (
        ('Prod', _('生产')),
        ('Dev', _('开发')),
        ('Test', _('测试')),
    )

    hostname = models.CharField(max_length=128, unique=True, verbose_name=_('业务名'))
    business_id = models.ForeignKey(Business, blank=True, null=True, related_name='server', on_delete=models.SET_NULL, verbose_name=_('机房'))
    cpu_count = models.IntegerField(null=True, verbose_name=_('CPU个数'))
    memory = models.CharField(max_length=64, null=True, blank=True, verbose_name=_('内存'))
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('创建日期'))