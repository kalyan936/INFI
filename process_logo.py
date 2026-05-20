from PIL import Image

def make_transparent(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # item is (R, G, B, A)
        r, g, b, a = item
        # If the pixel is very close to white/light gray (textured background)
        # The background in the image is textured white/off-white (typical values above 210)
        # The text is dark gray/black and the infinity stroke is colorful (high saturation or darker)
        if r > 210 and g > 210 and b > 210:
            # Make it transparent
            new_data.append((255, 255, 255, 0))
        else:
            # Keep original pixel, but we can also boost contrast or leave as is
            # Let's keep it as is
            new_data.append(item)

    img.putdata(new_data)
    
    # Let's crop it to remove empty transparent space around it
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    img.save(out_path, "PNG")
    print(f"Successfully processed logo and saved to {out_path}")

if __name__ == "__main__":
    make_transparent("g:/infybytes/logo.jpg", "g:/infybytes/logo.png")
