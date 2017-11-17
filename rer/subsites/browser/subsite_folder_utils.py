# -*- coding: utf-8 -*-
from rer.subsites.interfaces import IRERSubsiteEnabled
from rer.subsites.interfaces import IRERSubsiteUtilsView
from plone.app.contenttypes.interfaces import IFolder
from Products.Five.browser import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from plone import api
from zope.interface import alsoProvides, noLongerProvides
from zope.interface import implements


class BaseSubsiteView(BrowserView):
    def get_canonical(self):
        context = self.context.aq_inner
        pcs = context.restrictedTraverse('@@plone_context_state')
        return pcs.canonical_object()


class CheckSubsiteAction(BaseSubsiteView):

    def check_subsite_action_add(self):
        obj = self.get_canonical()
        if not IFolder.providedBy(obj):
            return False
        return not IRERSubsiteEnabled.providedBy(obj)

    def check_subsite_action_remove(self):
        obj = self.get_canonical()
        if not IFolder.providedBy(obj):
            return False
        return IRERSubsiteEnabled.providedBy(obj)


class ToggleMarkSubsite(BaseSubsiteView):

    def add_interface(self):
        obj = self.get_canonical()
        messages = IStatusMessage(self.request)
        if not IFolder.providedBy(obj):
            messages.addStatusMessage(
                u"Impossibile marcare il contenuto come subsite.",
                type='error'
            )
            return self.request.response.redirect(obj.absolute_url())
        if not IRERSubsiteEnabled.providedBy(obj):
            alsoProvides(obj, IRERSubsiteEnabled)
            obj.reindexObject(idxs=['object_provides'])
            messages.addStatusMessage(
                "Cartella marcata come subsite.", type='info')
        else:
            messages.addStatusMessage(
                u"Cartella già marcata come subsite.", type='warning')
        self.request.response.redirect(obj.absolute_url())

    def remove_interface(self):
        obj = self.get_canonical()
        messages = IStatusMessage(self.request)
        if IRERSubsiteEnabled.providedBy(obj):
            noLongerProvides(obj, IRERSubsiteEnabled)
            obj.reindexObject(idxs=['object_provides'])
            messages.addStatusMessage(u"Cartella non più subsite.",
                                      type='info')
        else:
            messages.addStatusMessage(u"La cartella non era già un subsite.",
                                      type='warning')

        self.request.response.redirect(obj.absolute_url())


class SubsiteUtilsView(BaseSubsiteView):

    implements(IRERSubsiteUtilsView)

    def get_subsite_folder(self):
        """
        Return the parent folder marked as "Subsite", for retrieve some infos
        like a color and the image pin
        """
        context = self.get_canonical()
        for elem in context.aq_inner.aq_chain:
            if IRERSubsiteEnabled.providedBy(elem):
                return elem
        return None

    def get_subsite_attributes(self):
        """
        Retrieve the subsite folder, and get saved css class
        """
        subsite = self.get_subsite_folder()
        if not subsite:
            return {}
        css_class = getattr(subsite, "subsite_css_class", subsite.getId())
        return {
            'title': subsite.Title(),
            'css_class': css_class,
            'pin': '{}/++resource++opr.theme/pins/pin-{}.png'.format(
                api.portal.get().absolute_url(),
                css_class
            )
        }

    def is_subsite_root(self, obj):
        """ Return True if a subsite is the root """
        return IRERSubsiteEnabled.providedBy(obj)
