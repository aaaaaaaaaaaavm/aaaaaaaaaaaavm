"""Generate the profile repository map. VOLLEY is deliberately dominant."""
from html import escape
from pathlib import Path

ROOT=Path(__file__).resolve().parent
BG,PANEL,INK,MUTED="#07111b","#0c1d2a","#e8f0f7","#8fa7ba"
CYAN,VIOLET,AMBER,GREEN="#38d6e8","#9b8cff","#ffb454","#61d6a3"

def txt(x,y,value,size,colour=INK,weight=400,anchor="start"):
    return f'<text x="{x}" y="{y}" fill="{colour}" font-family="Inter,Segoe UI,sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>'

def box(x,y,w,h,stroke="#17384b",fill=PANEL,radius=18):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'

def render():
    out=['<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1160" viewBox="0 0 1600 1160">',
         f'<rect width="1600" height="1160" fill="{BG}"/>',
         txt(72,76,"AVM · ENGINEERING PORTFOLIO",24,CYAN,700),
         txt(72,120,"One flagship, two adjacent systems, nine focused tools.",33,INK,650),
         txt(72,158,"The hierarchy is deliberate: VOLLEY remains the main body of work.",19,MUTED),
         box(72,214,858,478,stroke=CYAN),
         txt(108,266,"FLAGSHIP",15,CYAN,700),txt(108,326,"VOLLEY",48,INK,750),
         txt(108,374,"programmable CubeSat deployment",24,MUTED),
         txt(108,424,"Gen5 analysed baseline · Gen6 design target",20,INK,600),
         txt(108,464,"70 run sheets · 67 analyses · 0 measurements",20,INK,600),
         txt(108,528,"Engineering record",14,CYAN,700),
         txt(108,562,"calculations · CAD · failures · decisions · provenance",18,MUTED)]
    for x,label in [(108,"VOLLEY-paper"),(344,"VOLLEY-thesis"),(580,"VOLLEY-lab")]:
        out += [box(x,610,220,48,stroke="#24536a",fill="#091720",radius=12),txt(x+110,641,label,15,INK,650,"middle")]
    out += [box(974,214,550,220,stroke=VIOLET),txt(1006,258,"SIBLING SYSTEM",14,VIOLET,700),
            txt(1006,304,"BOLLEY",31,INK,750),txt(1006,344,"passive spacecraft interface",20,MUTED),
            txt(1006,386,"opposite premise · same evidence discipline",17,INK,550),
            box(974,472,550,220,stroke=AMBER),txt(1006,516,"ADJACENT SYSTEM",14,AMBER,700),
            txt(1006,562,"GATEWAYCX",31,INK,750),txt(1006,602,"one Internet across Earth and Moon",20,MUTED),
            txt(1006,644,"regional architecture · vendor-neutral bearers",17,INK,550),
            txt(72,748,"FOCUSED, REUSABLE EXTRACTIONS",16,GREEN,700)]
    tools=[
      ("PULSED MOTOR LAB","force · stroke · source",CYAN),
      ("ORBITAL TRADE","impulse · recoil · attitude",VIOLET),
      ("EVIDENCE TOOLKIT","links · JSON · hashes",GREEN),
      ("CONSTRAINT FLOOR","requirements · additive bounds",CYAN),
      ("CAD EVIDENCE","parameters · artifacts · hashes",AMBER),
      ("SEPARATION DYNAMICS","impulse · tip-off · internal mass",VIOLET),
      ("BEARER SDK","contract · receipt · conformance",AMBER),
      ("DISRUPTION LAB","contacts · wait · forward",GREEN),
      ("RUN REGISTRY","content IDs · claims · lineage",CYAN)]
    for i,(title,subtitle,colour) in enumerate(tools):
        row,col=divmod(i,3); x=72+col*496; y=780+row*104
        out += [box(x,y,456,82,stroke=colour,fill="#091720",radius=14),
                txt(x+22,y+33,title,14,colour,700),txt(x+22,y+60,subtitle,15,INK,550)]
    out += [txt(1494,1138,"PUBLIC REPOSITORIES · BOUNDARIES AND PROVENANCE KEPT EXPLICIT",15,MUTED,650,"end"),"</svg>"]
    return "\n".join(out)+"\n"

def main():
    output=ROOT/"assets"/"portfolio-map.svg"
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(render(),encoding="utf-8")
    print(output.relative_to(ROOT))

if __name__=="__main__": main()
