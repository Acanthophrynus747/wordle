pyinstaller --name pyrdle --icon=wordle-icon.ico --onefile wordle.py;

Copy-Item -Path '.\shuffled_real_wordles.txt' -Destination '.\dist\';

Read-Host -Prompt "Done. Press Enter to exit";