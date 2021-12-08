import pika
import pytest

from rabbitmq_provider.operators.rabbitmq import RabbitMQOperator


def test_operator(monkeypatch):
    monkeypatch.setenv(
        "AIRFLOW_CONN_CONN_RABBITMQ", "amqp://guest:guest@localhost:5672"
    )

    operator = RabbitMQOperator(
        task_id="run_id",
        rabbitmq_conn_id="conn_rabbitmq",
        exchange="",
        routing_key="test",
        message="Hello world",
    )
    operator.execute(context={})


def test_bad_exchange_name(monkeypatch):
    monkeypatch.setenv(
        "AIRFLOW_CONN_CONN_RABBITMQ", "amqp://guest:guest@localhost:5672"
    )

    with pytest.raises(pika.exceptions.ChannelClosedByBroker,
                       match="""\(404, \"NOT_FOUND - no exchange \'does_not_exist\' in vhost""",):

        operator = RabbitMQOperator(
            task_id="run_id",
            rabbitmq_conn_id="conn_rabbitmq",
            exchange="does_not_exist",
            routing_key="test",
            message="Hello world",
        )
        operator.execute(context={})