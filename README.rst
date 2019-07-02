###############################
pyApp - Asyncio Message Queuing
###############################

*Let us handle the boring stuff!*

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: http://github.com/ambv/black
   :alt: Once you go Black...

This extension provides an interface to a message queue. This can be either a task
queue style or pub-sub style queue.


Installation
============

Install using *pip*::

    pip install pyApp-aiomq

Install using *pipenv*::

    pip install pyApp-aiomq


Add the `MESSAGE_QUEUE` block into your runtime settings file::

    MESSAGE_QUEUE = {
        "default": ("
            "host": "localhost",
        }
    }



Usage
=====


API
===

`pyapp_ext.smtp.get_client() -> SMTP`

    Get named `SMTP` instance.

