# 21.co-Password-Generator
A Bitcoin payable API for generating secure, random passwords.

Requirements:
--
This project requires the two1 libraries for Python 3 from [21.co](https://21.co).

Usage:
--
 - Start a screen session: `screen -S passgen-server`
 - Start the server: `python3 passgen.py`
 - Detach the screen: <kbd>CTRL</kbd>+<kbd>a</kbd>, <kbd>d</kbd>
 - Publish your app: `21 publish submit manifest.yaml`
 
Before publishing, make sure you replace the `<YOUR IP HERE>` with the IP you get from `21 market status`.
