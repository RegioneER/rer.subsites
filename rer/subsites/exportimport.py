# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName


def import_various(context):
    if context.readDataFile('ersubsites-various.txt') is None:
        return

    portal = context.getSite()
    addPropertySheet(portal)


def addPropertySheet(portal):
    portal_properties = getToolByName(portal, 'portal_properties')
    er_news_archive_properties = getattr(portal_properties, 'er_news_archive_properties',None)
    if not er_news_archive_properties:
        portal_properties.addPropertySheet(id='er_news_archive_properties',title='News archives properties')
        portal.plone_log("Added news archives properties property-sheet")
        er_news_archive_properties = getattr(portal_properties, 'er_news_archive_properties',None)
    if not er_news_archive_properties.hasProperty('type_filter'):
        er_news_archive_properties.manage_addProperty('type_filter',"RERSubsite", 'string')
    else:
        er_news_archive_properties.manage_changeProperties(type_filter='RERSubsite')
