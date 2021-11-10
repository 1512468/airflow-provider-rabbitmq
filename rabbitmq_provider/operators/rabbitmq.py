from typing import Any

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

from rabbitmq_provider.hooks.rabbitmq import RabbitMQHook


class RabbitMQOperator(BaseOperator):
    """RabbitMQ operator that publishes a message with the given
    exchange, routing key, and message.

    :param exchange: the exchange to publish to
    :type exchange: str
    :param routing_key: the routing key to publish to
    :type routing_key: str
    :param message: the message to publish
    :type message: str
    :param rabbitmq_conn_id: connection that has the RabbitMQ
    connection (i.e amqp://guest:guest@localhost:5672), defaults to "rabbitmq_default"
    :type rabbitmq_conn_id: str, optional
    """

    template_fields = ["exchange", "routing_key", "message"]

    ui_color = "#ff6600"

    @apply_defaults
    def __init__(
        self,
        exchange: str,
        routing_key: str,
        message: str,
        rabbitmq_conn_id: str = "rabbitmq_default",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.exchange = exchange
        self.routing_key = routing_key
        self.message = message
        self.rabbitmq_conn_id = rabbitmq_conn_id

    def execute(self, context):
        hook = RabbitMQHook(self.rabbitmq_conn_id)
        hook.publish(self.exchange, self.routing_key, self.message)
