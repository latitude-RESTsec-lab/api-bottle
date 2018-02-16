import bottle
import controllers.servidores as servidorController
import argparse
import logging
import json
import os

app = application = bottle.default_app()

def load_configuration(config_file):
    filename = config_file
    if not os.path.dirname(os.path.dirname(config_file)):
        filename = os.path.dirname(__file__) + "/" + config_file

    if not os.path.isfile(filename):
        logging.error("Database config file is missing")
        # TODO raise exception

    configuration = json.load(open(filename))
    return configuration


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='"API Servidor" to provide/handle employee\'s data.')
    parser.add_argument("-c", "--config", 
                            help="Database config file path", metavar="config_file")
    args = parser.parse_args()

    server_config = {}
    if args.config:
        server_config = load_configuration(args.config)
    else: 
        server_config = load_configuration(os.path.dirname(os.path.abspath(__file__)) +"/conf.json")
    servidorController.configure_params(server_config['DatabaseHost'], server_config['DatabaseName'], server_config['DatabaseUser'], server_config['DatabasePassword'])
    bottle.run(host = '127.0.0.1', port = 8000)