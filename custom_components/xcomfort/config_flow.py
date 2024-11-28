###Version 1.3.6
from homeassistant.const import CONF_NAME
from homeassistant import config_entries
import voluptuous as vol
import logging

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema(
    {
        vol.Required("url", default="http://10.0.0.20"): str,
        vol.Required("username", default="admin1"): str,
        vol.Required("password",default=""): str,
        vol.Required("zones", default="hz_3,hz_4"): str,  # comma-separated zones
        vol.Required("scan_interval", default=5): int,
        vol.Optional("heating_zone0",default=""): str,
        vol.Optional("heating_zone0_radiator",default=""): str,
        vol.Optional("heating_zone1",default=""): str,
        vol.Optional("heating_zone1_radiator",default=""): str,
        vol.Optional("heating_zone2",default=""): str,
        vol.Optional("heating_zone2_radiator",default=""): str,
        vol.Optional("heating_zone3",default=""): str,
        vol.Optional("heating_zone3_radiator",default=""): str,
        vol.Optional("heating_zone4",default=""): str,
        vol.Optional("heating_zone4_radiator",default=""): str,
        vol.Optional("heating_zone5",default=""): str,
        vol.Optional("heating_zone5_radiator",default=""): str
    }
)


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    async def async_step_user(self, user_input=None):
        _LOGGER.debug("ConfigFlow start")
        
        errors = {}
        
        if user_input is not None:
            user_input["zones"] = [zone.strip() for zone in user_input["zones"].split(",")]
            await self.async_set_unique_id(user_input["url"], raise_on_progress=False)
            self._abort_if_unique_id_configured()
            
            return self.async_create_entry(title="xcomfort", data=user_input)
        return self.async_show_form(
            step_id="user", data_schema=DATA_SCHEMA, errors=errors,
        )
