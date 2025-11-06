# FlatInstall

Simple Python-based Flatpak installer for Arch Linux.

## Description

FlatInstall is a lightweight command-line tool that simplifies the installation and management of Flatpak applications on Arch Linux systems.

## Prerequisites

- Arch Linux (or Arch-based distribution)
- `base-devel` package group
- `flatpak` installed on your system
```bash
sudo pacman -S base-devel flatpak
```

## Installation

### Building from Source

1. **Clone the repository** (or download the source):
```bash
   git clone https://github.com/lkminv/flatinstall.git
   cd flatinstall
```

2. **Build the package**:
```bash
   makepkg -si
```
   
   This will:
   - Build the package
   - Install it automatically (prompts for sudo password)

   **Alternative** (build without installing):
```bash
   makepkg
```

3. **Manual installation** (if you built without `-i`):
```bash
   sudo pacman -U flatinstall-1.0-1-any.pkg.tar.zst
```

### Verify Installation
```bash
which flatinstall
flatinstall --help
```

## Usage
```bash
flatinstall [options] 
```

For detailed usage instructions, run:
```bash
flatinstall --help
```

## Removal

### Uninstall the package:
```bash
sudo pacman -R flatinstall
```

### Uninstall and remove dependencies:
```bash
sudo pacman -Rs flatinstall
```

### Force removal (if there are issues):
```bash
sudo pacman -Rdd flatinstall
```

## Troubleshooting

### "command not found" after installation
Reload your shell or run:
```bash
hash -r
```

### Permission issues
Make sure the wrapper script is executable:
```bash
chmod +x flatinstall
```

### Reinstalling after changes

1. Clean previous build:
```bash
   rm -f *.pkg.tar.zst
```

2. Rebuild and reinstall:
```bash
   makepkg -fi
```
   (The `-f` flag forces a rebuild)
