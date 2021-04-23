# API
This script allows:
 * To shorten the link.
 * Count the number of clicks on a shortened link.
 
This project interacts with the site [bit.ly](https://app.bitly.com/)

## Environment variables
Some of the settings are taken from the environment. To define them, create a file `.env` next to the file` main.py` and write there data in this format: `VARIABLE = value`.

The following variables are available:
- `LOGIN` — your login on the site [bit.ly](https://app.bitly.com/)
- `BITLY_TOKEN` — your personal token from [bit.ly](https://app.bitly.com/)

## HOW TO USE
1. Save files on your computer.
2. Install dependencies: 
```console
pip3 install -r requirements.txt
```
3. Run main.py in the console: 
```console
python3 main.py www.yourlink.com
```

  * If you want to shorten the link, enter your link as the first argument.
  * If you want to count clicks on links, enter a shortened link as the first argument.
  * If you want to see help, enter a -h or --help as the first argument
