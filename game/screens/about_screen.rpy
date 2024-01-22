## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About")):
        style_prefix "about"
        viewport id "abt":
            ypos 50
            xpos 50
            ymaximum 400
            xmaximum 850
            yfill True
            xfill True
            mousewheel True
            vbox:
                xpos 50
                ypos 50
                label "[config.name!t]"
                text _("Version [config.version!t]\n")

                ## gui.about is usually set in options.rpy.
                if gui.about:
                    text "[gui.about!t]\n"

                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
        vbar value YScrollValue("abt") xpos .75 ypos .1 ymaximum 400

        hbox:
            ypos .8
            xpos .05
            vbox:
                textbutton _("Return"): #TODO: fix all the return/main menu buttons positioning in the overlay popups
                    action Return()      

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size
