`pynotifier`: convenience library for developing scripts that send notifications
=================================================================================

This library lets you quickly and easily develop scripts that send you
notifications, statistics or some other data.

It has two basic modes of output: printing on the console and sending emails,
but you are free to add more.


Basic usage
------------

Here is the most basic notification script:

**test.py**

~~~~~~~~~~~~~~~~Python
#!/usr/bin/env python3

from notifier import init


n = init()
with n:
    n.subject = 'Test'
    print('Hello world!')
n.notify()
~~~~~~~~~~~~~~~~~~~~~~~

Let's run it:

~~~~~~~~~~~ShellSession
$ ./test.py
[Test]

Hello world!
~~~~~~~~~~~~

Great! But notifications printed to the console are not that useful.
We can do better.

~~~~~~~~~~~~~~~~~ShellSession
$ ./test.py email
Unknown provider. Known providers are: print
~~~~~~~~~~~~~~~~~

Hmm... Looks like we need some extra setup to send emails.

**test.py**

~~~~~~~~~~~~~~~Python
#!/usr/bin/env python3

from notifier import init
from notifier.providers import EmailNotify


n = init(email=EmailNotify())
with n:
    n.subject = 'Test'
    print('Hello world!')
n.notify()
~~~~~~~~~~~~~~~~~~~

Let's run it!

~~~~~~~~~~~~~~~~~~~~ShellSession
$ ./test.py email
Traceback (most recent call last):
  File "./test.py", line 7, in <module>
    n = init(email=EmailNotify())
  File "/home/kirrun/dev/pynotifier/notifier/providers/email.py", line 25, in __init__
    .format(xdgb.save_config_path('notifier')))
ValueError: No email addresses (defaults are read from /home/kirrun/.config/notifier/addresses, one address per line)
~~~~~~~~~~~~~~~~~~~~

Ah! It doesn't know where to send the email!
As the error suggests, you can put a list of default addresses to `$XDG_CONFIG_HOME/notifier/addresses`,
but for now we'll do something different.

**test.py**

~~~~~~~~~~~~~~~Python
#!/usr/bin/env python3

from notifier import init
from notifier.providers import EmailNotify


n = init(email=EmailNotify(addresses='kirelagin@gmail.com'))
with n:
    n.subject = 'Test'
    print('Hello world!')
n.notify()
~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~ShellSession
$ ./test.py email
~~~~~~~~~~~~

Yeah!

![Notification email](https://raw.githubusercontent.com/kirelagin/pynotifier/gh-pages/notifier1.png)

As you probably noticed, the script actually didn't print anything on your screen. That is,
_all_ the output (going to `stdout`) is redirected.


More cool stuff
----------------

First of all, let's set default email so that we don't have to repeat it in every single script:

~~~~~~~~ShellSession
$ echo kirelagin@gmail.com > ~/.config/notifier/addresses
~~~~~~~~

We've already seen `addresses` parameter of `EmailNotify` in action which we set to a string
representing an email address, but it can also be a list of strings.
There is another one parameter, `sender`, that lets you adjust, well, the `From:` field of the message.

Let me also explain the `init` function. You give it a list of named notification providers,
it reads the first commandline argument, matches it against known providers,
and uses the one that matched. By the way, the default provider is called `print`
and it is always implicitly added to the list if you haven't provided it.

The following script will send an email with a custom sender name by default
instead of printing.

**test2.py**

~~~~~~~~~~~~~Python
#!/usr/bin/env python3

from notifier import init
from notifier.providers import EmailNotify


n = init(print=EmailNotify('Tester'))
with n:
    n.subject = 'Test'
    print('Hello world!')
n.notify()
~~~~~~~~~~~~~~~~~~~~

~~~~~~~~ShellSession
$ ./test2.py
~~~~~~~~~~

![Notification email](https://raw.githubusercontent.com/kirelagin/pynotifier/gh-pages/notifier2.png)


Custom notification providers
------------------------------

* Use `notifier.provider.Provider` as a base class
* and provide `notify(self)` that reads `self.subject` and `self.text`.
* See `PrintNotify` and `EmailNotify` for reference.
* Don't forget to pass your custom provider to `init`!


Requirements
-------------

* [pyxdg](https://freedesktop.org/www/Software/pyxdg/) for configuration (optional, used only to read defaults)
