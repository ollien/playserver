from . import configmanager

_reader = configmanager.ConfigManager(configPath = "config/")
config = _reader["config"]
