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
from Products.validation.config import validation
from Products.validation.interfaces import ivalidator
from Products.validation.validators.SupplValidators import MaxSizeValidator
from Products.validation import V_REQUIRED

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
    atapi.ImageField('image',
            widget=atapi.ImageWidget(
                label=_(u'rer_subsites_image', default=u'Image'),
                description=_(u'rer_subsites_image_help', default=u"Insert an image for the viewlet with the subsite name."),
            ),
            storage=atapi.AttributeStorage(),
            max_size=(768,768),
            sizes= {'large'   : (768, 768),
                    'preview' : (400, 400),
                    'mini'    : (200, 200),
                    'thumb'   : (128, 128),
                    'tile'    :  (64, 64),
                    'icon'    :  (32, 32),
                    'listing' :  (16, 16),
                      },
            validators = (('isNonEmptyFile', V_REQUIRED)),
            ),
    atapi.StringField('subsiteColor',
                required=True,
                widget=atapi.StringWidget(label=_(u'rer_subsites_color', default=u'Color of the subsite'),
                                    description=_(u'rer_subsites_color_help', default=u"Insert an hexadecimal value for the subsite color. Use the # character before the  value (for example: #FFFFFF)"),
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
