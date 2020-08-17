"""Run main loop and imports all required modules."""

import yaml
import json
import flask
import logging


def main():
    """Import service and execute."""
    import service
    service.start()


if __name__ == '__main__':
    main()
