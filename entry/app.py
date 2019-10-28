import sys
import os
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Vte', '2.91')
from gi.repository import Gtk, Vte, GLib

class AppSignalHandlers:
    def onDestroy(self, *args):
        print("Destroy")
    def onChange(self, widget):
        print("Change", widget.get_text())

class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="com.genericsoft.app", **kwargs)
        self.window = None
        self.box = None
        self.term = None
    
    def do_activate(self):
        if not self.window:
            # load glade layout
            builder = Gtk.Builder()
            builder.add_from_file("./window.glade")
            # attach window to application
            self.window = builder.get_object("window")
            self.add_window(self.window)
            # set signal handler
            builder.connect_signals(AppSignalHandlers())

            # set initial text value
            entry = builder.get_object("entry")
            entry.set_text("first")

            # show
            self.window.show_all()

if __name__ == "__main__":
    print("Running")
    app = Application()
    app.run(sys.argv)
