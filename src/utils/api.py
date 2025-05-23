# This code was generated by GitHub Copilot (qwen2.5-coder:7b & GPT-4o).
# It has not been manually reviewed, tested, or modified.
# Use at your own risk.

import requests

API_BASE_URL = "https://mcarchive.net/api/v1/"

def get_mods_by_version(version):
    version = str(version)
    response = requests.get(f"{API_BASE_URL}mods/?game_version={version}")
    response.raise_for_status()
    mods = response.json()

    if not mods:
        raise ValueError(f"No mods found for game version: {version}")

    return [mod['slug'] for mod in mods]

def extract_valid_urls(mod_versions, version, exclude_keywords=None):
    """
    Extract valid URLs from mod versions based on the specified game version.

    Args:
        mod_versions (list): List of mod version data.
        version (str): The game version to match.
        exclude_keywords (list): Keywords to exclude from file names.

    Returns:
        list: A list of valid URLs.
    """
    exclude_keywords = exclude_keywords or []
    valid_urls = []

    for mod_version in mod_versions:
        if any(gv.get("name") == version for gv in mod_version.get("game_versions", [])):
            for file in mod_version.get("files", []):
                if not any(keyword in file["name"].lower() for keyword in exclude_keywords):
                    if file.get("direct_url"):
                        valid_urls.append(file["direct_url"])
                    elif file.get("archive_url"):
                        valid_urls.append(file["archive_url"])
                    elif file.get("redirect_url"):
                        valid_urls.append(file["redirect_url"])

    return valid_urls

def get_mod_download_url(slug, version):
    version = str(version)
    response = requests.get(f"{API_BASE_URL}mods/by_slug/{slug}")
    response.raise_for_status()
    mod_data = response.json()

    if not mod_data.get("mod_versions", []):
        raise ValueError(f"No mod versions found for slug: {slug}")

    urls = extract_valid_urls(mod_data.get("mod_versions", []), version, exclude_keywords=["doc"])
    return urls[0] if urls else None

def get_all_mod_download_urls(slug, version):
    version = str(version)
    response = requests.get(f"{API_BASE_URL}mods/by_slug/{slug}")
    response.raise_for_status()
    mod_data = response.json()

    if not mod_data.get("mod_versions", []):
        raise ValueError(f"No mod versions found for slug: {slug}")

    return extract_valid_urls(mod_data.get("mod_versions", []), version, exclude_keywords=["doc", "bundle"])

def get_latest_mod_download_url(slug, version):
    version = str(version)
    response = requests.get(f"{API_BASE_URL}mods/by_slug/{slug}")
    response.raise_for_status()
    mod_data = response.json()

    if not mod_data.get("mod_versions", []):
        raise ValueError(f"No mod versions found for slug: {slug}")

    urls = extract_valid_urls(mod_data.get("mod_versions", []), version, exclude_keywords=["doc", "bundle"])
    return urls[-1] if urls else None