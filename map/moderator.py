from moderation import moderation
from moderation.db import ModeratedModel
from moderation.moderator import GenericModerator
from map.models import City, County, State


class ResearchModerator(GenericModerator):
    auto_approve_for_staff = False


moderation.register(City, ResearchModerator)  # Uses default moderation settings
moderation.register(County, ResearchModerator)
moderation.register(State, ResearchModerator)