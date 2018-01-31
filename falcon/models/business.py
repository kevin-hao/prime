#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Business(models.Model):
    name = models.CharField(max_length=128,verbose_name=_('业务线名'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('创建日期'))

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()