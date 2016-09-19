# -*- coding: utf-8 -*-
from plone.app.registry.browser import controlpanel
from Products.statusmessages.interfaces import IStatusMessage
from rer.subsites import subsitesMessageFactory as _
from rer.subsites.interfaces import IRERSubsitesSettings
from plone import api


class RERSubsitesSettingsEditForm(controlpanel.RegistryEditForm):
    """
    Subsites settings
    """
    schema = IRERSubsitesSettings
    id = "RERSubsitesSettingsEditForm"
    label = _(u"Subsites settings")
    description = _(u"help_subsites_settings_editform",
                    default=u"Set subsites configurations")


class RERSubsitesSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """Subsites settings control panel.
    """
    form = RERSubsitesSettingsEditForm
