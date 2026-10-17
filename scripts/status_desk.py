"""Generate a privacy-friendly status desk snapshot; no external APIs needed."""
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from html import escape
now = datetime.now(ZoneInfo("Europe/Berlin"))
h = now.hour
if 6 <= h < 11:
    phase, sky, moon, status = "MORNING", "#527d9a", "☀", "A new day to learn something."
elif 11 <= h < 18:
    phase, sky, moon, status = "DAYTIME", "#527d9a", "☀", "Build. Test. Improve."
elif 18 <= h < 22:
    phase, sky, moon, status = "EVENING", "#293954", "☾", "Exploring new ideas."
else:
    phase, sky, moon, status = "NIGHT", "#121e36", "☾", "Rest is part of the process."
time = now.strftime("%d %b %Y · %H:%M %Z")
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="960" height="430" viewBox="0 0 960 430" role="img" aria-label="Developer desk snapshot, {escape(phase)} on {escape(time)}">
<rect width="960" height="430" rx="17" fill="#101929"/><rect x="22" y="22" width="916" height="386" rx="14" fill="#17273a" stroke="#314963"/>
<text x="58" y="67" fill="#65e0c3" font-family="monospace" font-size="20">~/status-desk</text><text x="900" y="67" text-anchor="end" fill="#b6c7e0" font-family="monospace" font-size="15">{escape(time)}</text>
<rect x="540" y="92" width="230" height="168" rx="13" fill="{sky}" stroke="#8095b6" stroke-width="9"/><path d="M655 92v168M540 177h230" stroke="#8194ae" stroke-width="6"/>
<text x="652" y="167" text-anchor="middle" font-size="42" fill="#f6d57d">{moon}</text>
<rect x="152" y="290" width="668" height="20" rx="8" fill="#b76b39"/><path d="M175 310h622v79H175z" fill="#744323"/>
<rect x="353" y="176" width="257" height="126" rx="10" fill="#243a4f" stroke="#536a82" stroke-width="7"/><rect x="367" y="189" width="230" height="98" rx="4" fill="#0b1524"/>
<path d="M385 209h65M385 226h126M385 243h88M385 260h115" stroke-width="5" stroke-linecap="round" stroke="#5be2bc"/><path d="M385 226h35" stroke="#7c9dff" stroke-width="5"/><path d="M385 260h32" stroke="#f17b9c" stroke-width="5"/>
<path d="M337 307h291" stroke="#768ba5" stroke-width="11" stroke-linecap="round"/>
<rect x="231" y="238" width="52" height="54" rx="6" fill="#e3eaf5"/><path d="M283 249q29 0 18 22q-6 10 -18 2" fill="none" stroke="#e3eaf5" stroke-width="7"/>
<path d="M722 284l29 -115l18 115" fill="none" stroke="#778ba8" stroke-width="6"/><path d="M726 170h43" stroke="#f9d57b" stroke-width="10" stroke-linecap="round"/>
<text x="58" y="354" font-family="monospace" font-size="20" fill="#75e5c6">{escape(phase)} / STATUS SNAPSHOT</text><text x="58" y="383" font-family="sans-serif" font-size="16" fill="#bfcee0">{escape(status)} · updated automatically, not live presence</text>
</svg>"""
Path('assets/status-desk.svg').write_text(svg, encoding='utf-8')
