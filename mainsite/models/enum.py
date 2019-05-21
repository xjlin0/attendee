from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class RecordStatusEnum(ChoiceEnum):
    ACTIVE = 'active'
    DELETED = 'deleted'
    ARCHIVED = 'archived'
