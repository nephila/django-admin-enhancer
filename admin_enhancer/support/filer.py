# -*- coding: utf-8 -*-
from django.contrib.admin.sites import NotRegistered, AlreadyRegistered
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from ..admin import EnhancedModelAdminMixin

try:
   from cmsplugin_filer_image.admin import ThumbnailOption

   class EnhancedThumbnailOptionAdmin(EnhancedModelAdminMixin,admin.ModelAdmin):
       list_display = ('name', 'width', 'height')

   try:
       admin.site.unregister(ThumbnailOption)
   except NotRegistered,e:
       print e
   try:
       admin.site.register(ThumbnailOption, EnhancedThumbnailOptionAdmin)
   except AlreadyRegistered,e:
       print e

except ImportError:
  print "cmsplugin_filer not installed, patching skipped"
