from config import LoggerConfig
from config.logging import (
    filename,
    directory
)


def get_logger_config() -> LoggerConfig:
    return LoggerConfig(
        filename=filename,
        directory=directory
    )
