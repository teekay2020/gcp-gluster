#!/usr/bin/env python
import os
import yaml
import logging
import argparse

def generate_variables(config,
                       **args):

    with open(config, 'r') as stream:
        try:
            source = yaml.load(stream)

            for resource in source['resources']:
                output = resource.copy()
                output['env'] = dict(
                    project='dummy',
                    name=resource['name'],
                    deployment=resource['name'],
                    type=resource['type']
                )

                print(yaml.dump(output, default_flow_style=False))

        except yaml.YAMLError as exc:
            print(exc.message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=('GCP Deployment Manager Jinja2 template expander tool'))

    parser.add_argument(
        '-V',
        '--verbose',
        default=False,
        action='store_true',
        help='Enable verbose logging'
    )

    parser.add_argument(
        '-D',
        '--debug',
        default=False,
        action='store_true',
        help='Enable debug logging'
    )

    parser.add_argument(
        '--config',
        required=True,
        help='Deployment manager configuration file'
    )

    # parser.add_argument(
    #     '--template',
    #     required=True,
    #     help='Input Jinja2 template file'
    # )

    args = parser.parse_args().__dict__

    # Setup logging levels based on verbosity setting
    FORMAT = '%(levelname)s: [%(filename)s/%(funcName)s] %(message)s'
    level = logging.WARNING

    # Mute certain overly verbose modules
    logging.getLogger("googleapiclient").setLevel(level)
    logging.getLogger("oauth2client").setLevel(level)

    if args['verbose']:
        level = logging.INFO

    if args['debug']:
        level = logging.DEBUG
        logging.getLogger("googleapiclient").setLevel(level)
        logging.getLogger("oauth2client").setLevel(level)

    logging.basicConfig(level=level, format=FORMAT)

    generate_variables(**args)
