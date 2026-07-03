# GTA Classic MP3 Shuffler
GTA III and Vice City both always play user MP3s in strict alphabetical filename order. This code is a fix that reshuffles them on launch.

## Installation
1. Copy `shuffle_mp3.py` into your game's `mp3` folder (`\Grand Theft Auto III\mp3` or `\Grand Theft Auto Vice City\mp3`).
2. Copy `gta-mp3-shuffle-launch.bat` into your game's root directory (same level as `gta-vc.exe` or `gta3.exe`).
3. Launch the game through `gta-mp3-shuffle-launch.bat` instead of the game's `.exe` directly.
4. Optionally, you can right click `gta-mp3-shuffle-launch.bat`, hover over `Send to` and press `Desktop (Create Shortcut)`.
5. Then, you can pin the shortcut to your Start menu and erase it from your desktop.
6. Using the attached `gtavc.ico` and `gta3.ico` files, you can add an icon to the shortcut so it doesn't look ugly.

## How it works
**`shuffle_mp3.py`**

Finds every `.mp3` in the folder, renames them all to random temporary names so nothing conflicts, then renames them again to `1.mp3`, `2.mp3`, `3.mp3`, so on. The games play by filename order so numbering them randomly is functionally the same as shuffling.
 
**`gta-mp3-shuffle-launch.bat`**

Runs the shuffle script first. If it fails, you get an error message and a pause (this was mostly just for debug purposes when making the code work). If it succeeds, it checks for `gta-vc.exe`, then `gta3.exe`, and launches whichever one it finds so the same script works for either game. It stops with an error if neither is found.

## Credits
I am not affiliated in any way with Rockstar Games, who made GTA Vice City and GTA 3 and their icons, and still sell The Definitive Editions of both games (for which this project will not work).
