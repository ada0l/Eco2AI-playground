from eco2ai_playground.core.schemas import Pagination


def get_pagination(offset: int = 0, limit: int = 10):
    return Pagination(offset=offset, limit=limit)
