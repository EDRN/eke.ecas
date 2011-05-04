# encoding: utf-8
# Copyright 2009 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EKE ECAS: test the setup of this package.
'''

import unittest
from base import BaseTestCase
from Products.CMFCore.utils import getToolByName

class TestSetup(BaseTestCase):
    '''Unit tests the setup of this package.'''
    def testCatalogIndexes(self):
        '''Check if indexes are properly installed'''
        catalog = getToolByName(self.portal, 'portal_catalog')
        indexes = catalog.indexes()
        for i in ('bodySystemName', 'protocolName', 'collaborativeGroup', 'piUID'):
            self.failUnless(i in indexes)
    def testCatalogMetadata(self):
        '''Check if indexed metadata schema are properly installed'''
        catalog = getToolByName(self.portal, 'portal_catalog')
        metadata = catalog.schema()
        for i in ('bodySystemName', 'protocolName', 'collaborativeGroup', 'piUID'):
            self.failUnless(i in metadata)
    def testTypes(self):
        '''Make sure our types are available'''
        types = getToolByName(self.portal, 'portal_types').objectIds()
        for i in ('Dataset Folder', 'Dataset'):
            self.failUnless(i in types)

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
    
