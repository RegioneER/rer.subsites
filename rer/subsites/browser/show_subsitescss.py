from Products.Five import BrowserView

class View(BrowserView):
    """If the object is in a subsite, the css is loaded
    """
    def __call__(self):
        for elem in self.context.aq_chain:
            if getattr(elem,'portal_type','') == 'RERSubsite':
                return True
        return False