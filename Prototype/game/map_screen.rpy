# Đăng ký dữ liệu các địa điểm trên bản đồ
init python:
    # Cấu trúc: [ id, Tên hiển thị, Tên file icon, Tọa độ X, Tọa độ Y, Chiều dài đường kẻ dọc ]
    # Lưu ý: Tọa độ (X, Y) ở đây là "Điểm Đích" nơi đường kẻ ghim vào bản đồ.
    # Hệ thống sẽ tự động đẩy nút bấm lên phía trên dựa theo chiều dài đường kẻ (line).
    
    map_locations = [
        {"id": "harbor_town", "name": "Harbor Town", "icon": "icon_house", "x": 152, "y": 180, "line": 50},
        {"id": "riverside", "name": "Riverside District", "icon": "icon_wave", "x": 472, "y": 140, "line": 40},
        {"id": "wind_farm", "name": "Wind Farm", "icon": "icon_wind", "x": 830, "y": 140, "line": 30},
        {"id": "bridge", "name": "Bridge", "icon": "icon_bridge", "x": 284, "y": 260, "line": 60},
        {"id": "hillside", "name": "Hillside Villas", "icon": "icon_villa", "x": 428, "y": 300, "line": 70},
        {"id": "industrial", "name": "Industrial Area", "icon": "icon_factory", "x": 673, "y": 240, "line": 40},
        {"id": "seaport", "name": "Seaport", "icon": "icon_anchor", "x": 63, "y": 410, "line": 140},
        {"id": "central_park", "name": "Central Park", "icon": "icon_tree", "x": 508, "y": 420, "line": 50},
        {"id": "lakeside", "name": "Lakeside Towers", "icon": "icon_building", "x": 725, "y": 440, "line": 80},
        {"id": "uptown", "name": "Uptown", "icon": "icon_skyscrapers", "x": 243, "y": 580, "line": 150},
        {"id": "power_plant", "name": "Power Plant", "icon": "icon_lightning", "x": 915, "y": 490, "line": 50},
        {"id": "downtown", "name": "Downtown", "icon": "icon_court", "x": 462, "y": 620, "line": 60},
        {"id": "city_hall", "name": "City Hall", "icon": "icon_city_hall", "x": 630, "y": 660, "line": 60},
        {"id": "boardwalk", "name": "Boardwalk", "icon": "icon_ferris", "x": 172, "y": 820, "line": 60},
        {"id": "stadium", "name": "Stadium", "icon": "icon_soccer", "x": 532, "y": 790, "line": 80},
        {"id": "suburbs", "name": "Suburbs", "icon": "icon_suburb", "x": 828, "y": 760, "line": 70},
        {"id": "mall", "name": "Mall", "icon": "icon_mall", "x": 434, "y": 910, "line": 80},
        {"id": "university", "name": "University", "icon": "icon_university", "x": 692, "y": 890, "line": 70}
    ]

# Định nghĩa các Style để tối ưu giao diện giống ảnh mẫu
style map_label_text:
    font "gui/font/Roboto-Regular.ttf" # Bạn có thể thay bằng font Sans-serif bất kỳ
    size 16
    color "#ffffff"
    outlines [ (1, "#000000aa", 0, 0) ]

style map_label_button:
    # Sử dụng Frame để kéo giãn ảnh nền bo tròn góc mà không bị vỡ hình
    background Frame("gui/map/label_bg.png", 10, 10) 
    hover_background Frame("gui/map/label_bg_hover.png", 10, 10)
    padding (12, 6, 12, 6)
    xpos 0.5
    anchor (0.5, 0.5)

# SCREEN CHÍNH
screen map_screen():
    tag menu
    
    # 1. Ảnh nền bản đồ thành phố ban đêm
    add "gui/map/map_background.png"
    
    # 2. Vòng lặp tự động tạo các Point of Interest (POI)
    for loc in map_locations:
        
        # Tạo một khối vbox định vị ngay tại điểm ghim trên bản đồ
        vbox:
            xpos loc["x"]
            ypos loc["y"]
            xanchor 0.5
            yanchor 1.0 # Trục Y neo ở đáy giúp đường kẻ kéo ngược lên trên nút bấm
            spacing 0
            
            # Khối 1: Nút bấm (Label + Icon)
            button:
                style "map_label_button"
                action Jump(loc["id"] + "_clicked") # Nhảy đến label cốt truyện tương ứng
                
                hbox:
                    spacing 8
                    yalign 0.5
                    # Thêm Icon địa điểm
                    add "gui/map/icons/" + loc["icon"] + ".png" yalign 0.5
                    # Thêm chữ
                    text loc["name"] style "map_label_text" yalign 0.5
            
            # Khối 2: Đường kẻ dọc mảnh chỉ xuống vị trí map
            frame:
                xalign 0.5
                background Solid("#ffffff66") # Màu trắng trong suốt 40%
                xsize 2                       # Độ dày đường kẻ 2 pixel
                ysize loc["line"]             # Chiều dài đường kẻ lấy từ database