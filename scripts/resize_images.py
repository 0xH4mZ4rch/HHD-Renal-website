import os
from PIL import Image

SRC = r"C:\Users\Hxmza-pc\Desktop\HDD\hhdrenal-original-images"
DST = r"C:\Users\Hxmza-pc\Desktop\HDD\hhd-renal-website\images"

# (filename, max_width, quality)
JOBS = [
    ("adult-students.jpg", 1600, 78),
    ("certifications.jpg", 1600, 78),
    ("dialysis-4.jpg", 1600, 78),
    ("dialysis-machine.jpeg", 1600, 78),
    ("dialysis-recliners.jpg", 1600, 78),
    ("hemo-patient.jpg", 1600, 78),
    ("reverse-osmosis-1.jpg", 1600, 78),
    ("reverse-osmosis-dialysis.jpg", 1600, 78),
    ("reverse-osmosis.jpg", 1600, 78),
]

os.makedirs(DST, exist_ok=True)

for name, max_w, quality in JOBS:
    src_path = os.path.join(SRC, name)
    base, _ = os.path.splitext(name)
    out_name = base + ".jpg"
    dst_path = os.path.join(DST, out_name)

    img = Image.open(src_path)
    img = img.convert("RGB")
    w, h = img.size
    if w > max_w:
        new_h = round(h * (max_w / w))
        img = img.resize((max_w, new_h), Image.LANCZOS)
    img.save(dst_path, "JPEG", quality=quality, optimize=True, progressive=True)

    orig_size = os.path.getsize(src_path)
    new_size = os.path.getsize(dst_path)
    print(f"{name}: {orig_size/1024:.0f}KB -> {out_name}: {new_size/1024:.0f}KB ({img.size[0]}x{img.size[1]})")
