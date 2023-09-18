import os
import sys
import traceback

from loguru import logger

import tg_bot
from config import (
    LoggerConfig,
    get_logger_config, get_database_config, get_tg_bot_config, TgBotConfig, DataBaseConfig
)
from database import registry_database


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

        logger.info('loading tg_bot configuration')
        tg_bot_config: TgBotConfig = get_tg_bot_config()

        logger.info('loading DataBase configuration')
        database_config: DataBaseConfig = get_database_config()

        logger.info('registry DataBase configuration')
        registry_database(database_config=database_config)

        tg_bot.start(tg_bot_config=tg_bot_config)

    except KeyboardInterrupt as interrupt:
        logger.error(interrupt)
    except Exception as error:
        logger.error(error)
        # смотрим ошибки
        logger.error(traceback.format_exc(limit=None, chain=True))
