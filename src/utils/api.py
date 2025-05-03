import requests

API_BASE_URL = "https://mcarchive.net/api/v1/"

def get_mods_by_version(version):
    # versionを文字列として扱う
    version = str(version)
    response = requests.get(f"{API_BASE_URL}mods/?game_version={version}")
    response.raise_for_status()  # Raise an error for bad responses
    mods = response.json()

    # データが空の場合にエラーを返す
    if not mods:
        raise ValueError(f"No mods found for game version: {version}")

    return [mod['slug'] for mod in mods]

def get_mod_download_url(slug, version):
    version = str(version)
    response = requests.get(f"{API_BASE_URL}mods/by_slug/{slug}")
    response.raise_for_status()
    mod_data = response.json()

    if not mod_data.get("mod_versions", []):
        raise ValueError(f"No mod versions found for slug: {slug}")

    for mod_version in mod_data.get("mod_versions", []):
        # 指定されたgame_versionが一致するか確認
        if any(gv.get("name") == version for gv in mod_version.get("game_versions", [])):
            for file in mod_version.get("files", []):
                # "doc"を含むファイル名を除外
                if "doc" not in file["name"].lower():
                    # 優先順位: direct_url > archive_url > redirect_url
                    if file.get("direct_url"):
                        return file["direct_url"]
                    elif file.get("archive_url"):
                        return file["archive_url"]
                    elif file.get("redirect_url"):
                        return file["redirect_url"]

    # 一致するURLが見つからなかった場合
    print(f"\033[93mWarning: No valid download URL found for the specified mod and version.\033[0m")
    return None