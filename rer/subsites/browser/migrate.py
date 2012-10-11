# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope.formlib import form
try: # >= 4.1
    from five.formlib import formbase
except ImportError: # < 4.1
    from Products.Five.formlib import formbase
from Products.statusmessages.interfaces import IStatusMessage

from rer.subsites import subsitesMessageFactory as _
from rer.subsites.migrator import migrateSubsites

class IMigrateBlobsSchema(Interface):
    pass


class MigrateBlobs(formbase.PageForm):
    form_fields = form.FormFields(IMigrateBlobsSchema)
    label = _(u'BLOBs Migration')
    description = _(u'Migrate Subsite images to Blob')

    @form.action(_(u'Migrate'))
    def actionMigrate(self, action, data):
        output = migrateSubsites(self.context).splitlines()
        cnt = 0
        for l in output:
            cnt+=1
            IStatusMessage(self.request).addStatusMessage(l, type='info')

        return self.request.response.redirect(self.context.absolute_url())

    @form.action(_(u'Cancel'))
    def actionCancel(self, action, data):
        return self.request.response.redirect(self.context.absolute_url())

