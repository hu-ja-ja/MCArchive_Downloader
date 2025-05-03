# Mod Downloader

This project is a Python script designed to download mods from the Minecraft Archive API. It allows users to specify a game version and download the corresponding mods to a designated directory.

## Project Structure

```
mod-downloader
├── src
│   ├── main.py          # Entry point of the application
│   └── utils
│       ├── api.py      # Handles API communication
│       └── downloader.py # Manages the downloading of mods
├── requirements.txt     # Lists project dependencies
└── README.md            # Project documentation
```

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

1. Open a terminal and navigate to the project directory.
2. Run the application using:

```
python src/main.py <game_version> <download_directory>
```

3. Replace `<game_version>` with the desired game version (e.g., `b1.3_01`) and `<download_directory>` with the path to the directory where mods should be saved.

## Functions

- **get_mods_by_version(version)**: Fetches the list of mods available for the specified game version.
- **get_mod_download_url(slug, version)**: Retrieves the direct download URL for a mod based on its slug and game version.
- **download_mod(url, directory)**: Downloads the mod file from the provided URL and saves it to the specified directory.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.