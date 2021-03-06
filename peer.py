# -*- coding: utf-8 -*-

"""
TLS peer
"""

from abc import ABCMeta, abstractmethod
import ssl
from pyssldemo import utils
from pyssldemo.ssl_logger import SSLLogger


class Peer(metaclass=ABCMeta):

    """ TLS peer on specified parameters """

    def __init__(self, context=None):
        if context is None:
            self.context = utils.create_context()
        else:
            self.context = context

        self.logger = SSLLogger(type(self).__name__)

    @staticmethod
    def get_session(self):
        """ Return current SSL session """

    @staticmethod
    def is_session_resumed(self):
        """ Check if the session is resumed """

    def set_peer_auth(self, peer_auth):
        """ Set if the peer's certificate must be verified """

        if peer_auth:
            self.context.verify_mode = ssl.CERT_REQUIRED
        else:
            self.context.verify_mode = ssl.CERT_NONE

    @staticmethod
    def set_app_protocols(self, *app_protocols):
        """ Set the supported application protocols """

    @staticmethod
    def get_app_protocol(self):
        """ Return the negotiated application protocol """

    @abstractmethod
    def close(self):
        """ Close the peer """

    def log(self, msg):
        self.logger.log(f'[{type(self).__name__}] {msg}')
