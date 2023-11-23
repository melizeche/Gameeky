import os

__dir__ = os.path.dirname(os.path.abspath(__file__))

from typing import Optional
from gi.repository import Gtk, Gdk, Adw

from .scene import Scene as SceneWidget
from .hud import Hud as HudWidget
from .highlight import Highlight as HighlightWidget
from .actions_popup import ActionsPopup

from ...client.game.scene import Scene as SceneModel
from ...client.game.stats import Stats as StatsModel


@Gtk.Template(filename=os.path.join(__dir__, "window.ui"))
class Window(Adw.ApplicationWindow):
    __gtype_name__ = "Window"

    stack = Gtk.Template.Child()
    overlay = Gtk.Template.Child()

    def __init__(self, *args, **kargs) -> None:
        super().__init__(*args, **kargs)
        self._scene = SceneWidget()
        self._hud = HudWidget()
        self._highlight = HighlightWidget()

        self.overlay.add_overlay(self._scene)
        self.overlay.add_overlay(self._hud)
        self.overlay.add_overlay(self._highlight)

        self._popup = ActionsPopup()
        self._popup.set_parent(self.canvas)

    def switch_to_loading(self) -> None:
        self.stack.set_visible_child_name("loading")

    def switch_to_failed(self) -> None:
        self._scene.model = None
        self._hud.model = None
        self.stack.set_visible_child_name("failed")

    def switch_to_game(
        self,
        scene: Optional[SceneModel],
        stats: Optional[StatsModel],
    ) -> None:
        self._scene.model = scene
        self._hud.model = stats
        self.stack.set_visible_child_name("game")

    def display_actions(self, x: int, y: int) -> None:
        self._popup.set_pointing_to(Gdk.Rectangle(x, y, 0, 0))
        self._popup.set_offset(x, y)
        self._popup.popup()

    @property
    def canvas(self) -> Gtk.Widget:
        return self._highlight.canvas

    @property
    def popover(self) -> ActionsPopup:
        return self._popup
