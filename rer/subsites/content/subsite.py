# -*- coding: utf-8 -*-
"""Definition of the subsite content type
"""

from zope.interface import implements

from AccessControl import ClassSecurityInfo

from Products.CMFCore import permissions

from Products.ATContentTypes.content import schemata, folder
from Products.ATContentTypes.content.base import registerATCT
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import \
    ReferenceBrowserWidget
from Products.Archetypes import atapi

from rer.subsites import subsitesMessageFactory as _
from rer.subsites.config import PROJECTNAME
from rer.subsites.interfaces import IRERSubsite
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
                description=_(u'rer_subsites_image_help',
                              default=u"Insert an image for the viewlet with the subsite name."),
            ),
            storage=atapi.AttributeStorage(),
            validators = (('isNonEmptyFile', V_REQUIRED)),
            sizes=None,
            ),
    atapi.StringField('subsiteColor',
                required=False,
                widget=atapi.StringWidget(label=_(u'rer_subsites_color', default=u'Color of the subsite'),
                                    description=_(u'rer_subsites_color_help', default=u"Insert an hexadecimal value for the subsite color. Use the # character before the value (for example: #FFFFFF)"),
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
    
    security = ClassSecurityInfo()
    
    def allowedContentTypes(self):
        '''
        Remove RERSubsite to allowed types
        '''
        all_allowed_types = super(folder.ATFolder, self).allowedContentTypes()
        return [type for type in all_allowed_types if type.title != "Subsite"]

    security.declareProtected(permissions.View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        # Commented, as this folderish image create problems with folder_summary_view used in subfolders
        # https://penelope.redturtle.it/trac/er-portale/ticket/625
        #return self.getField('image').tag(self, **kwargs)
        return None

    def __bobo_traverse__(self, REQUEST, name):
        """Transparent access to image scales
        """
        if name.startswith('image'):
            field = self.getField('image')
            image = None
            if name == 'image':
                image = field.getScale(self)
            else:
                scalename = name[len('image_'):]
                if scalename in field.getAvailableSizes(self):
                    image = field.getScale(self, scale=scalename)
            if image is not None and not isinstance(image, basestring):
                # image might be None or '' for empty images
                return image

        return folder.ATFolder.__bobo_traverse__(self, REQUEST, name)

registerATCT(RERSubsite, PROJECTNAME)
