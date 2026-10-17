import os
from PIL import Image, ImageDraw, ImageFont

def create_mufredat_var_logo():
    size = 1024
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. Background Squircle with Gradient
    # Outer radius 240
    margin = 48
    box = [margin, margin, size - margin, size - margin]
    
    # Draw gradient inside rounded rectangle
    # We can create a base gradient image and mask it with rounded rectangle
    base_grad = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw_grad = ImageDraw.Draw(base_grad)
    
    # Linear diagonal gradient from #6366F1 (Indigo 500) to #312E81 (Indigo 900) to #0F172A (Slate 900)
    for y in range(size):
        ratio = y / size
        # Start color (99, 102, 241) -> End color (15, 23, 42)
        r = int(99 * (1 - ratio) + 15 * ratio)
        g = int(102 * (1 - ratio) + 23 * ratio)
        b = int(241 * (1 - ratio) + 42 * ratio)
        draw_grad.line([(0, y), (size, y)], fill=(r, g, b, 255))
        
    # Mask
    mask = Image.new('L', (size, size), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.rounded_rectangle(box, radius=220, fill=255)
    
    # Composite squircle
    img.paste(base_grad, (0, 0), mask)
    
    # Draw elegant neon glowing border
    draw.rounded_rectangle(box, radius=220, outline=(129, 140, 248, 220), width=16)

    # 2. Draw Decorative Mathematical Grid / Radial Accent
    # Subtle inner circle
    center = size // 2
    draw.arc([center - 320, center - 320, center + 320, center + 320], start=0, end=360, fill=(255, 255, 255, 30), width=6)
    draw.arc([center - 400, center - 400, center + 400, center + 400], start=-30, end=210, fill=(16, 185, 129, 60), width=4)

    # 3. Draw Stylized Modern Math Emblem: "M" & "√" & "π" & Star
    # Star on top (Maarif star)
    star_x, star_y = center, center - 270
    draw.polygon([
        (star_x, star_y - 32), (star_x + 9, star_y - 9),
        (star_x + 32, star_y - 9), (star_x + 14, star_y + 6),
        (star_x + 20, star_y + 28), (star_x, star_y + 14),
        (star_x - 20, star_y + 28), (star_x - 14, star_y + 6),
        (star_x - 32, star_y - 9), (star_x - 9, star_y - 9)
    ], fill=(251, 191, 36, 255)) # Gold star

    # Stylized bold math curves:
    # A vibrant emerald root checkmark:
    check_pts = [
        (center - 320, center + 60),
        (center - 250, center + 60),
        (center - 190, center + 170),
        (center - 100, center - 180),
        (center + 310, center - 180)
    ]
    draw.line(check_pts, fill=(16, 185, 129, 240), width=32, joint='curve')

    # Stylized "M" in pure bright white with soft drop shadow
    # Points of M:
    m_left = center - 180
    m_right = center + 220
    m_top = center - 120
    m_bot = center + 240
    m_mid_x = (m_left + m_right) // 2
    
    # Shadow
    m_pts_shadow = [
        (m_left, m_bot + 8),
        (m_left, m_top + 8),
        (m_mid_x, center + 108),
        (m_right, m_top + 8),
        (m_right, m_bot + 8)
    ]
    draw.line(m_pts_shadow, fill=(15, 23, 42, 160), width=42, joint='curve')

    # Main M in white
    m_pts = [
        (m_left, m_bot),
        (m_left, m_top),
        (m_mid_x, center + 100),
        (m_right, m_top),
        (m_right, m_bot)
    ]
    draw.line(m_pts, fill=(255, 255, 255, 255), width=38, joint='curve')

    # Small Math symbols decoration inside:
    # π in cyan
    try:
        # Draw small decorative shapes or text
        pass
    except Exception:
        pass

    # Small subtitle pill at the bottom: "7. SINIF"
    pill_w, pill_h = 320, 70
    pill_box = [center - pill_w//2, size - margin - 150, center + pill_w//2, size - margin - 80]
    draw.rounded_rectangle(pill_box, radius=35, fill=(79, 70, 229, 240), outline=(199, 210, 254, 255), width=5)
    
    # Try using default font or drawing "7" and dots
    try:
        font = ImageFont.truetype("arial.ttf", 46)
        text = "7. SINIF MAT"
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((center - tw//2, pill_box[1] + (pill_h - th)//2 - 6), text, font=font, fill=(255, 255, 255, 255))
    except Exception:
        pass

    return img

if __name__ == '__main__':
    logo = create_mufredat_var_logo()
    
    # Create assets/images directory
    os.makedirs('assets/images', exist_ok=True)
    logo_path = 'assets/images/app_logo.png'
    logo.save(logo_path, format='PNG')
    print(f"Saved {logo_path}")

    # Android launcher icons paths
    sizes = {
        'android/app/src/main/res/mipmap-mdpi/ic_launcher.png': (48, 48),
        'android/app/src/main/res/mipmap-hdpi/ic_launcher.png': (72, 72),
        'android/app/src/main/res/mipmap-xhdpi/ic_launcher.png': (96, 96),
        'android/app/src/main/res/mipmap-xxhdpi/ic_launcher.png': (144, 144),
        'android/app/src/main/res/mipmap-xxxhdpi/ic_launcher.png': (192, 192),
    }

    for path, sz in sizes.items():
        os.makedirs(os.path.dirname(path), exist_ok=True)
        resized = logo.resize(sz, Image.Resampling.LANCZOS)
        resized.save(path, format='PNG')
        print(f"Saved {path} ({sz[0]}x{sz[1]})")
