#!/usr/bin/python

import charms.reactive as reactive
from charms import apt
from charmhelpers.core import hookenv


@reactive.when_not('python-designate-dashboard.installed')
@reactive.when('dashboard-plugin.available')
def install_packages(rel=None):
    hookenv.status_set('maintenance', 'Installing software')
    hookenv.log("Installing designate dashboard plugin")
    apt.queue_install(['python-designate-dashboard'])
    apt.install_queued()
    reactive.set_state('python-designate-dashboard.installed')
    rel.set_remote('plugin-ready')

@reactive.when_not('dashboard-plugin.available')
@reactive.when('python-designate-dashboard.installed')
def remove_packages(rel=None):
    hookenv.status_set('maintenance', 'Removing software')
    hookenv.log("Uninstalling designate dashboard plugin")
    apt.purge(['python-designate-dashboard'])
    reactive.remove_state('python-designate-dashboard.installed')
