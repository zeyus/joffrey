from registry import BasePlugin, plugin_registry


class Ping(BasePlugin):
    name = 'Ping'
    commands = {
        '!ping': 'Test your connection'
    }

    def process(self, message, sender, command=None, *args):
        if message.lower() == '!ping':
            return 'Pong!'
plugin_registry.register(Ping())
