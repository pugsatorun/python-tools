import math

import cv2
from PIL import Image


def get_fps_n_count(video_path):
    """動画のfpsとフレーム数を返す"""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return (None, None)

    count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = round(cap.get(cv2.CAP_PROP_FPS))

    cap.release()
    cv2.destroyAllWindows()
    return (fps, count)


def aspect_ratio(width, height):
    """アスペクト比を返す"""
    gcd = math.gcd(width, height)
    ratio_w = width // gcd
    ratio_h = height // gcd
    return (ratio_w, ratio_h)


def resize_based_on_aspect_ratio(aspect_ratio, base_width, max_width=400):
    """アスペクト比を元にリサイズ後のwidth, heightを求める"""
    if base_width < max_width:
        return None

    base = max_width / aspect_ratio[0]
    new_w = int(base * aspect_ratio[0])
    new_h = int(base * aspect_ratio[1])
    return (new_w, new_h)


def get_frame_range(video_path, start_frame, stop_frame, step_frame):
    """指定された範囲の画像をPillowのimage objectのリストにする"""
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return None

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    asp = aspect_ratio(width, height)
    # でかすぎてもあれなので最大幅を400にしとく
    width_height = resize_based_on_aspect_ratio(asp, width, max_width=800)
    #width_height = width

    im_list = []
    for n in range(start_frame, stop_frame, step_frame):
        cap.set(cv2.CAP_PROP_POS_FRAMES, n)
        ret, frame = cap.read()
        if ret:
            if width_height is not None:
                frame = cv2.resize(frame, dsize=width_height)
            # BGRをRGBにする
            img_array = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # numpyのarrayからPillowのimage objectを作る
            im = Image.fromarray(img_array)
            im_list.append(im)

    cap.release()
    cv2.destroyAllWindows()
    return im_list


def make_gif(filename, im_list):
    """gifを作る"""
    im_list[0].save(filename, save_all=True, append_images=im_list[1:], loop=0)


def main():
    """メイン処理"""
    video_file = "/Users/satoshi/Movies/ドローン荷重実験.mov"

    fps, count = get_fps_n_count(video_file)
    if fps is None:
        print("動画ファイルを開けませんでした")
        return

    # gifにしたい範囲を指定
    start_sec = 40
    stop_sec = 117

    start_frame = int(start_sec * fps)
    stop_frame = int(stop_sec * fps)
    # 適当(fpsに応じてうまいことやれるようにしたい)
    step_frame = 10

    print("開始(けっこう時間がかかる)")
    im_list = get_frame_range(video_file, start_frame, stop_frame, step_frame)
    if im_list is None:
        print("動画ファイルを開けませんでした")
        return

    make_gif('どうぶつ.gif', im_list)
    print("終了")


if __name__ == "__main__":
    main()