import sys
import os
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Vte', '2.91')
from gi.repository import Gtk, Vte, GLib

class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="com.genericsoft.app", **kwargs)
        self.window = None
        self.box = None
        self.term = None

    def onDestroy(self, *args):
        print("Destroy")

    def onClick(self, widget):
        dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK, "Message")
        Gtk.Dialog.run(dialog)
        Gtk.Widget.destroy(dialog)

    def do_activate(self):
        if not self.window:
            # load glade layout
            builder = Gtk.Builder()
            builder.add_from_file("./window.glade")
            # attach window to application
            self.window = builder.get_object("window")
            self.add_window(self.window)
            # set signal handler
            builder.connect_signals(self)

            # show
            self.window.show_all()

if __name__ == "__main__":
    print("Running")
    app = Application()
    app.run(sys.argv)
