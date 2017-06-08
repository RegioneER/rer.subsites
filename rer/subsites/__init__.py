
# -*- coding: utf-8 -*-
"""Init and utils."""

from zope.i18nmessageid import MessageFactory
from logging import getLogger


subsitesMessageFactory = MessageFactory('rer.subsites')
logger = getLogger('rer.subsites')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
