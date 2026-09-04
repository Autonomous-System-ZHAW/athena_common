"""Shared mode/mission/LED-color utilities for Athena nodes.

Single source of truth for anything derived from the SystemMode / Missions
message constants, so state_machine, led_manager, etc. don't each keep
their own copy that has to be updated in lockstep whenever a mode or
mission is added or renamed.
"""

from athena_custom_msgs_pkg.msg import SystemMode, Missions


def _build_name_map(msg_class):
    """Build {value: NAME} from the uppercase int constants of a generated
    ROS message class, e.g. SystemMode.INIT == 0 -> {0: "INIT"}.

    To add a new mode/mission, only the .msg file needs to change - this
    map (and anything derived from it) picks it up automatically the next
    time the workspace is rebuilt. No node needs to be touched.
    """
    return {
        value: name
        for name, value in vars(msg_class).items()
        if name.isupper() and isinstance(value, int)
    }


SYSTEM_MODE_NAMES = _build_name_map(SystemMode)
MISSION_NAMES = _build_name_map(Missions)

SYSTEM_MODE_COLOR_CODE = {
    SystemMode.INIT: (0, 0, 0, 255),
    SystemMode.READY: (255, 20, 0, 0),
    SystemMode.MISSION_SELECT: (255, 0, 150, 255),
    SystemMode.MANUAL_JOY: (0, 0, 255, 0),
    SystemMode.AUTONOMOUS: (0, 255, 0, 0),
    SystemMode.EMERGENCY: (255, 0, 0, 0),
    SystemMode.OFF: (0, 0, 0, 0),
}
