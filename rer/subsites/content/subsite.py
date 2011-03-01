# -*- coding: utf-8 -*-
"""Definition of the subsite content type
"""
from Products.ATContentTypes.content import folder
from Products.ATContentTypes.content.base import registerATCT
from rer.subsites.config import PROJECTNAME
from rer.subsites.interfaces import IRERSubsite
from zope.interface import implements

class RERSubsite(folder.ATFolder):
    """Folder for RERSubsite"""
    implements(IRERSubsite)
    meta_type = "RERSubsite"
    
    def allowedContentTypes(self):
        '''
        Remove RERSubsite to allowed types
        '''
        all_allowed_types = super(folder.ATFolder, self).allowedContentTypes()
        return [type for type in all_allowed_types if type.title != "Subsite"]
        
registerATCT(RERSubsite, PROJECTNAME)
