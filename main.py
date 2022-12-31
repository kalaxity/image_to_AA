import cv2
import numpy as np

PIXEL  = 14  # フォントサイズ14pxを想定
HEIGHT = PIXEL*80
WIDTH  = PIXEL*80

# 画像縮小
def shrink_image(img): 
    return cv2.resize(img, dsize=(WIDTH, HEIGHT))

# 各パーツを文字に変換
def image_to_char(img_part):
    chars = "電気ポケモン" # ここにAAに使いたい文字を並べる。濃い文字から薄い文字の順。
    dense = np.average(img_part).astype(np.int64)
    char_index = dense * len(chars) // 256
    if dense > 220:
        return "　"
    return chars[char_index]

# 画像をAAに変換
def image_to_AA(img):
    AA = ""
    for i in range(HEIGHT // PIXEL):
        for j in range(WIDTH // PIXEL):
            img_part = img[i*PIXEL : (i+1)*PIXEL, j*PIXEL : (j+1)*PIXEL]
            assert img_part.size != 0
            AA += image_to_char(img_part)
        AA += "\n"
    return AA

# メイン関数
def main():
    path = input("image path?: ") # ここでAA化する画像のパスを入力
    img = cv2.imread(path)
    img = shrink_image(img)
    AA = image_to_AA(img)
    print(AA)

if __name__ == "__main__":
    main()
