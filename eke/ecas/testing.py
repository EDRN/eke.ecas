# encoding: utf-8
# Copyright 2011 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from eke.knowledge.testing import EKE_KNOWLEDGE_FIXTURE
from eke.site.testing import EKE_SITE_FIXTURE
from eke.study.testing import EKE_STUDY_FIXTURE
from plone.app.testing import PloneSandboxLayer, IntegrationTesting, FunctionalTesting
from plone.testing import z2
from Products.CMFCore.utils import getToolByName

class EKEECAS(PloneSandboxLayer):
    defaultBases = (EKE_STUDY_FIXTURE, EKE_SITE_FIXTURE, EKE_KNOWLEDGE_FIXTURE)
    def setUpZope(self, app, configurationContext):
        import eke.ecas
        self.loadZCML(package=eke.ecas)
        z2.installProduct(app, 'eke.ecas')
        import eke.ecas.tests.base
        eke.ecas.tests.base.registerLocalTestData()
    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'eke.ecas:default')
        wfTool = getToolByName(portal, 'portal_workflow')
        wfTool.setDefaultChain('plone_workflow')
    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'eke.ecas')

EKE_ECAS_FIXTURE = EKEECAS()
EKE_ECAS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EKE_ECAS_FIXTURE,),
    name='EKEECAS:Integration',
)
EKE_ECAS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EKE_ECAS_FIXTURE,),
    name='EKEECAS:Functional',
)
