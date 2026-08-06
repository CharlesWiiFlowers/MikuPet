# MikuPet - Your Desktop Diva Companion

A virtual desktop pet inspired by Hatsune Miku. She follows your active window, walks around your desktop, and you can interact with her directly.

## Preview

<div align="center">
  <img src="./public/media/example_0.gif" alt="MikuPet Demo" width="350"/>
  <img src="./public/media/example_1.gif" alt="Miku Walking" width="350"/>
  <img src="./public/media/example_2.gif" alt="Miku Walking to left" width="350"/>
</div>

## Features

* Follows the active window around your desktop.
* Walks automatically across the window boundaries.
* Drag Miku around with your mouse.
* Animated sprite system with customizable characters.
* Lightweight desktop companion built with Python.

---

## Installation

> [!NOTE]
> MikuPet currently supports Windows only.

To run MikuPet on your system:

### 1. Install Python

Make sure Python 3 is installed on your system.

You can download it from:

https://www.python.org/downloads/

### 2. Download MikuPet

Go to the [Releases section](https://github.com/charleswiiflowers/MikuPet/releases) and download the latest version.

Extract the files anywhere on your computer.

### 3. Install dependencies

Open a terminal inside the MikuPet folder and run:

```bash
pip install -r requirements.txt
```

### 4. Run MikuPet

Execute:

```bash
start.bat
```

MikuPet will launch and appear on your desktop.

---

## Usage

After launching MikuPet:

* Miku will appear on your desktop.
* She will follow the active window.
* You can drag her around with your mouse.

More interaction features will be added in future versions.

---

## Built With

* Python 3
* Tkinter
* Pixel Art Sprites
* LibreSprite (for sprite editing and organization)

---

## Architecture

MikuPet has been rebuilt with a modular internal architecture.

The current version includes:

* Event-driven communication system.
* Engine update loop.
* Configurable systems.
* Character state management.
* Independent rendering and animation systems.

The goal is to make MikuPet easier to extend with new behaviors, characters, and features.

---

## Contributing

Contributions are welcome!

If you want to improve MikuPet, feel free to open an issue or submit a pull request.

The project documentation is still being improved. I hope to document the codebase in the future so contributing becomes easier for everyone.

Every contribution will be reviewed before merging.

Some especially valuable contributions would be:

* Adding macOS support.
* Improving cross-platform compatibility.
* Adding new characters or animations.
* Improving the internal systems.

Linux support is also planned, but will be worked on later.

---

## Credits

* Created with love by [Charles Flowers](https://charleswiiflowers.github.io/)

* Character assets by **BYP Studio** and **Chaim Videogames** for *Miku 'n Pop*.
  Source: [The VG Resource](https://www.spriters-resource.com/pc_computer/mikunpop/sheet/46493/)

* Inspired by classic desktop pets such as Shimeji.

---

## Thank You

Thanks for checking out MikuPet.

I hope this little desktop companion brings some fun to your workspace and makes your coding sessions a little more enjoyable.

> Life is a melody you compose at your own tempo.
