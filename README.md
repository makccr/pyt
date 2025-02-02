<a href="https://makc.co">
    <img src="https://makccr.github.io/images/github-header.svg" alt="MAKC lgoo" title="MAKC" align="right" height="50" />
</a>

# Polybar YouTube Module
This is a module, and a python script that enables users to place the YouTube subscriber count for any YouTube channel into their polybar configuration. 

<p align="center">
<img src="https://github.com/makccr/pyt/blob/master/shot.png">
</p>

## Dependencies
* [``python3``](https://github.com/python), you may very well be able to run this with older versions of python, but it couldn't hurt to just go ahead and install the newest version.
```sh
sudo pacman -S python
```
* [Source Code Pro Nerd Font](https://github.com/ryanoasis/nerd-fonts), is the default font for icons I've configured this module with.
```sh
sudo yay -S nerd-fonts-source-code-pro
```
* [Product Sans](https://befonts.com/product-sans-font.html), is the default font for text I've configured this module with.
```sh
sudo yay -S ttf-google-fonts-git
```
* [Gnome Character Map](https://wiki.gnome.org/Apps/Gucharmap) (``gucharmap``), is a handy tool that will let you pick glyphs or icons, if you wan't to use a different font.

## Installation Instructions
1. Change directory into your polybar config, clone the repo:
```sh
cd ~/.config/polybar
git clone https://github.com/makccr/pyt.git
```
2. Make the script executable
```sh
cd pyt
chmod +x sub.py
cd ..
```
3. Edit ``polybar/config``, to include the new module: 
```ini
;You'll need to update the following areas of your polybar/config file:

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
exec = /home/makc/.config/polybar/pyt/sub.py
```

### YouTube Video
I've also created a YouTube video with details for setting up and API key, and using the module. If you have any questions, feel free to check out the video: 

[![YT Sub Count Module](https://img.youtube.com/vi/Cj-frgJj83M/maxresdefault.jpg)](https://youtu.be/Cj-frgJj83M )

### Trouble-shooting 
1. You may need to run chmod to make the sub.py file executable after unzipping the files: 
```sh
chmod +x ~/.config/polybar/sub.py
```
2. There is a limit to how many times you can fetch with a standard YouTube API key. By default the module's interval is set to 1800 (thirty minutes). 
```ini
interval = 1800
```
You can set this interval to whatever value you want, but I experienced issues when refreshing at any point higher than once every five minutes (``interval = 300``). Do what you want, but you have been warned.
