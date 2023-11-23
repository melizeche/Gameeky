import os

__dir__ = os.path.dirname(os.path.abspath(__file__))

from gi.repository import Gtk, GObject

from ...common.definitions import Action


@Gtk.Template(filename=os.path.join(__dir__, "actions_popup.ui"))
class ActionsPopup(Gtk.Popover):
    __gtype_name__ = "ActionsPopup"

    __gsignals__ = {
        "performed": (GObject.SignalFlags.RUN_LAST, None, (int,)),
    }

    take = Gtk.Template.Child()
    drop = Gtk.Template.Child()
    use = Gtk.Template.Child()
    interact = Gtk.Template.Child()
    idle = Gtk.Template.Child()

    @Gtk.Template.Callback("on_clicked")
    def __on_clicked(self, button: Gtk.Button) -> None:
        self.emit("performed", Action[button.props.label.upper()])
        self.popdown()
