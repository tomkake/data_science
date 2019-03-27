import cv2
import numpy as np
import matplotlib.pyplot as plt
"""
    content : https://qiita.com/icoxfog417/items/53e61496ad980c41a08e
"""
def to_matplotlib_format(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#%%
"""
    グレースケール
    画像処理において、カラー情報が必要になることはあまりないので事前にグレースケール化を行うことがある。
    だが最終的には機械学習で使用する際にRGB情報が必要になルため、画像から切り出す際にカラーの方から順に行う。
"""
image_path = './images/'
def to_gray_scale(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return gray
"""
    普通のカラー画像はRGB,blue,green,redの順で読み込まれている。この三つと256階調で表される。
    グレースケール画像とは、0 (黒)～255 (白) までの256階調で表された画像をいう。
    gray = Red * 0.3 + Green * 0.59 + Blue * 0.11
"""
print('before')
img = cv2.imread(image_path + 'birds.JPG')
print(img.shape)
print('after')
gray_to = to_gray_scale(image_path + 'birds.JPG')
print(gray_to.shape)
#%%
"""
    閾値処理
    ある一定の閾値を超えているか否かで分ける画像処理。ある一定の値を下回る場合には黒を割り当て、そうでなければ城を割り当てる。
    背景を落とす->THRESH_BINARY
        閾値より大きい箇所(=明るい=薄い=背景): maxValue(255=白=消す)
        閾値未満: 0(黒=強調)
    境界の明確化->THRESH_BINARY_INV
        閾値より大きい箇所(=明るい=鳥の骨=境界): 0(黒=強調)
        閾値未満: maxValue(255=白=消す)
    https://docs.opencv.org/3.1.0/d7/d4d/tutorial_py_thresholding.html#gsc.tab=0
"""
def binary_threshold(path):
    img = cv2.imread(path)
    grayed = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    under_thresh = 105
    upper_thresh = 145
    maxValue = 255
    th , drop_back = cv2.threshold(grayed, under_thresh, maxValue, cv2.THRESH_BINARY)
    th, clarify_born = cv2.threshold(grayed, upper_thresh, maxValue, cv2.THRESH_BINARY_INV)
    merged = np.minimum(drop_back, clarify_born)
    return merged
print('before')
print(img)
print('after')
binary = binary_threshold(image_path + 'birds.JPG')
print(binary)
"""
    カラーによる閾値処理
    特定の色の部分を抜き出す。
    HSV空間 : 「色相(Hue)」「彩度(Saturation)」「明度(Value・Brightness)」の3要素で表現する方式
    RGBは細かな色の変化を見るのは不向きである(原色の組み合わせで表現しているため各要素を変動させた場合にどう変化するのかイメージが難しい)。
    対してHSVは鮮やかさ、明るさといった直感的に分かりやすい表現であるため感覚的に調整が可能
    https://www.peko-step.com/html/hsv.html
"""
def mask_blue(path):
    img = cv2.imread(path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    blue_min = np.array([100, 170, 200], np.uint8) #np.array([110, 50, 50])
    blue_max = np.array([120, 180, 255], np.uint8) #np.array([130, 255, 255])
    #blue_max = np.array([0, 0, 0], np.uint8)
    """この上記のmin,maxは抜き出したい場合はペイントツールのスポイトを使って推定するか、実際の行列の内容を見るしかない。img[10:20, 10:20]など"""
    blue_region = cv2.inRange(hsv, blue_min, blue_max) #マスク画像の作成
    white = np.full(img.shape, 255, dtype=img.dtype)  #whiteの設定
    background = cv2.bitwise_and(white, white, mask=blue_region) #背景をwhiteで満たす。
    inv_mask = cv2.bitwise_not(blue_region)  # マスクの部分画像をnotに設定
    extracted = cv2.bitwise_and(img, img, mask=inv_mask)
    masked = cv2.add(extracted, background)
    return masked
mask_blu = to_matplotlib_format(mask_blue(image_path + 'birds.JPG'))
plt.imshow(mask_blu)
plt.show()