# -*- coding: utf-8 -*-

from zope.component import adapts
from zope.interface import implements

from archetypes.schemaextender.interfaces import ISchemaExtender
from archetypes.schemaextender.field import ExtensionField
from plone.app.blob.field import ImageField as BlobImageField

from Products.ATContentTypes.configuration import zconf
from Products.Archetypes import atapi
from Products.validation import V_REQUIRED

from rer.subsites.interfaces import IRERSubsite
from rer.subsites.content.subsite import RERSubsiteSchema

class ExtensionBlobField(ExtensionField, BlobImageField):
    """ derivative of blobfield for extending schemas """


class RERSubsiteExtender(object):
    adapts(IRERSubsite)
    implements(ISchemaExtender)

    fields = [

        ExtensionBlobField('image',
            required = False,
            languageIndependent = True,
            max_size = zconf.ATNewsItem.max_image_dimension,
            sizes = None,
            validators = (('isNonEmptyFile', V_REQUIRED),
                          ('checkNewsImageMaxSize', V_REQUIRED)),
            widget=atapi.ImageWidget(
                label=RERSubsiteSchema['image'].widget.label,
                description=RERSubsiteSchema['image'].widget.description,
            ),
        ),
              
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
