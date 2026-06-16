# bắt đầu cảnh chính
label start:
    jump worldmap

# --- PHÒNG KHÁCH ---
label phongkhach:
    $ location = 1
    scene bg phongkhach
    show screen ui
    show screen nha_move
    # Khóa màn hình, chỉ cho phép tương tác với screen ui / nha_move
    $ renpy.pause(hard=True) 
label phongngu:
    hide screen nha_move
    hide screen truong_move
    $ location = 3
    scene bg phongngu
    show screen ui
    show screen nha_move
    # Khóa màn hình, chỉ cho phép tương tác với screen ui / nha_move
    $ renpy.pause(hard=True) 
# --- PHÒNG EM GÁI ---
label phongemgai:
    $ location = 2
    scene bg phongnguemgai
    show emgai
    with dissolve
    show screen emgai_hotspot
    show screen ui
    "Ấn vào cái ô đỏ ( đáng ra là làm bao quanh em gái nma tôi lười)"
    window hide dissolve # 👈 THÊM DÒNG NÀY: Ẩn thanh trắng đi một cách mượt mà
    $ renpy.pause(hard=True) 
label hanhlang:
    $ location = 4
    scene bg hanhlang
    show screen ui
    show screen truong_move
    # KHÓA TẠI ĐÂY: Người chơi click lung tung ra nền sẽ không có tác dụng, 
    # bắt buộc phải bấm trúng em gái (hotspot) hoặc nút trên screen ui.
    $ renpy.pause(hard=True) 
label phonghoc:
    $ location = 5
    scene bg phonghoc   
    show screen ui
    show screen truong_move
    $ renpy.pause(hard=True) 
# --- SCREEN HOTSPOT ---
screen emgai_hotspot():
    # Chỉ khi đang ở phòng em gái (location = 2) thì cái nút này mới xuất hiện
    if location == 2: 
        textbutton "":
            xalign 0.5
            yalign 0.65
            xsize 320
            ysize 420
            background "#ff000080" # Khối màu đỏ bạn vừa thêm lúc nãy
            action Jump("evemgai1")