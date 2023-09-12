from config import LoggerConfig
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
