from broadcaster import Broadcast
from eco2ai_playground.core.settings import settings

broadcaster = Broadcast(url=settings.REDIS_URL)
