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
    operator.execute()
