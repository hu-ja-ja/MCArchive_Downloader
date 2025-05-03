# MCArchive_Downloader

This project is a Python script designed to download mods from the [MCArchive API](https://mcarchive.net/api/v1/). It allows users to specify a game version and either download the corresponding mods to a designated directory or list all available mod URLs.

## Project Structure

```
MCArchive_Downloader
├── src
│   ├── main.py          # Entry point of the application
│   └── utils
│       ├── api.py      # Handles API communication
│       └── downloader.py # Manages the downloading of mods
├── requirements.txt     # Lists project dependencies
└── README.md            # Project documentation
```

## AI-Generated Code Notice

Some or all of the code in this repository was generated using GitHub Copilot (qwen2.5-coder:7b & GPT-4o).
It has **not been manually reviewed, tested, or modified**.
Please use with caution and perform your own testing and validation before relying on it in production or critical environments.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

1. Open a terminal and navigate to the project directory.
2. Run the application using one of the following commands:

### Download Mods

```
python src/main.py --download <game_version> <download_directory>
```

- Replace `<game_version>` with the desired game version (e.g., `b1.7_01`).
- Replace `<download_directory>` with the path to the directory where mods should be saved.

### List Mod URLs

```
python src/main.py --url <game_version>
```

- Replace `<game_version>` with the desired game version (e.g., `b1.7_01`).

### Notes:
- The script will pause for 1 minute after every 20 mods to respect rate limits.
- If a mod's download URL points to MediaFire, a warning will be displayed, and you may need to download the file manually.
- Each mod download is followed by a 3-second delay to avoid overwhelming the server.

## Functions

- **get_mods_by_version(version)**: Fetches the list of mods available for the specified game version.
- **get_mod_download_url(slug, version)**: Retrieves the direct download URL for a mod based on its slug and game version.
- **get_all_mod_download_urls(slug, version)**: Retrieves all available URLs (direct, archive, and redirect) for a mod based on its slug and game version.
- **download_mod(url, directory)**: Downloads the mod file from the provided URL and saves it to the specified directory. Automatically creates the directory if it does not exist.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.