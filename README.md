<a href="https://makc.co">
    <img src="https://makccr.github.io/images/github-header.svg" alt="MAKC lgoo" title="MAKC" align="right" height="60" />
</a>

# Polybar YouTube Module
This is a module, and a python script that enables users to place the YouTube subscriber count for any YouTube channel into their polybar configuration. The module requires a [YouTube API key](https://developers.google.com/youtube/v3/getting-started), additional instructions for which are included below.

<p align="center">
<img src="https://github.com/makccr/pyt/blob/master/shot.png">
</p>

## Dependencies
* [``python3``](https://github.com/python), you may very well be able to run this with older versions of python, but it couldn't hurt to just go ahead and install the newest version.
```
sudo pacman -S python
```
* [Source Code Pro Nerd Font](https://github.com/ryanoasis/nerd-fonts), is the default font for icons I've configured this module with.
```
sudo yay -S nerd-fonts-source-code-pro
```
* [Product Sans](https://befonts.com/product-sans-font.html), is the default font for text I've configured this module with.
```
sudo yay -S ttf-google-fonts-git
```
* [Gnome Character Map](https://wiki.gnome.org/Apps/Gucharmap) (``gucharmap``), is a handy tool that will let you pick glyphs or icons, if you wan't to use a different font.

## Installation Instructions
1. Download [ytSubCount.zip](https://github.com/makccr/pyt/releases) from the releases page. 
2. Navigate to your Downloads directory, and unzip the file:
```
sudo pacman -S unzip && cd Downloads && unzip ytSubCount.zip
```
3. Copy the ``api.txt``, and ``sub.py``, into your polybar config directory:
```
cp ~/Downloads/yt/api.txt ~/.config/polybar/api.txt && cp ~/Downloads/yt/sub.py ~/.config/polybar/sub.py
```
4. Navigate into the polybar config, and update the ``sub.py`` & ``api.key`` with:
    * Your API key (in ``api.txt``).
    * The path you the api.txt file (in ``sub.py``).
    * The username of the YouTube channel you wish to track (in ``sub.py``)
```
USERNAME="YOUTUBE-USERNAME" #replace with channel username

# You can also need to update the filepath below, with the path to a text document
# containing your YouTube API key.
# Default: /home/YOURSYSTEMUSERNAME/.config/polybar/api.txt
with open("PATH TO API.TXT", "r") as file:
    APIKEY = file.readline().strip()
```
5. Edit ``polybar/config``, to include the new module: 
```
# You'll need to update the following areas of your polybar/config file:

font-0 = Product Sans:size=10;2
font-1 = Sauce Code Pro NF:size=18;4

modules-left = 
modules-center = 
modules-right = yt 

[module/yt]
type = custom/script
interval = 1800
format-prefix = "  "
format = <label>
exec = /home/makc/.config/polybar/sub.py
```

### YouTube Video
I've also created a YouTube video with details for setting up and API key, and using the module. If you have any questions, feel free to check out the video: 

[![YT Sub Count Module](https://img.youtube.com/vi/Cj-frgJj83M /maxresdefault.jpg)](https://youtu.be/Cj-frgJj83M )

### Trouble-shooting 
1. You may need to run chmod to make the sub.py file executable after unzipping the files: 
```
chmod +x ~/.config/polybar/sub.py
```
2. There is a limit to how many times you can fetch with a standard YouTube API key. By default the module's interval is set to 1800 (thirty minutes). 
```
interval = 1800
```
You can set this interval to whatever value you want, but I experienced issues when refreshing at any point higher than once every five minutes (``interval = 300``). Do what you want, but you have been warned.
