from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class SubsiteTitleViewlet(ViewletBase):
    render = ViewPageTemplateFile('viewlets/rer_subsite_title.pt')