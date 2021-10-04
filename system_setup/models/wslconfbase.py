# Copyright 2015 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
import attr

log = logging.getLogger('system_setup.models.wsl_configuration_base')


@attr.s
class WSLConfigurationBase(object):
    automount_root = attr.ib()
    automount_options = attr.ib()
    network_generatehosts = attr.ib()
    network_generateresolvconf = attr.ib()


class WSLConfigurationBaseModel(object):
    """ Model representing basic wsl configuration
    """

    def __init__(self):
        self._wslconfbase = None
        # TODO WSL: Load settings from system

    def apply_settings(self, result):
        d = {}
        d['automount_root'] = result.automount_root
        d['automount_options'] = result.automount_options
        d['network_generatehosts'] = result.network_generatehosts
        d['network_generateresolvconf'] = result.network_generateresolvconf
        self._wslconfbase = WSLConfigurationBase(**d)

    @property
    def wslconfbase(self):
        return self._wslconfbase

    def __repr__(self):
        return "<WSL Conf Base: {}>".format(self.wslconfbase)
