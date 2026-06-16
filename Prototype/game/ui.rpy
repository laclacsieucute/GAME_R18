# =========================================================
# 1. UI DÙNG CHUNG TOÀN BỘ
# =========================================================
screen ui():
    # Ẩn khi đang hiện hộp thoại HOẶC đang hiện bảng lựa chọn menu
    if not renpy.get_screen("say") and not renpy.get_screen("choice"): 
        frame:
            xpos 20
            ypos 80

            vbox:
                spacing 5
                textbutton "World Map":
                    action Jump("worldmap")
                textbutton "Phòng ngủ":
                    action Jump("phongngu")

# =========================================================
# 2. UI DI CHUYỂN TRONG NHÀ
# =========================================================
screen nha_move():
    tag di_chuyen_ui
    
    # Ẩn khi đang hiện hộp thoại HOẶC đang hiện bảng lựa chọn menu
    if not renpy.get_screen("say") and not renpy.get_screen("choice"): 
        hbox:
            xpos 20
            ypos 950
            spacing 15

            textbutton "Phòng khách":
                action [
                    SetVariable("location", 1),
                    Jump("location")
                ]

            textbutton "Phòng em gái":
                action [
                    SetVariable("location", 2),
                    Jump("location")
                ]

            textbutton "Phòng ngủ":
                action [
                    SetVariable("location", 3),
                    Jump("location")
                ]

# =========================================================
# 3. UI DI CHUYỂN Ở TRƯỜNG HỌC
# =========================================================
screen truong_move():
    tag di_chuyen_ui
    
    # Ẩn khi đang hiện hộp thoại HOẶC đang hiện bảng lựa chọn menu
    if not renpy.get_screen("say") and not renpy.get_screen("choice"): 
        hbox:
            xpos 20
            ypos 950
            spacing 15

            textbutton "Hành lang":
                action [
                    SetVariable("location", 4),
                    Jump("location")
                ]

            textbutton "Phòng học":
                action [
                    SetVariable("location", 5),
                    Jump("location")
                ]