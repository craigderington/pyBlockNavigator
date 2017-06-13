# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = ''
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BLOCKS_MAIL_SUBJECT_PREFIX = ['PYBLOCKS']
    BLOCKS_MAIL_SENDER = 'PyBlocks Admin <admin@pyblocks.net>'
    BLOCKS_ADMIN = os.environ.get('PYBLOCKS_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('BLOCKS_MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('BLOCKS_MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevConfig
}
