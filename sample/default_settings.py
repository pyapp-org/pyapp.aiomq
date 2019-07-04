TASK_QUEUES = {
    "amqp": ("pyapp_ext.aiomq.amqp.MessageQueue", {
        "url": "http://"
    }),
    "sqs": ("pyapp_ext.aiomq.aws.MessageQueue", {
        "url": "http://"
    }),
}

PUBSUB_QUEUES = {
    "amqp": ("pyapp_ext.aiomq.amqp.PubSubQueue", {
        "url": "http://"
    }),
    "sqs": ("pyapp_ext.aiomq.aws.PubSubQueue", {
        "url": "http://"
    }),
}
