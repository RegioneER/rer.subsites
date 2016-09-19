# -*- coding: utf-8 -*-
from rer.subsites import logger

default_profile = 'profile-rer.subsites:default'
uninstall_profile = 'profile-rer.subsites:uninstall'


def to_1000(context):
    from Products.contentmigration.basemigrator.walker import MigrationError
    from rer.subsites.migrator import migrateSubsites
    try:
        output = migrateSubsites(context).splitlines()
        for msg in output:
            logger.info("    %s" % msg)
    except MigrationError:
        logger.warning("Error migrating to BLOB; still product upgrade will goes on")
    logger.info("Migrated to 1.2.0")


def to_1100(context):
    """
    Add a config panel to handle styles
    """
    logger.info('Upgrading rer.subsites to version 1100')
    context.runImportStepFromProfile(default_profile, 'plone.app.registry')
    context.runImportStepFromProfile(default_profile, 'controlpanel')
    logger.info('Reinstalled rolemap and controlpanel')
