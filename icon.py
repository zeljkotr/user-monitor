from PIL import Image, ImageDraw

def napravi_ikonu():
    img = Image.new("RGB", (64, 64), color="#1a1a2e")
    draw = ImageDraw.Draw(img)
    
    # Krug
    draw.ellipse([4, 4, 60, 60], outline="#00d4ff", width=3)
    
    # Slovo M
    draw.line([16, 48, 16, 16], fill="#00d4ff", width=3)
    draw.line([16, 16, 32, 32], fill="#00d4ff", width=3)
    draw.line([32, 32, 48, 16], fill="#00d4ff", width=3)
    draw.line([48, 16, 48, 48], fill="#00d4ff", width=3)
    
    return img