from dataclasses import dataclass


@dataclass
class LoggerConfig:
    filename: str
    directory: str


@dataclass
class TgBotConfig:
    token: str
