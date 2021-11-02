from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

from rabbitmq_provider.hooks.rabbitmq import RabbitMQHook


class RabbitMQOperator(BaseOperator):

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
