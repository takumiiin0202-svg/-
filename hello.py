ART = r"""
      ___           ___           ___       ___       ___
     /\__\         /\  \         /\__\     /\__\     /\  \
    /:/  /        /::\  \       /:/  /    /:/  /    /::\  \
   /:/__/        /:/\:\  \     /:/  /    /:/  /    /:/\:\  \
  /::\  \ ___   /::\~\:\  \   /:/  /    /:/  /    /:/  \:\  \
 /:/\:\  /\__\ /:/\:\ \:\__\ /:/__/    /:/__/    /:/__/ \:\__\
 \/__\:\/:/  / \:\~\:\ \/__/ \:\  \    \:\  \    \:\  \ /:/  /
      \::/  /   \:\ \:\__\    \:\  \    \:\  \    \:\  /:/  /
      /:/  /     \:\ \/__/     \:\  \    \:\  \    \:\/:/  /
     /:/  /       \:\__\        \:\__\    \:\__\    \::/  /
     \/__/         \/__/         \/__/     \/__/     \/__/
      ___           ___           ___           ___       ___
     /\__\         /\  \         /\  \         /\__\     /\  \
    /:/ _/_       /::\  \       /::\  \       /:/  /    /::\  \
   /:/ /\__\     /:/\:\  \     /:/\:\  \     /:/  /    /:/\:\  \
  /:/ /:/ _/_   /:/  \:\  \   /::\~\:\  \   /:/  /    /:/  \:\__\
 /:/_/:/ /\__\ /:/__/ \:\__\ /:/\:\ \:\__\ /:/__/    /:/__/ \:|__|
 \:\/:/ /:/  / \:\  \ /:/  / \/_|::\/:/  / \:\  \    \:\  \ /:/  /
  \::/_/:/  /   \:\  /:/  /     |:|::/  /   \:\  \    \:\  /:/  /
   \:\/:/  /     \:\/:/  /      |:|\/__/     \:\  \    \:\/:/  /
    \::/  /       \::/  /       |:|  |        \:\__\    \::/__/
     \/__/         \/__/         \|__|         \/__/     ~~
"""

# Futuristic HUD palette (256-color): electric blue -> cyan -> teal -> white
TECH_COLORS = [33, 39, 45, 51, 87, 195, 255]
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
BG = "\033[48;5;233m"  # near-black background, HUD-style contrast
FRAME_COLOR = "\033[38;5;39m"


def tech_line(text, color):
    return f"{BG}{BOLD}\033[38;5;{color}m{text}{RESET}"


def frame_line(text):
    return f"{BG}{DIM}{FRAME_COLOR}{text}{RESET}"


def print_futuristic(art):
    lines = art.strip("\n").splitlines()
    width = max(len(line) for line in lines) + 4

    print(frame_line("╔" + "═" * 4 + "[ SYSTEM ONLINE ]" + "═" * (width - 22) + "╗"))
    for i, line in enumerate(lines):
        color = TECH_COLORS[i % len(TECH_COLORS)]
        padded = f"  {line.ljust(width - 4)}  "
        print(f"{frame_line('║')}{tech_line(padded, color)}{frame_line('║')}")
    print(frame_line("╚" + "═" * 4 + "[ HELLO_WORLD.EXE :: RENDER COMPLETE ]" + "═" * max(width - 43, 0) + "╝"))


print_futuristic(ART)
