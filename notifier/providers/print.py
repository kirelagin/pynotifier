from notifier.provider import Provider


class PrintNotify(Provider):
    def notify(self):
        if self.subject is not None:
            print('[{}]'.format(self.subject), end='')
            print()
            print()
        print(self.text, end='')
