"""Build the D5 preview site (index, events, resources, contact) from the
club's own pages. Run from the repo root: python3 redesign/site/build.py

Content comes from index.html, events.html, resources.html and contact.html;
only layout and styling change. Pages are written next to this script.
"""
import re, pathlib

REPO = pathlib.Path(__file__).resolve().parents[2]
OUT = pathlib.Path(__file__).resolve().parent

FORM = "https://forms.gle/29HpRs3yAWa1Dg757"
LUMA = "https://luma.com/stanford-founders-events"
LIST = "https://mailman.stanford.edu/mailman/listinfo/stanfordfoundersannouncement"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Epilogue:wght@400;600;700&display=swap" rel="stylesheet">'


def head(title, desc, extra_css=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONTS}
{extra_css}<link rel="stylesheet" href="site.css">
</head>
"""


def nav(active):
    def link(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    return f"""<a class="skip" href="#main">Skip to content</a>

<header class="bar">
  <div class="container bar-inner">
    <a class="wordmark" href="index.html">
      <img src="../brand/sfc-mark-ink.svg" alt="" width="28" height="31">
      <span>Stanford Founders&rsquo; Club</span>
    </a>
    <nav class="bar-links" aria-label="Primary">
      {link("events.html", "Events &amp; Services", "events")}
      {link("resources.html", "Resources", "resources")}
      {link("contact.html", "Contact", "contact")}
      <a class="btn btn--primary btn--small" href="{FORM}">Join Now</a>
    </nav>
  </div>
</header>
"""


FOOT = f"""<footer class="site-foot">
  <div class="container foot-grid">
    <div class="foot-brand">
      <img class="foot-lockup" src="../brand/sfc-lockup-white.svg" alt="Stanford Founders&rsquo; Club" width="300" height="248">
    </div>
    <div>
      <h2 class="foot-h">Connect</h2>
      <ul>
        <li><a href="https://www.instagram.com/stanford_founders/">Instagram</a></li>
        <li><a href="https://www.linkedin.com/company/stanford-founders/">LinkedIn</a></li>
        <li><a href="events.html">Events &amp; Calendar</a></li>
        <li><a href="tel:+18884333195">Text / WhatsApp (888) 433-3195</a></li>
        <li><a href="mailto:hello@intake.stanfordfoundersclub.com">hello@intake.stanfordfoundersclub.com</a></li>
        <li><a href="{LIST}">Mailing List</a></li>
      </ul>
    </div>
    <div>
      <h2 class="foot-h">For Partners</h2>
      <ul>
        <li><a href="contact.html">Sponsor a Mixer</a></li>
        <li><a href="contact.html">Speaker Inquiries</a></li>
        <li><a href="contact.html">Press</a></li>
      </ul>
    </div>
    <p class="legal">2026 Stanford Founders&rsquo; Club. Stanford&trade; is a trademark of The Board of Trustees of the Leland Stanford Junior University.</p>
  </div>
</footer>
"""

SLOT_SCRIPT = """<script>document.querySelectorAll('[data-slot] img').forEach((i) => { if (i.complete && !i.naturalWidth) i.remove(); else i.addEventListener('error', () => i.remove(), { once: true }); });</script>
"""


def page(name, html):
    (OUT / name).write_text(html)
    print("wrote", OUT / name)


# ── home ────────────────────────────────────────────────────────────
page("index.html", head("Stanford Founders' Club", "Stanford Founders' Club is the graduate founder community at Stanford. 1,150+ members across seven schools, 150+ startups pitched, 300+ investors at Demo Day.") + '<body class="page-home">\n' + nav("home") + f"""
<main id="main">

  <section class="wall" id="top">
    <div class="container wall-grid">
      <div class="wall-copy">
        <h1>Welcome to Stanford Founders&rsquo; Club</h1>
        <p class="lead">Join our casual community of 1,150+ graduate founders pushing and supporting each other.</p>
        <div class="actions">
          <a class="btn btn--primary" href="{FORM}">Join the community</a>
          <a class="btn" href="events.html">See our events</a>
        </div>
      </div>
      <div class="tile tile--a"><div class="photo" data-slot="wall-a"><img src="../img/networking-portrait.jpg" alt="Two founders in conversation at a Magic Room dinner" loading="eager"></div></div>
      <div class="tile tile--b photo" data-slot="wall-b"><img src="../img/pitch-night-crowd.jpg" alt="Students talking after an evening event" loading="eager"></div>
      <div class="tile tile--c photo" data-slot="wall-c"><img src="../img/demo-pitch.jpg" alt="A founder pitching on stage at Demo Day" loading="eager"></div>
      <div class="tile tile--d photo" data-slot="wall-d"><img src="../img/magic-room-table.jpg" alt="Founders at a long dinner table" loading="eager"></div>
    </div>
  </section>

  <section class="stats" aria-label="The club in numbers">
    <div class="container">
      <dl class="stats-grid">
        <div><dt>Graduate founders</dt><dd>1,150+</dd></div>
        <div><dt>Startups pitched</dt><dd>150+</dd></div>
        <div><dt>Investors at Demo Day</dt><dd>300+</dd></div>
        <div><dt>Demo Day attendees</dt><dd>1,500+</dd></div>
      </dl>
    </div>
  </section>

  <section class="about" aria-label="About the club">
    <div class="container">
      <div class="about-row">
        <h2>History</h2>
        <div class="about-body">
          <p>It started as a WhatsApp group of ten friends trading events, resources and opportunities across Stanford&rsquo;s graduate schools. Finding a co-founder, or a resource run by another school, was harder than it should have been, so we set out to bridge that gap.</p>
          <p>The chat grew from 10 to over 1,200 members, then became an official student organization running programs and events for graduate students.</p>
        </div>
      </div>
      <div class="about-row">
        <h2>Mission &amp; Values</h2>
        <div class="about-cols">
          <div>
            <h3>Where we fit</h3>
            <p>Stanford already has StartX, GSB E-Club, BASES, ASES, STVP and more. We help earlier: when graduate students move from research to a startup and need a new community.</p>
            <a class="more" href="resources.html">Explore Stanford&rsquo;s resources</a>
          </div>
          <div>
            <h3>Values</h3>
            <p>Diversity, collaboration and integrity, in a community where founders push and support each other.</p>
          </div>
          <div>
            <h3>Community</h3>
            <p>Graduate founders from every school, connected with resources, investors and like-minded co-founders.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

</main>
""" + FOOT + SLOT_SCRIPT + "</body>\n</html>\n")


# ── events ──────────────────────────────────────────────────────────
ev = (REPO / "events.html").read_text()
sponsors = re.findall(r'<img src="images/logos/sponsors/([^"]+)" alt="([^"]*)"', ev)
investors = re.findall(r'<img src="images/logos/investors/([^"]+)" alt="([^"]*)"', ev)
logo_li = lambda kind, items: "\n".join(f'        <li><img src="../../images/logos/{kind}/{f}" alt="{a}" loading="lazy"></li>' for f, a in items)

PROGS = [
    ("Founder programming", "A regular speaker series and workshops for members, on fundraising, recruiting, go-to-market and other operating topics, led by founders and partners.",
     ["Speaker series and firesides with operators", "Fundraising, recruiting, and go-to-market workshops", "Office hours with partners and angels"],
     "demo-day-panel.jpg", "Founder Q&amp;A panel with audience"),
    ("Co-founder matching", "Curated dinners and introductions across the graduate schools to help members find co-founders, paired by background, sector, and stage.",
     ["Curated co-founder dinners", "Profile-based introductions across schools", "Office hours for matched pairs"],
     "magic-room-portrait.jpg", "Co-founder dinner, Magic Room series"),
    ("Sector mixers", "Gatherings for members working in similar areas.",
     ["Bio &amp; therapeutics", "Climate &amp; energy", "Defense &amp; deeptech", "AI infrastructure", "Fintech &amp; payments"],
     "ai-social-event.jpg", "AI sector mixer"),
    ("Investor access &amp; Demo Day", "Partner introductions and the annual Demo Day, held each spring on campus.",
     ["Demo Day each spring, open to all members", "Partner introductions at active venture firms", "Pre-pitch reviews with alumni founders"],
     "demo-day-presenter.jpg", "Founder presenting at Stanford Founders Demo Day"),
]
rows = "\n".join(f"""        <li class="prog-row">
          <div class="prog-text">
            <h2>{t}</h2>
            <p>{d}</p>
            <ul class="prog-list">
{chr(10).join(f'              <li>{b}</li>' for b in bl)}
            </ul>
          </div>
          <div class="photo" data-slot="p{i}"><img src="../img/{img}" alt="{alt}" loading="{'eager' if i == 0 else 'lazy'}"></div>
        </li>""" for i, (t, d, bl, img, alt) in enumerate(PROGS))

page("events.html", head("Events & Services | Stanford Founders' Club", "Weekly events on Luma, founder programming, co-founder matching, sector mixers, Demo Day, sponsors, and investors.") + '<body class="page-events">\n' + nav("events") + f"""
<main id="main">

  <section class="page-head">
    <div class="container page-head-grid">
      <h1>Events &amp; Services</h1>
      <div class="page-head-side">
        <a class="btn btn--primary" href="{LUMA}">Events every week on Luma</a>
        <p><a href="{LUMA}?period=past">Browse past events</a></p>
      </div>
    </div>
  </section>

  <section class="programmes" aria-label="What we do">
    <div class="container">
      <ul class="prog-rows">
{rows}
      </ul>
    </div>
  </section>

  <section class="demo" aria-labelledby="demo-h">
    <div class="container">
      <h2 id="demo-h">Spring Demo Day</h2>
      <dl class="stats-grid">
        <div><dt>Startups pitched</dt><dd>90</dd></div>
        <div><dt>Investors in the room</dt><dd>300+</dd></div>
        <div><dt>Total attendees</dt><dd>1,500+</dd></div>
        <div><dt>Stanford graduate schools represented</dt><dd>7</dd></div>
      </dl>
      <div class="photo-row">
        <div class="photo" data-slot="dd1"><img src="../img/dd25-pitch-hyperthread.jpg" alt="A founder pitching at Demo Day" loading="lazy"></div>
        <div class="photo" data-slot="dd2"><img src="../img/dd25-investors-vests.jpg" alt="Investors in the audience at Demo Day" loading="lazy"></div>
        <div class="photo" data-slot="dd3"><img src="../img/demo-day-group-2026.jpg" alt="Organizers and founders together on stage at the Spring 2026 Demo Day" loading="lazy"></div>
      </div>
      <div class="close-row">
        <div class="close-text">
          <h3>Every spring at Stanford</h3>
          <p class="lead">Follow us on Luma to hear about the next Demo Day first.</p>
        </div>
        <div class="actions">
          <a class="btn btn--primary" href="{LUMA}">Follow on Luma</a>
          <a class="btn" href="contact.html">Get in touch</a>
        </div>
      </div>
    </div>
  </section>

  <section class="logos" aria-labelledby="sup-h">
    <div class="container">
      <h2 id="sup-h">With support from</h2>
      <ul class="logo-grid logo-grid--sponsors">
{logo_li("sponsors", sponsors)}
      </ul>
    </div>
  </section>

  <section class="logos" aria-labelledby="inv-h">
    <div class="container">
      <h2 id="inv-h">Investors including</h2>
      <ul class="logo-grid">
{logo_li("investors", investors)}
      </ul>
    </div>
  </section>

</main>
""" + FOOT + SLOT_SCRIPT + "</body>\n</html>\n")


# ── resources: the Atlas markup, unchanged, inside the D5 frame ──────
rs = (REPO / "resources.html").read_text()
atlas = re.search(r'(<div class="atlas-app">.*?\n</div>)\n  </div>\n</section>', rs, re.S).group(1)
page("resources.html", head("Resources | Stanford Founders' Club", "Explore Stanford's entrepreneurship resources: clubs, courses, funds, accelerators, and support offices for Stanford founders, grouped by the kind of help they give.",
                            '<link rel="stylesheet" href="../../static/css/atlas.css">\n') + '<body class="page-resources">\n' + nav("resources") + f"""
<main id="main">

  <section class="page-head">
    <div class="container">
      <h1>Explore Stanford&rsquo;s entrepreneurship resources</h1>
    </div>
  </section>

  <section class="atlas-wrap">
    <div class="container">
{atlas}
    </div>
  </section>

</main>
""" + FOOT + '<script src="../../static/js/atlas.js"></script>\n</body>\n</html>\n')


# ── contact ─────────────────────────────────────────────────────────
page("contact.html", head("Contact | Stanford Founders' Club", "Apply to Stanford Founders' Club, sponsor a mixer, or get in touch.") + '<body class="page-contact">\n' + nav("contact") + f"""
<main id="main">

  <section class="page-head">
    <div class="container">
      <h1>Apply, sponsor, or get in touch</h1>
      <p class="lead">Membership applications go through the form below. Sponsors, speakers, and press should email us directly.</p>
    </div>
  </section>

  <section class="contact">
    <div class="container contact-grid">
      <div class="contact-info">
        <div class="info-block">
          <h2>Reach us</h2>
          <p>Email <a href="mailto:hello@intake.stanfordfoundersclub.com">hello@intake.stanfordfoundersclub.com</a>, or text or WhatsApp <a href="tel:+18884333195">(888) 433-3195</a>.</p>
          <p>Stay in the loop on the <a href="{LIST}">mailing list</a>, <a href="{LUMA}">Luma</a>, <a href="https://www.instagram.com/stanford_founders/">Instagram</a> and <a href="https://www.linkedin.com/company/stanford-founders/">LinkedIn</a>. Members get the WhatsApp community link after joining.</p>
        </div>
        <div class="info-block">
          <h2>Membership</h2>
          <p>Open to current Stanford graduate students working on a company, or seriously considering one. Apply with the form here or the <a href="{FORM}">Google form</a>. Rolling review.</p>
        </div>
        <div class="info-block">
          <h2>Sponsorship</h2>
          <p>Sector mixers and Demo Day are sponsor-supported. Email us for the current deck and pricing.</p>
        </div>
        <div class="info-block">
          <h2>Press</h2>
          <p>For Demo Day press credentials and media inquiries, email us with &ldquo;Press&rdquo; in the subject.</p>
        </div>
      </div>

      <form id="contact-form" class="form" autocomplete="on" novalidate>
        <div class="field-row">
          <div class="field"><label for="firstName">First name</label><input id="firstName" name="firstName" type="text" required autocomplete="given-name"></div>
          <div class="field"><label for="lastName">Last name</label><input id="lastName" name="lastName" type="text" required autocomplete="family-name"></div>
        </div>
        <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email" placeholder="you@example.com"></div>
        <div class="field hp" aria-hidden="true"><label for="website">Website</label><input id="website" name="website" type="text" tabindex="-1" autocomplete="off"></div>
        <div class="field"><label for="message">Message</label><textarea id="message" name="message" required placeholder="Tell us what you're working on, or which inquiry you're sending: membership, sponsor, speaker, or press."></textarea></div>
        <button type="submit" class="btn btn--primary">Send</button>
        <p class="form-status" aria-live="polite"></p>
      </form>
    </div>
  </section>

</main>
""" + FOOT + """<script>
  // Preview only: this copy never posts. The live contact.html keeps its own handler in static/js/components.js.
  document.getElementById('contact-form').addEventListener('submit', (e) => {
    e.preventDefault();
    const f = e.currentTarget, s = f.querySelector('.form-status');
    s.textContent = f.checkValidity() ? 'Preview only: nothing was sent.' : 'Fill in your name, email and message.';
  });
</script>
</body>
</html>
""")
