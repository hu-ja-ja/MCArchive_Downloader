import os
import sys
import time  # 追加
from utils.api import get_mods_by_version, get_mod_download_url
from utils.downloader import download_mod

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <game_version> <download_directory>")
        sys.exit(1)

    game_version = sys.argv[1]
    download_directory = sys.argv[2]

    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    print(f"Fetching mods for version: {game_version}")
    try:
        mod_slugs = get_mods_by_version(game_version)
    except ValueError as e:
        print(f"\033[91mError: {e}\033[0m")
        sys.exit(1)

    print(f"Mod slugs fetched: {mod_slugs}")

    mediafire_warnings = []  # MediaFireリンクの警告を格納するリスト

    for i, slug in enumerate(mod_slugs):
        # 20件ごとに1分間待機
        if i > 0 and i % 20 == 0:
            print("Rate limit reached. Waiting for 1 minute...")
            time.sleep(60)

        print(f"Fetching download URL for mod: {slug}")
        try:
            mod_url = get_mod_download_url(slug, game_version)  # 修正: 完全なダウンロードURLを取得
        except ValueError as e:
            print(f"\033[91mError: {e}\033[0m")
            continue

        if mod_url:  # URLが取得できた場合のみダウンロード
            if "mediafire.com" in mod_url:
                mediafire_warnings.append(f"{slug}: {mod_url}")  # 警告をリストに追加
            else:
                print(f"Downloading mod from: {mod_url}")
                download_mod(mod_url, download_directory)
        else:
            # URLが見つからなかった場合の警告を黄色で表示
            print(f"\033[93mWarning: Download URL not found for mod: {slug}\033[0m")

        # 各リクエスト間に少し待機
        time.sleep(3)  # 3秒待機

    # MediaFireリンクの警告を最後にまとめて表示
    if mediafire_warnings:
        print("\n\033[93mMediaFire links detected. These may require manual download:\033[0m")
        for warning in mediafire_warnings:
            print(f"\033[93m{warning}\033[0m")

    print("Download completed.")

if __name__ == "__main__":
    main()