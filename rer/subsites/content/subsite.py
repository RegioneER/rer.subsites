# -*- coding: utf-8 -*-
"""Definition of the subsite content type
"""
from Products.ATContentTypes.content import schemata, folder
from Products.ATContentTypes.content.base import registerATCT
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import \
    ReferenceBrowserWidget
from Products.Archetypes import atapi
from rer.subsites import subsitesMessageFactory as _
from rer.subsites.config import PROJECTNAME
from rer.subsites.interfaces import IRERSubsite
from zope.interface import implements

RERSubsiteSchema = folder.ATFolderSchema.copy() + atapi.Schema((
    
    atapi.ReferenceField("newsArchiveFolder",
             storage=atapi.AnnotationStorage(),
             required=False,
             multiValued=False,
             relationship='newsArchiveFolder',
             widget=ReferenceBrowserWidget(
                            label=_('rer_subsites_newsarchivefolder', default=u'News archive'),
                            description=_('rer_subsites_newsarchivefolder_help', default=u'An archive for the news. If this field is set, the news in this subsite will show his value in "News archive" link'),
                            )
             ),
))

RERSubsiteSchema['title'].storage = atapi.AnnotationStorage()
RERSubsiteSchema['description'].storage = atapi.AnnotationStorage()
schemata.finalizeATCTSchema(RERSubsiteSchema, moveDiscussion=False)

class RERSubsite(folder.ATFolder):
    """Folder for RERSubsite"""
    implements(IRERSubsite)
    meta_type = "RERSubsite"
    schema = RERSubsiteSchema
    
    def allowedContentTypes(self):
        '''
        Remove RERSubsite to allowed types
        '''
        all_allowed_types = super(folder.ATFolder, self).allowedContentTypes()
        return [type for type in all_allowed_types if type.title != "Subsite"]
        
registerATCT(RERSubsite, PROJECTNAME)
