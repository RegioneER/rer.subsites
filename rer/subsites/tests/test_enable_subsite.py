# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from rer.subsites.testing import RER_SUBSITES_INTEGRATION_TESTING  # noqa
import unittest2 as unittest
from rer.subsites.interfaces import IRERSubsiteEnabled
from zope.interface import alsoProvides


class TestSetup(unittest.TestCase):
    """Test that rer.subsites is properly installed."""

    layer = RER_SUBSITES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

        self.folder = api.content.create(
            type='Folder',
            title='Test folder',
            container=self.portal)

    def test_no_subsite_cant_access_subsite_styles_form(self):
        """
        """
        view = self.folder.restrictedTraverse('subsite_styles_form', None)
        self.assertIsNone(view)

    def test_subsite_can_access_subsite_styles_form(self):
        """
        """
        alsoProvides(self.folder, IRERSubsiteEnabled)
        view = self.folder.restrictedTraverse('subsite_styles_form', None)
        self.assertIsNotNone(view)
