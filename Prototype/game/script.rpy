# tạo các nhân vật sẽ có trong game
define e = Character("em gái")


#bắt đầu cảnh chính
label start:
    "các tính năng hiện có"
    "load cảnh, thoại, đưa ra các lựa chọn và up lên một nơi để có thể teamwork"
    "và Chúc mừng sinh nhật KQNhi \\(>.<)/"
label trong_nha:
    scene bg phongkhach
    menu menu_bat_dau:
        "bạn chọn đi đâu"
        "tới phòng em gái":
            jump phong_em_gai
        "ra ngoài chạm cỏ":
            jump ngoai_cua

#lệnh return để kết thúc game
#return
        


#load cảnh phòng em gái
label phong_em_gai:
    scene bg phongnguemgai
    show emgai
    with dissolve
    e "anh định làm gì ở đây vậy anh giai?"
    menu menu_phong_em_gai:
        e "anh giai muốn cùng em làm gì nào?"
        "cho mút kẹo":
            hide emgai
            play sound 'audio/suck.ogg'
            " hình ảnh anh trai cho em gái mút kẹo "
            stop sound
            jump phong_em_gai
        "rời đi":
            hide emgai
            jump trong_nha



#load cảnh ngoài cửa
label ngoai_cua:
    scene bg map
    "bạn muốn đi đâu"
    menu ra_ngoai:
        "tới trường học":
            jump truong_hoc
        "đi vào nhà":
            jump trong_nha


#load cảnh trường học
label truong_hoc:
    "đang nghỉ hè, quay về đi"
    menu:
        "về nhà":
            jump ngoai_cua

    