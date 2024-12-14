# plugins/time/time.py

import plugins
from plugins import *
from datetime import datetime

@plugins.register(name="Time", desc="Adds timestamp to prompt", version="1.0", author="Bard", desire_priority=990)
class TimePlugin(Plugin):
    def __init__(self):
        super().__init__()
        self.handlers[Event.ON_HANDLE_CONTEXT] = self.add_timestamp

    def add_timestamp(self, e_context: EventContext):
        context = e_context["context"]
        if context.type == ContextType.TEXT or context.type == ContextType.IMAGE_CREATE:
            try:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")  # Use UTC for consistency
                if "prompt" in context:
                    context["prompt"] = f"{timestamp}: {context['prompt']}"
                else:
                    logger.warning("[TimePlugin] 'prompt' key not found in context.")
            except Exception as e:
                logger.error(f"[TimePlugin] Error adding timestamp: {e}")
        e_context.action = EventAction.CONTINUE