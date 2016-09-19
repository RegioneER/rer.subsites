# -*- coding: utf-8 -*-
from zope.interface import Interface
from rer.subsites import subsitesMessageFactory as _
from zope import schema


class IRERSubsitesSettings(Interface):
    """
    Settings used in the control panel for Subsite colors
    """

    subsite_styles = schema.Text(
        title=_(u"Subsite styles"),
        description=_('help_subsite_styles',
                      default=u"Insert a list of css styles that will be applied in the subsite and his children. Where you need to use the subsite color, you should write '$color$' string."),
        required=False,
    )
