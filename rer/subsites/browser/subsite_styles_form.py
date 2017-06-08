# -*- coding=utf-8 -*-
from .. import logger as _
from plone import api
from plone.directives.form import Schema
from plone.directives.form import SchemaForm
from z3c.form import button
from zope.component import adapter
from zope.interface import implementer
from rer.subsites.interfaces import IRERSubsiteSchema
from rer.subsites.interfaces import IRERSubsiteEnabled
from zope.interface import Invalid
from z3c.form.interfaces import WidgetActionExecutionError


@implementer(IRERSubsiteSchema)
@adapter(IRERSubsiteEnabled)
class SubsiteStylesFormAdapter(object):
    ''''''
    def __init__(self, context):
        ''' To basic stuff
        '''
        self.context = context
        self.subsite_color = getattr(context, 'subsite_color', '')
        self.image = getattr(context, 'image', '')


class SubsiteStylesForm(SchemaForm):

    ''' Dinamically built form
    '''
    schema = IRERSubsiteSchema
    ignoreContext = False

    def show_message(self, msg, msg_type):
        ''' Facade for the show message api function
        '''
        show_message = api.portal.show_message
        return show_message(msg, request=self.request, type=msg_type)

    def redirect(self, target=None, msg="", msg_type="error"):
        """ Redirects the user to the target, optionally with a portal message
        """
        if target is None:
            target = self.context.absolute_url()
        if msg:
            self.show_message(msg, msg_type)
        return self.request.response.redirect(target)

    def store_data(self, data):
        ''' Store the data before returning
        '''
        self.context.subsite_color = data.get('subsite_color')
        self.context.image = data.get('image')

    def additional_validation(self, data):
        return
        # Some additional validation
        if data.get('remoteUrl') and data.get('ISmartLinkExtension.internal_link'):
            raise WidgetActionExecutionError('remoteUrl',
                Invalid(_('error_internallink_externallink_doubled', default="You must select an internal link or enter an external link. You cannot have both."),))

    @button.buttonAndHandler(u'Salva', name='save')
    def handleSubmit(self, action):
        data, errors = self.extractData()
        self.additional_validation(data)
        if not errors:
            self.store_data(data)
            return self.redirect()

    @button.buttonAndHandler(u'Annulla', name='cancel')
    def handleCancel(self, action):
        """
        """
        return self.redirect()
