import random
from sims4communitylib.events.event_handling.common_event import CommonEvent
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from sims4communitylib.enums.buffs_enum import CommonBuffId
from sims4communitylib.utils.sims.common_buff_utils import CommonBuffUtils
from sims4communitylib.events.interaction.events.interaction_started import (
    S4CLInteractionStartedEvent,
)
from sims4communitylib.events.event_handling.common_event_registry import (
    CommonEventRegistry,
)
from EA.simulation.interactions.base.interaction import Interaction
from EA.simulation.objects. import Phone


class PhoneBatteryDiesEvent(S4CLInteractionStartedEvent):
    def _should_run(self, interaction: Interaction, *args, **kwargs) -> bool:
        return isinstance(interaction.target, Phone)

    def _run(self, interaction: Interaction, *args, **kwargs) -> bool:
        sim = interaction.sim
        sim_info = CommonSimUtils.get_sim_info(sim)
        # Determine if the phone's battery dies
        if random.random() < 0.1:
            # Add the custom buff to the Sim
            CommonBuffUtils.add_buff(
                sim_info=sim_info,
                buff=CommonBuffId.TRAIT_INSANE_ANGRY,
                buff_reason="Phone battery died",
            )
        return True


class FirstWorldProblemsEvent(CommonEvent):
    def _run(self, *args, **kwargs) -> bool:
        # Get the Sim from the arguments
        sim = kwargs.get("sim")

        # Notify the user that the Sim's phone battery has died
        notification_message = f"{CommonSimUtils.get_sim_name(sim)}'s phone battery has died!  1st World problems!!"
        CommonSimUtils.display_notification(notification_message)

        return True


# Register the event so it runs when an interaction starts
CommonEventRegistry.get().register_interaction_start_event(PhoneBatteryDiesEvent())
