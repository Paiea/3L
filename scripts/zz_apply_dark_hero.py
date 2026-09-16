from pathlib import Path

path = Path("index.html")
s = path.read_text(encoding="utf-8")

replacements = [
    ('<meta name="theme-color" content="#17140f">', '<meta name="theme-color" content="#11100e">'),
    ('<meta property="og:image" content="https://paiea.github.io/peg-leg-greg-reader/3l/assets/images/hero/dragon-bargain.png">', '<meta property="og:image" content="https://paiea.github.io/3L/visual/1212.png">'),
    ('<meta name="twitter:image" content="https://paiea.github.io/peg-leg-greg-reader/3l/assets/images/hero/dragon-bargain.png">', '<meta name="twitter:image" content="https://paiea.github.io/3L/visual/1212.png">'),
    (':root{color-scheme:light;--paper:#f3ede1;--ink:#211d18;--muted:#786f63;--line:#d5cab9;--accent:#8b5635;--accent-dark:#59331f;--panel:#fffaf1;--night:#17140f;--night-soft:#272017;--gold:#d6b176;--max:46rem;--wide:68rem}', ':root{color-scheme:dark;--paper:#11100e;--ink:#eee7db;--muted:#9c968d;--line:#332f2a;--accent:#5ba8d1;--accent-dark:#2f6f91;--panel:#191816;--night:#0c0c0b;--night-soft:#161513;--gold:#b8ada0;--max:46rem;--wide:72rem}'),
    ("body{margin:0;background:var(--paper);color:var(--ink);font-family:Georgia,'Times New Roman',serif;line-height:1.72}", "body{margin:0;background:radial-gradient(circle at 20% 0%,#181715 0,transparent 32rem),var(--paper);color:var(--ink);font-family:Georgia,'Times New Roman',serif;line-height:1.72}"),
    ('a:focus-visible,button:focus-visible,select:focus-visible,input:focus-visible{outline:3px solid #c98c55;outline-offset:3px}', 'a:focus-visible,button:focus-visible,select:focus-visible,input:focus-visible{outline:3px solid var(--accent);outline-offset:3px}'),
    ('.site-head{position:relative;z-index:20;padding:.9rem 0;border-bottom:1px solid rgba(213,202,185,.85);background:rgba(243,237,225,.94);backdrop-filter:blur(12px);font-family:ui-sans-serif,system-ui,sans-serif}', '.site-head{position:relative;z-index:20;padding:.9rem 0;border-bottom:1px solid rgba(238,231,219,.08);background:rgba(17,16,14,.92);backdrop-filter:blur(12px);font-family:ui-sans-serif,system-ui,sans-serif}'),
    ('.site-links .current{color:var(--ink);font-weight:750}', '.site-links .current{color:var(--accent);font-weight:750}'),
    ('.prose blockquote{margin:1.2rem 0;padding-left:1rem;border-left:3px solid var(--line);color:#4d453c}', '.prose blockquote{margin:1.2rem 0;padding-left:1rem;border-left:3px solid var(--line);color:#b9b1a6}'),
    ('.status{font-family:ui-sans-serif,system-ui,sans-serif;background:#efe3cf;border:1px solid #d7c4a7;border-radius:999px;display:inline-block;padding:.28rem .58rem;font-size:.72rem;margin-top:.5rem}', '.status{font-family:ui-sans-serif,system-ui,sans-serif;background:#172127;border:1px solid #334650;color:#c9dce6;border-radius:999px;display:inline-block;padding:.28rem .58rem;font-size:.72rem;margin-top:.5rem}'),
    ('.error{background:#fff3ef;border:1px solid #d9aaa0;border-radius:12px;padding:1rem;font-family:ui-sans-serif,system-ui,sans-serif}', '.error{background:#241817;border:1px solid #68433f;color:#e6c8c3;border-radius:8px;padding:1rem;font-family:ui-sans-serif,system-ui,sans-serif}'),
    ('.audio-card{width:100%;display:grid;grid-template-columns:auto 1fr auto;gap:.85rem;align-items:center;text-align:left;background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:.85rem .95rem;color:var(--ink);cursor:pointer;box-shadow:0 4px 14px rgba(48,39,28,.035);transition:border-color .15s,transform .15s,box-shadow .15s}', '.audio-card{width:100%;display:grid;grid-template-columns:auto 1fr auto;gap:.85rem;align-items:center;text-align:left;background:#171614;border:1px solid var(--line);border-radius:7px;padding:.85rem .95rem;color:var(--ink);cursor:pointer;box-shadow:none;transition:border-color .15s,background .15s}'),
    ('.audio-card:hover{border-color:#ad9577;transform:translateY(-1px);box-shadow:0 9px 24px rgba(48,39,28,.07)}', '.audio-card:hover{border-color:#4f6570;background:#1b1a18}'),
    ('.audio-card .play{width:2.1rem;height:2.1rem;border-radius:999px;display:grid;place-items:center;background:var(--ink);color:var(--panel);font-family:ui-sans-serif,system-ui,sans-serif;font-size:.75rem}', '.audio-card .play{width:2.1rem;height:2.1rem;border-radius:999px;display:grid;place-items:center;background:#24211e;border:1px solid var(--line);color:var(--ink);font-family:ui-sans-serif,system-ui,sans-serif;font-size:.75rem}'),
    ('.lineage a,.lineage .lineage-current{display:block;padding:1rem;border:1px solid var(--line);border-radius:14px;color:var(--ink);text-decoration:none;background:rgba(255,250,241,.55)}', '.lineage a,.lineage .lineage-current{display:block;padding:1rem;border:1px solid var(--line);border-radius:7px;color:var(--ink);text-decoration:none;background:#171614}'),
    ('.lineage a:hover{border-color:#aa9478;background:var(--panel)}', '.lineage a:hover{border-color:#4f6570;background:#1b1a18}'),
    ('.lineage-current{box-shadow:inset 0 0 0 1px rgba(115,74,47,.1)}', '.lineage-current{box-shadow:inset 0 2px 0 rgba(91,168,209,.5)}'),
]

old_hero_css = '''.story-hero{overflow:hidden;display:grid;grid-template-columns:minmax(0,1.18fr) minmax(18rem,.82fr);min-height:33rem;background:var(--night);color:#f7efe3;border-radius:26px;box-shadow:0 24px 70px rgba(38,29,20,.18);margin-bottom:3rem}
.story-hero-art{position:relative;min-height:33rem;background:#0f0d0a}
.story-hero-art img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;display:block}
.story-hero-art:after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,transparent 52%,rgba(23,20,15,.28) 76%,var(--night) 100%),linear-gradient(0deg,rgba(12,10,8,.72) 0%,transparent 45%)}
.scene-caption{position:absolute;z-index:2;left:1.45rem;right:1.45rem;bottom:1.35rem;margin:0;color:#f8efe2;font-size:clamp(1.05rem,2.4vw,1.38rem);line-height:1.35;text-shadow:0 2px 18px #000}
.scene-caption span{display:block;margin-bottom:.3rem;font-family:ui-sans-serif,system-ui,sans-serif;color:#dbc7a8;font-size:.66rem;letter-spacing:.14em;text-transform:uppercase}
.story-hero-copy{display:flex;flex-direction:column;justify-content:center;padding:clamp(2rem,5vw,3.3rem)}
.story-hero-copy .eyebrow{color:#c9ae89}
.story-hero-copy h1{font-size:clamp(3rem,7vw,5.6rem);letter-spacing:-.045em;line-height:.84;margin:.65rem 0 1.35rem;color:#fffaf1}
.story-hook{font-size:clamp(1.13rem,2vw,1.35rem);line-height:1.48;margin:0 0 1rem;color:#efe3d2}
.story-deck{margin:0 0 1.6rem;color:#bfb3a4;font-family:ui-sans-serif,system-ui,sans-serif;font-size:.9rem;line-height:1.6}
.hero-actions{display:flex;flex-wrap:wrap;gap:.7rem;font-family:ui-sans-serif,system-ui,sans-serif}
.hero-actions a{display:inline-flex;align-items:center;justify-content:center;min-height:2.85rem;padding:.62rem 1rem;border-radius:999px;text-decoration:none;font-size:.84rem;font-weight:750}
.hero-actions .primary{background:#f4eadb;color:#211b15}
.hero-actions .secondary{border:1px solid #5c5042;color:#e7d6c1}
.hero-actions a:hover{transform:translateY(-1px)}'''
new_hero_css = '''.story-hero{position:relative;overflow:hidden;isolation:isolate;min-height:clamp(34rem,64vw,48rem);background:#080807;color:#f3ede4;border:1px solid #2b2925;border-radius:8px;box-shadow:0 28px 90px rgba(0,0,0,.45);margin-bottom:3.4rem}
.story-hero-art{position:absolute;inset:0;background:#080807}
.story-hero-art img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;display:block;filter:contrast(1.04) brightness(.9) saturate(.9)}
.story-hero-art:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,8,8,.72) 0%,rgba(7,8,8,.18) 42%,rgba(7,8,8,.1) 62%,rgba(7,8,8,.5) 100%)}
.story-hero-overlay{position:relative;z-index:2;min-height:clamp(34rem,64vw,48rem);display:flex;flex-direction:column;align-items:flex-start;justify-content:flex-start;max-width:39rem;padding:clamp(2rem,5vw,4rem)}
.story-hero-overlay .eyebrow{color:var(--accent);font-size:.7rem;font-weight:760;letter-spacing:.16em}
.story-hero-overlay h1{font-family:ui-sans-serif,system-ui,sans-serif;font-size:clamp(3.5rem,7.6vw,6.7rem);font-weight:900;letter-spacing:-.06em;line-height:.82;margin:.55rem 0 1.25rem;color:#f3eee7;text-transform:uppercase;text-wrap:balance}
.story-hook{max-width:30rem;margin:0 0 1.55rem;color:#eee7dd;font-size:clamp(1.12rem,2vw,1.34rem);line-height:1.45;text-shadow:0 2px 18px rgba(0,0,0,.6)}
.story-hook strong{display:block;margin-bottom:.38rem;font-family:ui-sans-serif,system-ui,sans-serif;font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:#c8c2b8}
.hero-actions{display:flex;flex-wrap:wrap;gap:.6rem;font-family:ui-sans-serif,system-ui,sans-serif}
.hero-actions a{display:inline-flex;align-items:center;justify-content:center;min-height:2.75rem;padding:.58rem .9rem;border:1px solid #5c5750;border-radius:4px;text-decoration:none;font-size:.78rem;font-weight:760;letter-spacing:.025em;background:rgba(10,10,9,.42);color:#eee7db;backdrop-filter:blur(8px)}
.hero-actions .primary{background:#e9e1d6;border-color:#e9e1d6;color:#121210}
.hero-actions .secondary{border-color:#5c5750;color:#eee7db}
.hero-actions a:hover{border-color:var(--accent)}'''
replacements.append((old_hero_css, new_hero_css))

old_media = '''@media(max-width:760px){
  .story-hero{grid-template-columns:1fr;min-height:0}
  .story-hero-art{min-height:56vw;max-height:25rem}
  .story-hero-art:after{background:linear-gradient(0deg,var(--night) 0%,rgba(23,20,15,.24) 40%,transparent 68%)}
  .story-hero-copy{padding:1.75rem 1.3rem 2rem}
  .story-hero-copy h1{font-size:clamp(3.1rem,15vw,5rem)}
  .lineage{grid-template-columns:1fr}
}'''
new_media = '''@media(max-width:760px){
  .story-hero{min-height:42rem}
  .story-hero-overlay{min-height:42rem;max-width:30rem;padding:2rem 1.5rem}
  .story-hero-overlay h1{font-size:clamp(3.4rem,14vw,5.5rem)}
  .story-hero-art img{object-position:52% center}
  .lineage{grid-template-columns:1fr}
}'''
replacements.append((old_media, new_media))
replacements.append(('  .story-hero{border-radius:18px;margin-bottom:2.25rem}\n  .story-hero-art{min-height:70vw}\n  .scene-caption{left:1rem;right:1rem;bottom:.85rem;font-size:1.02rem}', '  .story-hero{min-height:38rem;border-radius:4px;margin-bottom:2.25rem}\n  .story-hero-overlay{min-height:38rem;padding:1.5rem 1.1rem}\n  .story-hero-overlay h1{font-size:clamp(3rem,17vw,4.7rem)}'))

old_hero_html = '''<section class="story-hero" aria-labelledby="story-title">
  <div class="story-hero-art">
    <img src="https://paiea.github.io/peg-leg-greg-reader/3l/assets/images/hero/dragon-bargain.png" alt="Greg faces Ithar, a vast black dragon, in the mountain bargain that opens The Third Leg." width="1536" height="1024" fetchpriority="high" decoding="async">
    <p class="scene-caption"><span>Record 001 · The Petitioner</span>“Is your name Dinner?”<br>“Greg.”</p>
  </div>
  <div class="story-hero-copy">
    <div class="eyebrow">3L · A record of two lives</div>
    <h1 id="story-title">The<br>Third Leg</h1>
    <p class="story-hook">Greg climbed six days to reach a dragon. The first thing Ithar calls him is food.</p>
    <p class="story-deck">Start at the mountain. Listen first if you want the performed version, or read the same story directly underneath.</p>
    <div class="hero-actions"><a class="primary" href="?record=001">Begin Record 001</a><a class="secondary" href="#audioLibrary">Open Audio Library</a></div>
  </div>
</section>'''
new_hero_html = '''<section class="story-hero" aria-labelledby="story-title">
  <div class="story-hero-art" aria-hidden="true">
    <img src="visual/1212.png" alt="" fetchpriority="high" decoding="async">
  </div>
  <div class="story-hero-overlay">
    <div class="eyebrow">3L · Record 001</div>
    <h1 id="story-title">The Third Leg</h1>
    <p class="story-hook"><strong>Six days up.</strong>The first thing Ithar calls him is food.</p>
    <div class="hero-actions"><a class="primary" href="?record=001">Listen from the beginning</a><a class="secondary" href="?record=001">Read Record 001</a></div>
  </div>
</section>'''
replacements.append((old_hero_html, new_hero_html))

for old, new in replacements:
    if old not in s:
        raise SystemExit(f"Missing expected index fragment: {old[:120]!r}")
    s = s.replace(old, new, 1)

path.write_text(s, encoding="utf-8")
