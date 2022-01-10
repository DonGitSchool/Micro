def on_button_pressed_ab():
    basic.show_string("Hello!")
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

basic.show_leds("""
    # # . # #
        # # . # #
        . . . . .
        # # . # #
        # # . # #
""")
basic.show_leds("""
    . # . . .
        . . # . .
        . # . . .
        . . # . .
        . # . . .
""")

def on_forever():
    basic.show_icon(IconNames.YES)
basic.forever(on_forever)
