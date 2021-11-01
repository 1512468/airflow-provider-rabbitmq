import pika
from airflow.hooks.base import BaseHook


class RabbitMQHook(BaseHook):

    conn_name_attr = "rabbitmq_conn_id"
    default_conn_name = "rabbitmq_default"
    conn_type = "amqp"
    hook_name = "RabbitMQ"

    @staticmethod
    def get_ui_field_behaviour():
        """Returns custom field behaviour"""
        return {
            "hidden_fields": ["schema", "extra"],
            "relabeling": {},
            "placeholders": {
                "login": "guest",
                "password": "guest",
                "port": "5672",
                "host": "localhost",
            },
        }

    def __init__(
        self,
        rabbitmq_conn_id: str = default_conn_name,
    ) -> None:
        """RabbitMQ interaction hook.

        :param rabbitmq_conn_id: 'Conn ID` of the Connection to be used to
        configure this hook, defaults to default_conn_name
        :type rabbitmq_conn_id: str, optional
        """
        super().__init__()
        self.rabbitmq_conn_id = rabbitmq_conn_id
        self._client = None

    def get_conn(self):
        """Return pika connection."""

        conn = self.get_connection(self.rabbitmq_conn_id)

        credentials = pika.PlainCredentials(conn.login, conn.password)
        parameters = pika.ConnectionParameters(conn.host, conn.port, "/", credentials)
        connection = pika.BlockingConnection(parameters)
        return connection

    def publish(self, exchange: str, routing_key: str, message: str):
        connection = self.get_conn()
        channel = connection.channel()
        channel.basic_publish(exchange, routing_key, message)
        channel.close()

    def declare_queue(self, name: str, passive: bool = False):
        connection = self.get_conn()
        channel = connection.channel()
        declaration = channel.queue_declare(name, passive)
        channel.close()
        return declaration

    def delete_queue(self, name: str):
        connection = self.get_conn()
        channel = connection.channel()
        return channel.queue_delete(name)

    def pull(self, queue: str):
        connection = self.get_conn()
        channel = connection.channel()
        method_frame, _, body = channel.basic_get(queue)
        if method_frame:
            channel.basic_ack(method_frame.delivery_tag)
            message = str(body, "utf-8")
        else:
            message = None
        channel.close()
        return message
