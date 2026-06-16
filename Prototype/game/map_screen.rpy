label worldmap:
    hide screen nha_move
    hide screen truong_move
    call screen worldmap
    return


screen worldmap():

    add "bg map.png"

    textbutton "Nhà":
        xpos 500
        ypos 500
        action Jump("phongkhach")

    textbutton "Trường":
        xpos 1100
        ypos 300
        action Jump("hanhlang")