from PIL import Image

def extract_logo_icon(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        r, g, b, a = item
        
        # 1. Background removal: Very light/off-white pixels
        if r > 180 and g > 180 and b > 180:
            new_data.append((255, 255, 255, 0))
        # 2. Text removal: Dark gray/black pixels -> Make them transparent
        elif r < 110 and g < 110 and b < 110 and abs(r - g) < 20 and abs(g - b) < 20 and abs(r - b) < 20:
            new_data.append((255, 255, 255, 0))
        # 3. Infinity loop colorful stroke pixels: Keep them!
        else:
            new_data.append((r, g, b, 255))

    img.putdata(new_data)
    
    # Crop to the bounding box of non-transparent pixels
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    img.save(out_path, "PNG")
    print(f"Successfully extracted logo icon and saved to {out_path}")

if __name__ == "__main__":
    # Create the icon only logo
    extract_logo_icon("g:/infybytes/logo.jpg", "g:/infybytes/logo_icon.png")
