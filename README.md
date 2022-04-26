[![PyPI version](https://badge.fury.io/py/airflow-provider-rabbitmq.svg)](https://badge.fury.io/py/airflow-provider-rabbitmq)

# RabbitMQ Provider for Apache Airflow


## Configuration

In the Airflow user interface, configure a connection with the `Conn Type` set to RabbitMQ.
Configure the following fields:

- `Conn Id`: How you wish to reference this connection.
    The default value is `rabbitmq_default`.
- `login`: Login for the RabbitMQ server.
- `password`: Password for the RabbitMQ server.,
- `port`: Port for the RabbitMQ server, typically 5672.
- `host`: Host of the RabbitMQ server.
- `vhost`: The virtual host you wish to connect to.

## Modules

### RabbitMQ Operator

The `RabbitMQOperator` publishes a message to your specificed RabbitMQ server.

Import into your DAG using:

```Python
from rabbitmq_provider.operators.rabbitmq import RabbitMQOperator
```

### RabbitMQ Sensor

The `RabbitMQSensor` checks a given queue for a message. Once it has found a message
the sensor triggers downstream proccesses in your DAG.

Import into your DAG using:

```Python
from rabbitmq_provider.sensors.rabbitmq import RabbitMQSensor
```

## Testing

To run unit tests, use:

```shell
poetry run pytest .
```

A RabbitMQ instance is required to run the tests. Use the following command:

```shell
docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```
