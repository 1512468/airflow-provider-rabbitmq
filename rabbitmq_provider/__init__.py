def get_provider_info():
    return {
        "package-name": "airflow-provider-rabbitmq",
        "name": "RabbitMQ Airflow Provider",
        "description": "A RabbitMQ provider for Apache Airflow.",
        "hook-class-names": ["rabbitmq_provider.hooks.rabbitmq.RabbitMQHook"],
        "connection-types": [
            {
                "hook-class-name": "rabbitmq_provider.hooks.rabbitmq.RabbitMQHook",
                "connection-type": "amqp",
            }
        ],
        "versions": ["0.0.1"],
    }
