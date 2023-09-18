from dataclasses import dataclass


@dataclass
class LoggerConfig:
    logger_filename: str
    logger_directory: str
    logger_format: str
    logger_level: str
    logger_rotation: str
    logger_compression: str


@dataclass
class TgBotConfig:
    token: str


@dataclass
class DataBaseConfig:
    db_user: str
    db_pass: str
    db_name: str
    db_host: str
    db_port: str
