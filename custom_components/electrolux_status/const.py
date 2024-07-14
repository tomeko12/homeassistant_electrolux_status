"""The electrolux Status constants."""

from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.components.button import ButtonDeviceClass
from homeassistant.components.number import NumberDeviceClass
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.switch import SwitchDeviceClass
from homeassistant.const import (
    PERCENTAGE,
    Platform,
    UnitOfPower,
    UnitOfTemperature,
    UnitOfTime,
    UnitOfVolume,
)
from homeassistant.helpers.entity import EntityCategory

from .model import ElectroluxDevice

# Base component constants
NAME = "Electrolux status"
DOMAIN = "electrolux_status"
DOMAIN_DATA = f"{DOMAIN}_data"

# Platforms
BINARY_SENSOR = Platform.BINARY_SENSOR
BUTTON = Platform.BUTTON
NUMBER = Platform.NUMBER
SELECT = Platform.SELECT
SENSOR = Platform.SENSOR
SWITCH = Platform.SWITCH
PLATFORMS = [BINARY_SENSOR, BUTTON, NUMBER, SELECT, SENSOR, SWITCH]

# Configuration and options
CONF_LANGUAGE = "language"
CONF_RENEW_INTERVAL = "renew_interval"

# Defaults
DEFAULT_LANGUAGE = "English"
DEFAULT_WEBSOCKET_RENEWAL_DELAY = 43200  # 12 hours

# these are attributes that appear in the state file but not in the capabilities.
# defining them here and in the catalog will allow these devices to be added dynamicaly
STATIC_ATTRIBUTES = [
    "connectivityState",
    "networkInterface/linkQualityIndicator",
    "applianceMode",
]

Catalog: dict[str, ElectroluxDevice] = {
    "airFilterLifeTime": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:air-filter",
    ),
    "airFilterLifeTimeBuyThreshold": ElectroluxDevice(
        capability_info={"access": "constant", "default": 12873600, "type": "number"},
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:air-filter",
        entity_registry_enabled_default=False,
    ),
    "airFilterLifeTimeChangeThreshold": ElectroluxDevice(
        capability_info={"access": "constant", "default": 15724800, "type": "number"},
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:air-filter",
        entity_registry_enabled_default=False,
    ),
    "airFilterState": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "string",
            "values": {"BUY": {}, "CHANGE": {}, "CLEAN": {}, "GOOD": {}},
        },
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:air-filter",
    ),
    "airFilterStateReset": ElectroluxDevice(
        capability_info={
            "access": "write",
            "type": "string",
            "values": {"RESET": {}},
        },
        device_class=None,
        unit=None,
        entity_category=EntityCategory.CONFIG,
        entity_icon="mdi:air-filter",
    ),
    "alerts": ElectroluxDevice(
        capability_info={"access": "read", "type": "alert"},
        device_class=None,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:alert",
    ),
    "applianceMode": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "string",
            "values": {"DEMO": {}, "NORMAL": {}, "SERVICE": {}},
        },
        device_class=None,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:auto-mode",
        entity_registry_enabled_default=False,
    ),
    "applianceState": ElectroluxDevice(
        capability_info={"access": "read", "type": "string"},
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:state-machine",
    ),
    "applianceTotalWorkingTime": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:clock-time-eight-outline",
    ),
    "connectivityState": ElectroluxDevice(
        capability_info={"access": "read", "type": "string"},
        device_class=SensorDeviceClass.ENUM,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:wifi",
    ),
    "cyclePhase": ElectroluxDevice(
        capability_info={"access": "read", "type": "string"},
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon=None,
    ),
    "cycleSubPhase": ElectroluxDevice(
        capability_info={"access": "read", "type": "string"},
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon=None,
    ),
    "defrostRoutineState": ElectroluxDevice(
        capability_info={"access": "read", "type": "string"},
        device_class=None,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:snowflake-thermometer",
        entity_registry_enabled_default=False,
    ),
    "defrostTemperature": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
        entity_category=None,
        entity_icon="mdi:thermometer",
    ),
    "defaultExtraRinse": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "type": "string",
            "values": {
                "EXTRA_RINSE_1": {},
                "EXTRA_RINSE_2": {},
                "EXTRA_RINSE_OFF": {},
            },
        },
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon=None,
    ),
    "displayFoodProbeTemperature": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
        entity_category=None,
        entity_icon="mdi:thermometer",
    ),
    "displayTemperature": ElectroluxDevice(
        capability_info={"access": "read", "type": "string"},
        device_class=SensorDeviceClass.TEMPERATURE,
        unit=None,
        entity_category=None,
        entity_icon="mdi:thermometer",
    ),
    "doorLock": ElectroluxDevice(
        capability_info={"access": "read", "type": "string"},
        device_class=BinarySensorDeviceClass.LOCK,
        unit=None,
        entity_category=None,
        entity_icon="mdi:door-closed-lock",
    ),
    "doorState": ElectroluxDevice(
        capability_info={"access": "read", "type": "string"},
        device_class=BinarySensorDeviceClass.DOOR,
        unit=None,
        entity_category=None,
        entity_icon="mdi:door",
    ),
    "endOfCycleSound": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "type": "string",
            "values": {"NO_SOUND": {}, "SHORT_SOUND": {}},
        },
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:cellphone-sound",
    ),
    "executeCommand": ElectroluxDevice(
        capability_info={
            "access": "write",
            "type": "string",
            "values": {
                "OFF": {},
                "ON": {},
                "PAUSE": {},
                "RESUME": {},
                "START": {},
                "STOPRESET": {},
            },
        },
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:house",
    ),
    "extraCavity/alerts": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "alert",
            "values": {
                "AIR_SENSOR_BROKEN": {},
                "AIR_SENSOR_OPEN_CIRCUIT": {},
                "AIR_SENSOR_SHORT_CIRCUIT": {},
                "DOOR_ALARM": {},
                "TEMPERATURE_ALARM": {},
            },
        },
        device_class=None,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:alert",
    ),
    "extraCavity/applianceState": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "string",
            "values": {"OFF": {}, "RUNNING": {}},
        },
        device_class=BinarySensorDeviceClass.RUNNING,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:fridge-variant",
    ),
    "extraCavity/cloneTargetTemperatureMode": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "type": "number",
            "values": {"FREEZER": {}, "OFF": {}},
        },
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:fridge-variant",
        value_mapping={
            0: "OFF",
            2: "FREEZER",
        },
    ),
    "extraCavity/doorState": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "string",
            "values": {"CLOSED": {}, "OPEN": {}},
        },
        device_class=BinarySensorDeviceClass.DOOR,
        unit=None,
        entity_category=None,
        entity_icon="mdi:fridge-variant",
    ),
    "extraCavity/fanState": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "number",
            "values": {"OFF": {}, "ON": {}},
        },
        device_class=BinarySensorDeviceClass.RUNNING,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:fridge-variant",
        state_invert=True,
        entity_registry_enabled_default=False,
    ),
    "extraCavity/temperatureAdjustingState": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "number",
            "values": {"DOWN": {}, "NONE": {}, "UP": {}},
        },
        device_class=SensorDeviceClass.ENUM,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:fridge-variant",
        value_mapping={
            1: "DOWN",
            0: "NONE",
            2: "UP",
        },
        entity_registry_enabled_default=False,
    ),
    "extraCavity/targetTemperatureC": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "type": "temperature",
            "values": {"-2.0": {}, "0.0": {}, "3.0": {}, "7.0": {}},
        },
        device_class=None,  # cannot set device class on select entity
        unit=UnitOfTemperature.CELSIUS,
        entity_category=None,
        entity_icon="mdi:thermometer",
        value_mapping={
            -0.5: "-2.0",
            0.5: "0.0",
            3.5: "3.0",
        },
    ),
    "freezer/alerts": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "alert",
            "values": {
                "AIR_SENSOR_BROKEN": {},
                "AIR_SENSOR_OPEN_CIRCUIT": {},
                "AIR_SENSOR_SHORT_CIRCUIT": {},
                "DEFROST_SENSOR_BROKEN": {},
                "DEFROST_SENSOR_OPEN_CIRCUIT": {},
                "DEFROST_SENSOR_SHORT_CIRCUIT": {},
                "DOOR_ALARM": {},
                "TEMPERATURE_ALARM": {},
            },
        },
        device_class=None,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:alert",
    ),
    "freezer/applianceState": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "string",
            "values": {"OFF": {}, "RUNNING": {}},
        },
        device_class=BinarySensorDeviceClass.RUNNING,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:fridge-variant",
    ),
    "freezer/doorState": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "string",
            "values": {"CLOSED": {}, "OPEN": {}},
        },
        device_class=BinarySensorDeviceClass.DOOR,
        unit=None,
        entity_category=None,
        entity_icon="mdi:fridge-variant",
    ),
    "freezer/fastMode": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "type": "string",
            "values": {"OFF": {}, "ON": {}},
        },
        device_class=SwitchDeviceClass.SWITCH,
        unit=None,
        entity_category=None,
        entity_icon="mdi:fridge-variant",
    ),
    "freezer/fastModeTimeToEnd": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:fridge-variant",
    ),
    "freezer/targetTemperatureC": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "default": -18.0,
            "max": -13.0,
            "min": -23.0,
            "step": 1.0,
            "type": "temperature",
        },
        device_class=NumberDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
        entity_category=None,
        entity_icon="mdi:thermometer",
    ),
    "fridge/alerts": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "alert",
            "values": {
                "AIR_SENSOR_BROKEN": {},
                "AIR_SENSOR_OPEN_CIRCUIT": {},
                "AIR_SENSOR_SHORT_CIRCUIT": {},
                "DEFROST_SENSOR_BROKEN": {},
                "DEFROST_SENSOR_OPEN_CIRCUIT": {},
                "DEFROST_SENSOR_SHORT_CIRCUIT": {},
                "DOOR_ALARM": {},
                "TEMPERATURE_ALARM": {},
            },
        },
        device_class=None,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:alert",
    ),
    "fridge/applianceState": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "string",
            "values": {"OFF": {}, "RUNNING": {}},
        },
        device_class=BinarySensorDeviceClass.RUNNING,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:fridge-variant",
    ),
    "fridge/doorState": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "string",
            "values": {"CLOSED": {}, "OPEN": {}},
        },
        device_class=BinarySensorDeviceClass.DOOR,
        unit=None,
        entity_category=None,
        entity_icon="mdi:fridge-variant",
    ),
    "fridge/fastMode": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "type": "string",
            "values": {"OFF": {}, "ON": {}},
        },
        device_class=SwitchDeviceClass.SWITCH,
        unit=None,
        entity_category=None,
        entity_icon="mdi:fridge-variant",
    ),
    "fridge/fastModeTimeToEnd": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:fridge-variant",
    ),
    "fridge/targetTemperatureC": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "default": -18.0,
            "max": -13.0,
            "min": -23.0,
            "step": 1.0,
            "type": "temperature",
        },
        device_class=NumberDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
        entity_category=None,
        entity_icon="mdi:thermometer",
    ),
    "iceMaker/alerts": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "alert",
            "values": {
                "AIR_SENSOR_BROKEN": {},
                "AIR_SENSOR_OPEN_CIRCUIT": {},
                "AIR_SENSOR_SHORT_CIRCUIT": {},
                "DEFROST_SENSOR_BROKEN": {},
                "DEFROST_SENSOR_OPEN_CIRCUIT": {},
                "DEFROST_SENSOR_SHORT_CIRCUIT": {},
            },
        },
        device_class=None,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:alert",
    ),
    "iceMaker/applianceState": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "string",
            "values": {"OFF": {}, "RUNNING": {}},
        },
        device_class=BinarySensorDeviceClass.RUNNING,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:snowflake",
        entity_registry_enabled_default=False,  # sister entity for iceMaker/executeCommand
    ),
    "iceMaker/defrostTemperatureC": ElectroluxDevice(
        capability_info={"access": "read", "type": "temperature"},
        device_class=SensorDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:snowflake",
    ),
    "iceMaker/defrostTemperatureF": ElectroluxDevice(
        capability_info={"access": "read", "type": "temperature"},
        device_class=SensorDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.FAHRENHEIT,
        entity_category=None,
        entity_icon="mdi:snowflake",
    ),
    "iceMaker/evaporatorFanState": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=BinarySensorDeviceClass.RUNNING,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:snowflake",
        entity_registry_enabled_default=False,
    ),
    "iceMaker/executeCommand": ElectroluxDevice(
        capability_info={
            "access": "write",
            "type": "string",
            "values": {
                "OFF": {},
                "ON": {},
            },
        },
        device_class=SwitchDeviceClass.SWITCH,
        unit=None,
        entity_category=None,
        entity_icon="mdi:snowflake",
        friendly_name="Ice Maker",
        state_mapping="iceMaker/applianceState",
    ),
    "iceMaker/iceDispenserState": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.ENUM,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:snowflake",
        value_mapping={
            0: "Water",
            1: "Cubes",
            2: "Dispensing Cubes",
            4: "Crushed",
            5: "Dispensing Crushed",
        },
    ),
    "iceMaker/iceTrayWaterFillSetting": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "number",
            "values": {
                "LOW_PRESSURE": {},
                "NORMAL_PRESSURE": {},
                "VERY_HIGH_PRESSURE": {},
                "VERY_LOW_PRESSURE": {},
            },
        },
        device_class=SensorDeviceClass.ENUM,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:snowflake",
        value_mapping={
            0: "LOW_PRESSURE",
            1: "NORMAL_PRESSURE",
            2: "VERY_HIGH_PRESSURE",
            3: "VERY_LOW_PRESSURE",
        },
    ),
    "networkInterface/linkQualityIndicator": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "string",
            "values": {
                "EXCELLENT": {},
                "GOOD": {},
                "POOR": {},
                "UNDEFINED": {},
                "VERY_GOOD": {},
                "VERY_POOR": {},
            },
        },
        device_class=None,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:wifi",
        entity_registry_enabled_default=False,
    ),
    "ovenProcessIdentifier": ElectroluxDevice(
        capability_info={"access": "read", "type": "string"},
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:application-settings-outline",
    ),
    "preWashPhase": ElectroluxDevice(
        capability_info={"access": "read", "type": "boolean"},
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:washing-machine",
    ),
    "reminderTime": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "default": 1200,
            "max": 2700,
            "min": 1200,
            "step": 60,
            "type": "number",
        },
        device_class=SensorDeviceClass.DURATION,  # Force Sensor as entity is non-editable
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:timelapse",
        entity_registry_enabled_default=False,
    ),
    "remoteControl": ElectroluxDevice(
        capability_info={"access": "read", "type": "string"},
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:remote",
    ),
    "runningTime": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:timelapse",
    ),
    "sensorHumidity": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.HUMIDITY,
        unit=PERCENTAGE,
        entity_category=None,
        entity_icon="mdi:water-opacity",
        friendly_name="Humidity",
    ),
    "sensorTemperature": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:thermometer",
    ),
    "startTime": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "type": "number",
            "max": 72000,
            "min": 0,
            "step": 1800,
        },
        device_class=None,
        unit=UnitOfTime.SECONDS,
        entity_category=None,
        entity_icon="mdi:clock-start",
    ),
    "targetMicrowavePower": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.ENERGY,
        unit=UnitOfPower.WATT,
        entity_category=None,
        entity_icon="mdi:microwave",
    ),
    "targetTemperatureC": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "type": "number",
            "max": 300.0,
            "min": 0,
            "step": 5.0,
        },
        device_class=SensorDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.CELSIUS,
        entity_category=None,
        entity_icon="mdi:thermometer",
    ),
    "targetTemperatureF": ElectroluxDevice(
        # capability_info={
        #     "access": "readwrite",
        #     "type": "number",
        #     "max": 300.0,
        #     "min": 0,
        #     "step": 5.0,
        # },
        device_class=SensorDeviceClass.TEMPERATURE,
        unit=UnitOfTemperature.FAHRENHEIT,
        entity_category=None,
        entity_icon="mdi:thermometer",
    ),
    "timeToEnd": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:av-timer",
    ),
    "totalCycleCounter": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=None,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:counter",
    ),
    "totalWashingTime": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:washing-machine",
    ),
    "uiLockMode": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "type": "boolean",
            "values": {"OFF": {}, "ON": {}},
        },
        device_class=SwitchDeviceClass.SWITCH,
        unit=None,
        entity_category=None,
        entity_icon="mdi:lock",
    ),
    "ui2LockMode": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "type": "boolean",
            "values": {"OFF": {}, "ON": {}},
        },
        device_class=SwitchDeviceClass.SWITCH,
        unit=None,
        entity_category=None,
        entity_icon="mdi:lock",
    ),
    "userSelections/analogSpinSpeed": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "type": "string",
            "values": {
                "0_RPM": {},
                "1000_RPM": {},
                "1200_RPM": {},
                "1400_RPM": {},
                "1600_RPM": {},
                "400_RPM": {},
                "600_RPM": {},
                "800_RPM": {},
                "DISABLED": {"disabled": True},
            },
        },
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:speedometer",
    ),
    "userSelections/analogTemperature": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "type": "string",
            "values": {
                "20_CELSIUS": {},
                "30_CELSIUS": {},
                "40_CELSIUS": {},
                "50_CELSIUS": {},
                "60_CELSIUS": {},
                "90_CELSIUS": {},
                "95_CELSIUS": {},
                "COLD": {},
            },
        },
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:thermometer",
    ),
    "userSelections/programUID": ElectroluxDevice(
        capability_info={"access": "read", "type": "string"},
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:application-settings-outline",
    ),
    "userSelections/steamValue": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "string",
            "values": {
                "STEAM_MAX": {},
                "STEAM_MED": {},
                "STEAM_MIN": {},
                "STEAM_OFF": {},
            },
        },
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:pot-steam",
    ),
    "vacationHolidayMode": ElectroluxDevice(
        capability_info={
            "access": "readwrite",
            "type": "boolean",
            "values": {"OFF": {}, "ON": {}},
        },
        device_class=SwitchDeviceClass.SWITCH,
        unit=None,
        entity_category=None,
        entity_icon="mdi:home",
    ),
    "waterFilterFlow": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.WATER,
        unit=UnitOfVolume.LITERS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:cup-water",
    ),
    "waterFilterFlowBuyThreshold": ElectroluxDevice(
        capability_info={"access": "constant", "default": 354, "type": "number"},
        device_class=SensorDeviceClass.WATER,
        unit=UnitOfVolume.LITERS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:cup-water",
        entity_registry_enabled_default=False,
    ),
    "waterFilterFlowChangeThreshold": ElectroluxDevice(
        capability_info={"access": "constant", "default": 473, "type": "number"},
        device_class=SensorDeviceClass.WATER,
        unit=UnitOfVolume.LITERS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:cup-water",
        entity_registry_enabled_default=False,
    ),
    "waterFilterLifeTime": ElectroluxDevice(
        capability_info={"access": "read", "type": "number"},
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:water",
        entity_registry_enabled_default=False,
    ),
    "waterFilterLifeTimeBuyThreshold": ElectroluxDevice(
        capability_info={"access": "constant", "default": 12960000, "type": "number"},
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:water",
        entity_registry_enabled_default=False,
    ),
    "waterFilterLifeTimeChangeThreshold": ElectroluxDevice(
        capability_info={"access": "constant", "default": 15811200, "type": "number"},
        device_class=SensorDeviceClass.DURATION,
        unit=UnitOfTime.SECONDS,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:water",
        entity_registry_enabled_default=False,
    ),
    "waterFilterState": ElectroluxDevice(
        capability_info={
            "access": "read",
            "type": "number",
            "values": {"BUY": {}, "CHANGE": {}, "CLEAN": {}, "GOOD": {}},
        },
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:water",
    ),
    "waterFilterStateReset": ElectroluxDevice(
        capability_info={
            "access": "write",
            "type": "string",
            "values": {"RESET": {}},
        },
        device_class=ButtonDeviceClass.RESTART,
        unit=None,
        entity_category=EntityCategory.CONFIG,
        entity_icon="mdi:water",
    ),
    "waterHardness": ElectroluxDevice(
        capability_info={"access": "read", "type": "string"},
        device_class=None,
        unit=None,
        entity_category=EntityCategory.DIAGNOSTIC,
        entity_icon="mdi:water",
    ),
    "waterSoftenerMode": ElectroluxDevice(
        capability_info={"access": "read", "type": "string"},
        device_class=None,
        unit=None,
        entity_category=None,
        entity_icon="mdi:water",
    ),
}

# Icon mappings for default executeCommands
icon_mapping = {
    "OFF": "mdi:power-off",
    "ON": "mdi:power-on",
    "START": "mdi:play",
    "STOPRESET": "mdi:stop",
    "PAUSE": "mdi:pause",
    "RESUME": "mdi:play-pause",
}

# List of supported Mobile App languages
# refer to https://emea-production.api.electrolux.net/masterdata-service/api/v1/languages
languages = {
    "български": "bul",
    "český": "ces",
    "Dansk": "dan",
    "Deutsch": "deu",
    "ελληνικός": "ell",
    "English": "eng",
    "eesti": "est",
    "Soome": "fin",
    "Français": "fra",
    "Hrvatski": "hrv",
    "magyar": "hun",
    "Italiano": "ita",
    "lettone": "lav",
    "lituano": "lit",
    "Luxembourgish": "ltz",
    "nederlands": "nld",
    "Norsk": "nor",
    "Polski": "pol",
    "Português": "por",
    "Română": "ron",
    "rusesc": "rus",
    "slovenský": "slk",
    "slovinský": "slv",
    "Español": "spa",
    "Svenska": "swe",
    "Türk": "tur",
    "Ukrayna": "ukr",
}
