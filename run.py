import os
import sys
import traceback

from loguru import logger

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
    logger.remove()

    logger.add(
        # console
        sink=sys.stderr,
        level=config.logger_level,
        format=config.logger_format
    )

    logger.add(
        sink=os.path.join(config.logger_directory, config.logger_filename),
        level=config.logger_level,
        format=config.logger_format,
        rotation=config.logger_rotation,
        compression=config.logger_compression
    )


if __name__ == '__main__':
    try:
        config_logger(config=get_logger_config())
        logger.info('Poehyli! @Gagarin')
    except KeyboardInterrupt as interrupt:
        logger.error(interrupt)
    except Exception as error:
        logger.error(error)
        # смотрим ошибки
        logger.error(traceback.format_exc(limit=None, chain=True))
