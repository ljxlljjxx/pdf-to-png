from PIL import Image  # PIL就是pip install pillow

def concatenate_vertical(images_path, output_path):
    images = [Image.open(path).convert("RGBA") for path in images_path]
    widths, heights = zip(*(img.size for img in images))
    
    max_width = max(widths)
    total_height = sum(heights)
    
    combined = Image.new('RGBA', (max_width, total_height), (0, 0, 0, 0))
    
    y_offset = 0
    for img in images:
        combined.paste(img, (0, y_offset), img)
        y_offset += img.height
    
    combined.save(output_path, 'PNG')

if __name__ == '__main__':
    n = int(input('一共几张png?'))
    images = [input(f'第{i+1}张') for i in range(n)]
    output_path = input('新图地址:')
    concatenate_vertical(images, output_path)
