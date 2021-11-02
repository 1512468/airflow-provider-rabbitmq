from airflow.sensors.base import BaseSensorOperator
from airflow.utils.decorators import apply_defaults

from rabbitmq_provider.hooks.rabbitmq import RabbitMQHook


class RabbitMQSensor(BaseSensorOperator):

    ui_color = "#ff6600"

    @apply_defaults
    def __init__(
        self, queue: str, rabbitmq_conn_id: str = "rabbitmq_default", **kwargs
    ):
        super().__init__(**kwargs)
        self.queue = queue
        self.rabbitmq_conn_id = rabbitmq_conn_id

    def poke(self, context):
        hook = RabbitMQHook(self.rabbitmq_conn_id)
        message = hook.pull(self.queue)
        if message:
            return True
        else:
            return False
