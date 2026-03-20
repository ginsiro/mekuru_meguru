import os
from PIL import Image

# フォルダの設定
UPLOAD_DIR = 'uploads'
OUTPUT_DIR = 'root/img'

def process():
    # フォルダを強制的に作成し、中に目印のファイルを作る
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, '.gitkeep'), 'w') as f:
        f.write('') # 空のファイルを作る

    if not os.path.exists(UPLOAD_DIR):
        return

    for filename in os.listdir(UPLOAD_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(UPLOAD_DIR, filename)
            
            # WebPとして保存
            base_name = os.path.splitext(filename)[0]
            save_path = os.path.join(OUTPUT_DIR, f"{base_name}.webp")
            
            with Image.open(img_path) as img:
                img.save(save_path, 'WEBP')
            
            os.remove(img_path)

if __name__ == "__main__":
    process()
