# -*- coding: utf-8 -*-
from zope.interface import Interface
from plone.namedfile.field import NamedBlobImage
from collective.z3cform.colorpicker import Color
from rer.subsites import subsitesMessageFactory as _
from zope import schema


class IRERSubsitesSettings(Interface):
    """
    Settings used in the control panel for Subsite colors
    """

    subsite_styles = schema.Text(
        title=_(u"Subsite styles"),
        description=_(
            'help_subsite_styles',
            default=u"Insert a list of css styles that will be applied in the "
                    u"subsite and his children. Where you need to use the "
                    u"subsite color, you should write '$color$' string."),
        required=False,
    )


class IRERSubsiteEnabled(Interface):

    subsite_color = Color(
        title=_(u'rer_subsites_color', default=u'Color of the subsite'),
        description=_(
            u'rer_subsites_color_help',
            default=u"Insert an hexadecimal value for the subsite color."
                    u" Use the # character before the value"
                    u" (for example: #FFFFFF)"
        ),
        required=False,
    )

    image = NamedBlobImage(
        title=_(u'rer_subsites_image', default=u'Image'),
        description=_(
            u'rer_subsites_image_help',
            default=u"Insert an image for the viewlet with the subsite name."),
        required=False,

    )
