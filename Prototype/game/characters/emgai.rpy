define e = Character("Em gái")
default emgai_love = 0
default emgai_corruption = 0
default emgai_event = 0
default emgai_location = 3
label evemgai1:
    # Ẩn ngay hotspot đi để khi đang hiện menu lựa chọn, 
    # người chơi không bấm đè lại vào em gái được nữa.
    hide screen emgai_hotspot 
    
    e "Bạn đã nhấn vào em gái và đến sự kiện evemgai1." 
    e "Anh định làm gì ở đây vậy anh giai?" 
    
    menu menuevemgai1:
        "Cho mút kẹo":
            play sound 'audio/suck.ogg'
            "Hình ảnh anh trai cho em gái mút kẹo..."
            stop sound
            jump phongemgai # Quay lại phòng, nút hotspot sẽ tự động hiện lại
        "Thôi":
            "ĐỒ NGU! ĐỒ ĂN HẠI!"
            jump phongemgai # Quay lại phòng, nút hotspot sẽ tự động hiện lại