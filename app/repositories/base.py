from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Optional


class BaseRepository(ABC):
    @abstractmethod
    def delete(self, pk: int) -> None:
        pass

    @abstractmethod
    def create(self, data: Any) -> Any:
        pass

    @abstractmethod
    def get_by_id(self, pk: int) -> Optional[Any]:
        pass

    @abstractmethod
    def update(self, pk: int, data: Any) -> Any:
        pass
