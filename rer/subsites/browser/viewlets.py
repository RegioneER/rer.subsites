# -*- coding: utf-8 -*-
from plone import api
from plone.app.layout.viewlets.common import ViewletBase
from rer.subsites.interfaces import IRERSubsitesSettings, IRERSubsiteEnabled
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SubsiteViewletBase(ViewletBase):
    def __init__(self, context, request, view, manager):
        super(SubsiteViewletBase, self).__init__(context, request, view, manager)
        self.subsite = self.getSubsiteObj()

    def render(self):
        if self.subsite:
            return self.index()
        else:
            return ""

    def getSubsiteObj(self):
        for elem in self.context.aq_inner.aq_chain:
            if IRERSubsiteEnabled.providedBy(elem):
                return elem
        return None


class SubsiteTitleViewlet(SubsiteViewletBase):
    """
    viewlet with title
    """
    index = ViewPageTemplateFile('viewlets/rer_subsite_title.pt')


class SubsiteColorViewlet(SubsiteViewletBase):
    """
    A Viewlet that allows to add some dynamic css in the  header
    """
    def render(self):
        if not self.subsite:
            return ""

        return_string = ''
        styles = self.get_default_styles()
        custom_styles = self.get_custom_styles()
        if custom_styles:
            styles += custom_styles
        return_string = "<style type='text/css'>%s</style>" % styles
        return return_string

    def get_default_styles(self):
        color = self.context.subsite_color
        image = self.context.image
        subsite_url = self.context.absolute_url()
        if not color and not image:
            return ""
        styles = []
        css = "#subsiteTitle {"
        if color:
            styles.append("background-color:%s" % color)
        if image:
            styles.append("background-image:url(%s/@@images/image)" % subsite_url)
        css += ';'.join(styles)
        css += '}'
        styles = []
        css += "#contentCarousel {"
        if color:
            styles.append("background-color:%s" % color)
        css += ';'.join(styles)
        css += '}'
        return css

    def get_custom_styles(self):
        """
        read styles from control panel
        """
        color = self.context.subsite_color
        css = api.portal.get_registry_record(
            'subsite_styles',
            interface=IRERSubsitesSettings)
        if not css:
            return ""
        return css.replace('\r\n', ' ').replace('$color$', color)
