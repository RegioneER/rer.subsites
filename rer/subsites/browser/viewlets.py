from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

class SubsiteViewletBase(ViewletBase):
    def __init__(self, context, request, view, manager):
        super(SubsiteViewletBase, self).__init__(context, request, view, manager)
        self.subsite=self.getSubsiteObj()
    
    def render(self):
        if self.subsite:
            return self.index()
        else:
            return ""
    
    def getSubsiteObj(self):
        for elem in self.context.aq_inner.aq_chain:
            if getattr(elem,'portal_type','') == 'RERSubsite':
                return elem
        return None
    
class SubsiteTitleViewlet(SubsiteViewletBase):
    index = ViewPageTemplateFile('viewlets/rer_subsite_title.pt')
    
class SubsiteColorViewlet(SubsiteViewletBase):
    """
    A Viewlet that allows to add some dynamic css in the  header
    """
    def render(self):
        if not self.subsite:
            return ""
        color=self.subsite.getSubsiteColor()
        image=self.subsite.getImage()
        return_string = ''
        if color or image:
            styles=[]
            css="#subsiteTitle {"
            if color:
                styles.append("background-color:%s" %color)
            if image:
                styles.append("background-image:url(%s)" %image.absolute_url())
            css +=';'.join(styles)
            css +='}'
            return_string = "<style type='text/css'>%s</style>" %css
        return return_string