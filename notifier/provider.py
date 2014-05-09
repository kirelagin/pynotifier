import abc
import sys


class Provider(metaclass=abc.ABCMeta):
    def __init__(self):
        self._subject = None
        self._text = ''

    @property
    def subject(self):
        return self._subject
    @subject.setter
    def subject(self, s):
        self._subject = s

    @property
    def text(self):
        return self._text

    def say(self, msg='', end='\n'):
        self._text += msg + end

    def write(self, msg):
        self.say(msg, end='')

    @abc.abstractmethod
    def notify(self):
        pass


    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self
        return self

    def __exit__(self, exctype, excinst, exctb):
        sys.stdout = self._stdout
