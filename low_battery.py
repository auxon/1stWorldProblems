from sims4communitylib.events.event_handling.common_event_registry import CommonEventRegistry
from sims4communitylib.events.zone_spin.update_tuning_event import UpdateTuningEvent
from sims4communitylib.events.zone_update.events.zone_update_event import S4CLZoneUpdateEvent
from sims4communitylib.modinfo import ModInfo
from sims4communitylib.utils.resources.common_capability_loot_actions import CommonCapabilityLootActions
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from sims4communitylib.utils.sims.common_sim_name_utils import CommonSimNameUtils

def on_low_battery_reaction(event_data: UpdateTuningEvent):
    sim_info = CommonSimUtils.get_sim_info(event_data.sim_id)
    if sim_info is not None:
        # Replace with appropriate reaction logic (e.g., change mood, play animation)
        sim_info.show_notification('Oh no! My phone is about to die!')
