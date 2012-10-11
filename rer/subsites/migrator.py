# -*- coding: utf-8 -*-

from plone.app.blob.migrations import migrate as migrateBlob

def migrateSubsites(context):
    return migrateBlob(context, 'RERSubsite', 'RERSubsite')

