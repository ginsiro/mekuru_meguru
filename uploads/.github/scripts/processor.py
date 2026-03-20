import os
import re
from PIL import Image

# 荷受け場と納品先のフォルダ設定
UPLOAD_DIR = 'uploads'
IMG_DIR = 'root/img'

def process_images():
    if not os.path.exists(UPLOAD_DIR):
        return

    # uploadsフォルダの中身を一つずつ確認
    for filename in os.listdir(UPLOAD_DIR):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            # 画像を開く
            img_path = os.path.join(UPLOAD_DIR, filename)
            img = Image.open(img_path)

            # タイトル（ファイル名）からWebPの名前を生成
            # 例: 「別府温泉.jpg」→「beppu_onsen.webp」
            base_name = os.path.splitext(filename)[0]
            new_name = f"{base_name}.webp"
            save_path = os.path.join(IMG_DIR, new_name)

            # WebPに変換して保存
            if not os.path.exists(IMG_DIR):
                os.makedirs(IMG_DIR)
            img.save(save_path, 'WEBP')
            print(f"Converted: {filename} -> {new_name}")

            # 元のファイルを削除（お掃除）
            os.remove(img_path)

if __name__ == "__main__":
    process_images()
