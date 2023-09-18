import os

from environs import Env

from config.classes import LoggerConfig, DataBaseConfig, TgBotConfig
from config.logging import (
    filename,
    directory,
    logger_format,
    logger_level,
    logger_rotation,
    logger_compression
)


def get_logger_config() -> LoggerConfig:
    return LoggerConfig(
        logger_filename=filename,
        logger_directory=directory,
        logger_format=logger_format,
        logger_level=logger_level,
        logger_rotation=logger_rotation,
        logger_compression=logger_compression
    )


def get_tg_bot_config() -> TgBotConfig:
    env = Env()
    env.read_env(os.path.join(os.getcwd(), '.env'))

    return TgBotConfig(
        token=env.str('TOKEN'),
        admin_ids=env.str('ADMIN_IDS').split(','),
        error_chanel_id=env.str('ERROR_CHANEL_ID').split(','),
        chanel_id=env.str('CHANEL_ID').split(','),
    )


def get_database_config() -> DataBaseConfig:
    env = Env()
    env.read_env(os.path.join(os.getcwd(), '.env'))

    return DataBaseConfig(
        db_user=env.str('DB_USER'),
        db_pass=env.str('DB_PASS'),
        db_host=env.str('DB_HOST'),
        db_port=env.str('DB_PORT'),
        db_name=env.str('DB_NAME'),
    )
