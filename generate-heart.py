import math
import json
import os

## Hàm tạo các điểm cho một trái tim với một tỷ lệ (scale) nhất định
# trái tim nhỏ đi khi scale < 1
def generate_heart_points(scale_factor):
    points = []
    step = 0.05 # Độ mịn điểm
    u = 0
    while u <= math.pi:
        v = 0
        while v <= 2 * math.pi:
           
            x = scale_factor * (math.sin(u) * (15 * math.sin(v) - 4 * math.sin(3*v)))
            y = scale_factor * (8 * math.cos(u))
            z = scale_factor * (math.sin(u) * (15 * math.cos(v) - 5 * math.cos(2*v) - 2 * math.cos(3*v) - math.cos(v)))
            
            points.append({"x": x, "y": y, "z": z})
            v += step
        u += step
    return points


scales = [1.0, 0.85, 0.70, 0.55, 0.40]

# Tạo thư mục data nếu chưa có
if not os.path.exists("data"):
    os.makedirs("data")

for i, scale in enumerate(scales):
    heart_points = generate_heart_points(scale)
    filename = f"data/heart_data_{i}.json"
    with open(filename, "w") as f:
        json.dump(heart_points, f)
    print(f"Đã tạo file {filename} với tỷ lệ {scale}")

print("Hoàn tất quá trình tạo dữ liệu.")