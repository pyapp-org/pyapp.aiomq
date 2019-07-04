import logging
import botocore.exceptions

from typing import Sequence
from pyapp_ext.aiobotocore import create_client

from ..import base

logger = logging.getLogger(__name__)


class MessageQueue(base.MessageQueue):
    """
    Message Queue using SQS
    """

    def __init__(self, *, name: str, aws_credentials: str = None):
        self.name = name
        self.client = create_client("SQS", credentials=aws_credentials)

        self._queue_url = None

    async def _get_queue_url(self):
        if self._queue_url:
            try:
                response = await self.client.get_queue_url(QueueName=self.name)
            except botocore.exceptions.ClientError as ex:
                if ex.response['Error']['Code'] == "AWS.SimpleQueueService.NonExistentQueue":
                    raise QueueNotFound
                else:
                    raise
            self._queue_url = response["QueueUrl"]
        return self._queue_url

    async def create(self, name):
        pass

    async def send(self, message: str):
        self.client.send_message(
            URL=self.url,
            MessageBody=message
        )

    async def receive(self, count: int = 1) -> Sequence[str]:
        self.client

    async def listen(self):
        pass


class PubSubQueue(base.PubSubQueue):
    """
    Publish-Subscribe Queue using SNS
    """
    async def publish(self, message: str, topic: str):
        pass

    async def subscribe(self, topic: str):
        pass

    async def cancel_subscription(self, topic: str):
        pass