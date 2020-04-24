import configparser
import os


def parse_config():
    user_dir = os.getcwd()
    config_file_path = user_dir + '/settings.conf'
    if not os.path.exists(config_file_path):
        raise Exception("param.conf file not exists in the location %s" % user_dir)

    config = configparser.RawConfigParser()
    config.read(config_file_path)
    return config

