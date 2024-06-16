# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.scripts.main import VERSION
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration, RectDecoration
#from random import randint

mod = "mod4"
terminal = "kitty"
browser = 'firefox'
discord = '󰙯'
spotify = ''

### colors ###
background = '#1e2127' 
foreground = '#abb2bf'
black = '#32344a'
red = '#f7768e'
green = '#6ece6a' 
yellow = '#e0af68'
blue = '#7aa2f7'
magenta = '#ad8ee6'
cyan = '#449dab'
white = '#787c99'

### Shortcuts ###

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    ### Switch between windows ###
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "tab", lazy.layout.next(), desc="Move window focus to other window"),
    
    ### Move windows ###
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    
    ### Grow windows ###
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    
    ### Rofi ###
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Run rofi applications"),
    Key([mod, "control"], "space", lazy.spawn("rofi -show run"), desc="Run rofi"),

    ### Browser shortcuts ###
    Key([mod], "b", lazy.spawn(browser), desc='Open browser'),
    Key([mod], "m", lazy.spawn(f'{browser} -new-window https://www.monkeytype.com -P \"profile2\"'), desc='Typing test'),
    Key([mod], "y", lazy.spawn(f'{browser} -new-window https://vid.puffyan.us/feed/popular -P \"profile2\"'), desc='Youtube'),
    
    ### Volume Controls ###
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-"), desc="Lower Volume by 5%"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+"), desc="Raise Volume by 5%"),
    Key([], "XF86AudioMute", lazy.spawn("amixer sset Master 1+ toggle"), desc="Mute/Unmute Volume"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"), 
    
    ### Other shortcuts ###
    Key([mod], "z", lazy.spawn('rofi -show power-menu -modi power-menu:~/.config/rofi/rofi-power-menu'), desc="Power menu"),
    Key([mod], "x", lazy.spawn('betterlockscreen -l'), desc='Lockscreen'),
    Key([mod, "control"], "b", lazy.spawn(os.path.expanduser("~/.config/nitrogen/cycledesktop")), desc="Change background"), 

]

### Groups ###

groups = [Group(i) for i in "123456"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )


### Layouts ###

layout_theme = {"border_focus":white,
                "border_normal":black,
                "border_width":2,
                "margin":8,
                }

layouts = [
    layout.MonadTall(**layout_theme),
]

floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

### Widgets ###

widget_defaults = dict(
    font="JetBrainsMono NF",
    fontsize=16,
    padding=8,
)
extension_defaults = widget_defaults.copy()

powerline = {
        'decorations': [
            PowerLineDecoration(path='arrow_right')
        ]
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(linewidth=0, padding=6),    
                widget.GroupBox(
                    highlight_method='line',
                    highlight_color=['111111', '282828'],
                    inactive='505050',
                    this_current_screen_border=blue,
                    disable_drag=True,
                ), 
                #right_arrow(yellow, background),
                widget.CurrentLayout(
                    #background=yellow, 
                    decorations=[
                        RectDecoration(
                            colour=yellow,
                            radius=10,
                            filled=True,
                            padding_y=1,
                        )
                    ]),
                #right_arrow(background, yellow),
                widget.WindowName(),
                widget.Systray(),
                widget.Sep(linewidth=0, padding=6, **powerline),
                #left_arrow(background, red),
                widget.CPU(format=' {load_percent}%', background=red, **powerline),
                #left_arrow(red, magenta),
                widget.Memory(format=' {MemPercent}%', background=magenta, **powerline),
                #left_arrow(magenta, green),
                widget.Net(format='{down}  {up}', background=green, **powerline),
                #left_arrow(green, cyan),
                widget.Clock(format="  %A %B %d - %H:%M", background=cyan, **powerline),
                #left_arrow(cyan, background),
                widget.TextBox(
                    text='',
                    background=background,
                    foreground=blue,
                    fontsize=20,
                    mouse_callbacks={'Button1': lazy.spawn('rofi -show power-menu -modi power-menu:~/.config/rofi/rofi-power-menu')},
                ),
                widget.Sep(linewidth=0, padding=8),
            ],
            30,
            background=background,
            foreground=foreground,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = f"Qtile {VERSION}"
