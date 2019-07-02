import abc

from typing import Sequence, Callable, Awaitable

from pyapp.events import AsyncEvent


class TaskQueue(abc.ABC):
    """
    Task style queue.

    Messages are delivered to the first listener to query for the next message
    eg::

                  |--> [Listener 1]
        [Sender] -|    [Listener 2]
                  |    [Listener 2]

    """
    new_message = AsyncEvent[Callable[[str], Awaitable]]()

    @abc.abstractmethod
    async def send(self, message: str):
        """
        Send a message to the task queue
        """

    @abc.abstractmethod
    async def receive(self, count: int = 1) -> Sequence[str]:
        """
        Receive a message (or messages) from the task queue
        """

    @abc.abstractmethod
    async def listen(self):
        """
        Start listening on the queue for messages
        """


class PubSubQueue(abc.ABC):
    """
    Pub/Sub style queue.

    Messages are broadcast to all subscribed listeners eg::

                  |--> [Listener 1]
        [Sender] -|--> [Listener 2]
                  |--> [Listener 3]

    """
    @abc.abstractmethod
    async def publish(self, message: str, topic: str):
        """
        Publish a message to queue
        """

    @abc.abstractmethod
    async def subscribe(self, topic: str):
        """
        Subscribe to a named topic
        """

    @abc.abstractmethod
    async def cancel_subscription(self, topic: str):
        """
        Unsubscribe from a topic
        """
