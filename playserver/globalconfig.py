from . import configreader

_reader = configreader.ConfigReader(configPath = "../config")
config = _reader["config"]
