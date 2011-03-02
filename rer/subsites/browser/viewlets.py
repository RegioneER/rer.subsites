from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class SubsiteTitleViewlet(ViewletBase):
    index = ViewPageTemplateFile('viewlets/rer_subsite_title.pt')
    
    def __init__(self, context, request, view, manager):
        super(SubsiteTitleViewlet, self).__init__(context, request, view, manager)
        self.subsite_title=self.getSubsiteTitle()
        
    def render(self):
        if self.subsite_title:
            return self.index()
        else:
            return ""
    
    def getSubsiteTitle(self):
        for elem in self.context.aq_inner.aq_chain:
            if getattr(elem,'portal_type','') == 'RERSubsite':
                return elem.Title()
    
    