from .base import Actuator as BaseActuator

from ....common.state import State


class Actuator(BaseActuator):
    name = "grows"
    interactable = False
    activatable = False

    def tick(self) -> None:
        if self._seconds_since_activation() <= self._entity.rate:
            return

        self._entity.state = State.DESTROYED
        self._entity.spawn()

        super().tick()