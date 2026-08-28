"""Generate the profile's repository map. VOLLEY is deliberately the dominant block."""

from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BG, PANEL, INK, MUTED = "#07111b", "#0c1d2a", "#e8f0f7", "#8fa7ba"
CYAN, VIOLET, AMBER, GREEN = "#38d6e8", "#9b8cff", "#ffb454", "#61d6a3"


def txt(x: float, y: float, value: str, size: int, colour: str = INK, weight: int = 400,
        anchor: str = "start") -> str:
    return (
        f'<text x="{x}" y="{y}" fill="{colour}" font-family="Inter,Segoe UI,sans-serif" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>'
    )


def box(x: float, y: float, w: float, h: float, stroke: str = "#17384b", fill: str = PANEL,
        radius: int = 18) -> str:
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'


def render() -> str:
    out = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900">',
        f'<rect width="1600" height="900" fill="{BG}"/>',
        txt(72, 76, "AVM · ENGINEERING PORTFOLIO", 24, CYAN, 700),
        txt(72, 120, "One flagship, two adjacent systems, three reusable extractions.", 33, INK, 650),
        txt(72, 158, "The block size is deliberate: VOLLEY remains the main body of work.", 19, MUTED),
        box(72, 214, 858, 478, stroke=CYAN),
        txt(108, 266, "FLAGSHIP", 15, CYAN, 700),
        txt(108, 326, "VOLLEY", 48, INK, 750),
        txt(108, 374, "programmable CubeSat deployment", 24, MUTED),
        txt(108, 424, "Gen5 analysed baseline · Gen6 design target", 20, INK, 600),
        txt(108, 464, "70 run sheets · 67 analyses · 0 measurements", 20, INK, 600),
        txt(108, 528, "Engineering record", 14, CYAN, 700),
        txt(108, 562, "calculations · CAD · failures · decisions · provenance", 18, MUTED),
        box(108, 610, 220, 48, stroke="#24536a", fill="#091720", radius=12),
        txt(218, 641, "VOLLEY-paper", 15, INK, 650, "middle"),
        box(344, 610, 220, 48, stroke="#24536a", fill="#091720", radius=12),
        txt(454, 641, "VOLLEY-thesis", 15, INK, 650, "middle"),
        box(580, 610, 220, 48, stroke="#24536a", fill="#091720", radius=12),
        txt(690, 641, "VOLLEY-lab", 15, INK, 650, "middle"),
        box(974, 214, 550, 220, stroke=VIOLET),
        txt(1006, 258, "SIBLING SYSTEM", 14, VIOLET, 700),
        txt(1006, 304, "BOLLEY", 31, INK, 750),
        txt(1006, 344, "passive spacecraft interface", 20, MUTED),
        txt(1006, 386, "opposite premise · same evidence discipline", 17, INK, 550),
        box(974, 472, 550, 220, stroke=AMBER),
        txt(1006, 516, "ADJACENT SYSTEM", 14, AMBER, 700),
        txt(1006, 562, "GATEWAYCX", 31, INK, 750),
        txt(1006, 602, "one Internet across Earth and Moon", 20, MUTED),
        txt(1006, 644, "regional architecture · RF / optical · durable traffic", 17, INK, 550),
    ]
    tools = [
        ("PULSED MOTOR LAB", "force · stroke · source", CYAN),
        ("ORBITAL TRADE", "impulse · recoil · attitude", VIOLET),
        ("EVIDENCE TOOLKIT", "links · JSON · hashes", GREEN),
    ]
    for i, (title, subtitle, colour) in enumerate(tools):
        x = 72 + i * 496
        out += [box(x, 742, 456, 104, stroke=colour, fill="#091720"), txt(x + 26, 784, title, 15, colour, 700), txt(x + 26, 820, subtitle, 17, INK, 550)]
    out += [txt(1494, 882, "PUBLIC REPOSITORIES · PROJECT BOUNDARIES KEPT EXPLICIT", 15, MUTED, 650, "end"), "</svg>"]
    return "\n".join(out) + "\n"


def main() -> None:
    output = ROOT / "assets" / "portfolio-map.svg"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render(), encoding="utf-8")
    print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
