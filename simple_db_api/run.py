#coding:utf-8
import argparse

from simple_db_api import web_app
from simple_db_api.app import define_urls


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_true', default=False)
    parser.add_argument('-p', '--port', type=int, default=7532)
    parser.add_argument('-b', '--database')
    parser.add_argument('-H', '--host', default='127.0.0.1')
    return parser.parse_args()


def configure_app(app, options):
    app.config['DB'] = options.database
    define_urls(app)


def dev_server():
    options = get_options()
    configure_app(web_app, options)
    web_app.run(debug=options.debug, port=options.port, host=options.host)


def run_server():
    options = get_options()
    configure_app(web_app, options)

    from gevent.wsgi import WSGIServer

    server = WSGIServer((options.host, options.port), web_app)
    server.serve_forever()


if __name__ == '__main__':
    run_server()
