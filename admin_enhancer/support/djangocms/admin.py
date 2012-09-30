# -*- coding: utf-8 -*-
from django.contrib.admin.sites import NotRegistered, AlreadyRegistered
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from ...admin import EnhancedModelAdminMixin

try:
    from cms.admin.pageadmin import PageAdmin,Page

    class EnhancedPageAdmin(EnhancedModelAdminMixin, PageAdmin):
        pass

    try:
        admin.site.unregister(Page)
    except NotRegistered, e:
        print e
    try:
        admin.site.register(Page, EnhancedPageAdmin)
    except AlreadyRegistered, e:
        print e
except ImportError:
    print "Error while importing django-cms, patching skipped"
