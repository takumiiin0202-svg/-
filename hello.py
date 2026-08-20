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

# Wild mode: fire/lava palette (256-color), scattered per-character for a
# chaotic, blazing look instead of a calm gradient.
FIRE_COLORS = [196, 202, 208, 214, 220, 226, 198, 199]
RESET = "\033[0m"
BOLD = "\033[1m"
BG = "\033[48;5;233m"
STRIPE_COLORS = [196, 226]  # red/yellow hazard stripes


def fire_char(ch, seed):
    if ch == " ":
        return ch
    color = FIRE_COLORS[seed % len(FIRE_COLORS)]
    return f"{BOLD}\033[38;5;{color}m{ch}{RESET}{BG}"


def hazard_border(width):
    chars = []
    for i in range(width):
        color = STRIPE_COLORS[i % 2]
        chars.append(f"\033[38;5;{color}m▓{RESET}{BG}")
    return "".join(chars)


def print_wild(art):
    lines = art.strip("\n").splitlines()
    width = max(len(line) for line in lines) + 4

    print(f"{BG}{hazard_border(width)}{RESET}")
    print(f"{BG}{BOLD}\033[38;5;226m  ⚡ WARNING: WILD MODE ACTIVATED ⚡{RESET}")
    print(f"{BG}{hazard_border(width)}{RESET}")

    seed = 0
    for line in lines:
        padded = f"  {line.ljust(width - 4)}  "
        rendered = "".join(fire_char(ch, seed + j) for j, ch in enumerate(padded))
        seed += 7
        print(f"{BG}{rendered}{RESET}")

    print(f"{BG}{hazard_border(width)}{RESET}")
    print(f"{BG}{BOLD}\033[38;5;196m  \U0001f525 HELLO_WORLD.EXE :: SYSTEM OVERDRIVE \U0001f525{RESET}")
    print(f"{BG}{hazard_border(width)}{RESET}")


print_wild(ART)
