# GTK+

## Label

Simple control to show a text string.

## Image

Simple control to show an image.

## Button

Simple button with a click signal, if multiple buttons send the same signal, each button's `id` can be used to identify the sender.

## Check Button

Checkbox example, with signal when button is toggled, gets new state.

## Combo

Combo example, with signal when selection is changed, gets new selection.

Create a combo, create a tree model - define the schema ( columns, use gchararray for string ), add a row for each selectable value.  Edit the combo, and create a label, set 'text' to the id of the column to use to render in the combo drop down.

## Entry

Text entry field, set initial value, signal when value is change.

## Switch

A simple boolean toggle, set initial value, signal when state is changed.

## MenuBar

A menu bar with menus, each containing a number of items.  An activte signal is sent when one is selected.

## Spinner

An activity spinner, call start ( spinner.start() ) to make it appear and animate, call stop ( spinner.stop() ) to hide it.
