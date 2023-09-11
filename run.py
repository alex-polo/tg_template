import logging
import os.path

from config import (
    LoggerConfig,
    get_logger_config
)


def config_logger(config: LoggerConfig) -> None:
    """
    Функция выполняет конфигурацию логгера
    :param config: LoggerConfig
    :return: None
    """
    if not os.path.exists(config.directory):
        os.mkdir(config.directory)

    # logging.basicConfig()


if __name__ == '__main__':
    try:
        config_logger(config=get_logger_config())
    except KeyboardInterrupt as interrupt:
        print(interrupt)
    except Exception as error:
        print(error)
