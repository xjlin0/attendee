from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(choice.name, choice.value) for choice in cls]


class GenderEnum(ChoiceEnum):
    MALE = 'male'
    FEMALE = 'female'
    UNSPECIFIED = 'unspecified'


class RecordStatusEnum(ChoiceEnum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    DELETED = 'deleted'
    ARCHIVED = 'archived'


class AttendingDivisionEnum(ChoiceEnum):
    CHINESE = 'Chinese 中文'
    ENGLISH = 'English 英文'
    CHILDREN = 'Children 兒童'
    NURSERY = 'Nursery 嬰孩'
    STAFF = 'Staff 勤務'
    OTHER = 'Other 其他'
    NONE = None
