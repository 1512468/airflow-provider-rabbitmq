import pytest

from rabbitmq_provider.hooks.rabbitmq import RabbitMQHook
from rabbitmq_provider.sensors.rabbitmq import RabbitMQSensor


@pytest.fixture(autouse=True)
def reset_test_queue(monkeypatch):
    monkeypatch.setenv(
        "AIRFLOW_CONN_CONN_RABBITMQ", "amqp://guest:guest@localhost:5672"
    )
    hook = RabbitMQHook(rabbitmq_conn_id="conn_rabbitmq")
    hook.delete_queue("test")
    hook.declare_queue("test")
    hook.publish("", "test", "Hello World")


def test_sensor():
    sensor = RabbitMQSensor(
        task_id="sample_sensor_check", rabbitmq_conn_id="conn_rabbitmq", queue="test"
    )

    # Queue has 1 message, will be consumed and return True
    assert sensor.poke() is True
    # Queue now has no message, will return False
    assert sensor.poke() is False