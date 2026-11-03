"""Generate the three colour variants of mockup D from one template.

Copy on the page is the club's own, taken verbatim from index.html,
events.html and footer.html in the repo. Only layout, photos and colour change.
"""
import sys, pathlib

ROOT = pathlib.Path(sys.argv[1])  # .../redesign

VARIANTS = {
    "d1-cardinal": dict(label="D1, Cardinal", nav_mark="white", foot_mark="white"),
    "d2-navy": dict(label="D2, Cardinal and navy", nav_mark="white", foot_mark="white"),
    "d3-campus": dict(label="D3, Programme colours", nav_mark="cardinal", foot_mark="white"),
}

FORM = "https://forms.gle/29HpRs3yAWa1Dg757"
LUMA = "https://luma.com/stanford-founders-events"
LIST = "https://mailman.stanford.edu/mailman/listinfo/stanfordfoundersannouncement"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex">
<title>Stanford Founders' Club | Mockup {label}</title>
<meta name="description" content="Stanford Founders' Club is the graduate founder community at Stanford. 1,150+ members across seven schools, 150+ startups pitched, 300+ investors at Demo Day.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Epilogue:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<a class="skip" href="#main">Skip to content</a>

<header class="bar">
  <div class="container bar-inner">
    <a class="wordmark" href="#top">
      <img src="../brand/sfc-mark-{nav_mark}.svg" alt="" width="22" height="24">
      <span>Stanford Founders&rsquo; Club</span>
    </a>
    <nav class="bar-links" aria-label="Primary">
      <a href="../../events.html">Events &amp; Services</a>
      <a href="../../resources.html">Resources</a>
      <a href="../../contact.html">Contact</a>
      <a class="btn btn--nav btn--small" href="{form}">Join Now</a>
    </nav>
  </div>
</header>

<main id="main">

  <section class="wall" id="top">
    <div class="container wall-grid">
      <div class="wall-copy">
        <blockquote class="quote">
          <h1>&ldquo;Alone we can do so little; together we can do so&nbsp;much.&rdquo;</h1>
          <cite>Helen Keller</cite>
        </blockquote>
        <p class="lead">Join our casual community of 1,150+ graduate founders pushing and supporting each other.</p>
        <div class="actions">
          <a class="btn btn--tile" href="{form}">Join the community</a>
          <a class="btn btn--tile-quiet" href="../../events.html">See our events</a>
        </div>
      </div>
      <figure class="tile tile--a">
        <div class="photo" data-slot="wall-a"><img src="../img/networking-portrait.jpg" alt="Two founders in conversation at a dinner" loading="eager"></div>
        <figcaption class="on-photo">Magic Room dinner series, Spring 2026</figcaption>
      </figure>
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

  <section class="history" aria-labelledby="history-h">
    <div class="container history-grid">
      <div class="history-text">
        <h2 id="history-h">History</h2>
        <p class="lead">It started as a WhatsApp group of ten friends trading events, resources and opportunities across Stanford&rsquo;s graduate schools.</p>
        <p>Finding a co-founder, or a resource run by another school, was harder than it should have been. We set out to bridge that gap.</p>
        <p>The chat grew from 10 to over 1,200 members, then became an official student organization running programs and events for graduate students.</p>
      </div>
      <div class="history-photo photo" data-slot="history"><img src="../img/team-community.jpg" alt="A room of members at a club meetup" loading="lazy"></div>
    </div>
  </section>

  <section class="programmes" aria-labelledby="prog-h">
    <div class="container">
      <div class="head-split">
        <h2 id="prog-h">Programming, matching, mixers, and investor access</h2>
        <a class="more" href="../../events.html">Events &amp; Services</a>
      </div>
      <ul class="bento">
        <li class="b b--1">
          <div class="photo" data-slot="p1"><img src="../img/magic-room-portrait.jpg" alt="Members at a co-founder dinner" loading="lazy"></div>
          <div class="b-text"><h3>Co-founder matching</h3><p>We host curated dinners and introductions across the graduate schools to help members find co-founders.</p></div>
        </li>
        <li class="b b--2">
          <div class="photo" data-slot="p2"><img src="../img/sophie-fireside.jpg" alt="A fireside conversation on stage" loading="lazy"></div>
          <div class="b-text"><h3>Founder programming</h3><p>A regular speaker series and workshops on fundraising, recruiting, and go-to-market.</p></div>
        </li>
        <li class="b b--3">
          <div class="photo" data-slot="p3"><img src="../img/energy-event.jpg" alt="Members at an energy-sector gathering" loading="lazy"></div>
          <div class="b-text"><h3>Sector mixers</h3><p>Bio and therapeutics, climate and energy, defense, AI infrastructure, and fintech.</p></div>
        </li>
        <li class="b b--4">
          <div class="photo" data-slot="p4"><img src="../img/dd25-investors-vests.jpg" alt="Investors in the audience at Demo Day" loading="lazy"></div>
          <div class="b-text"><h3>Investor access &amp; Demo Day</h3><p>Partner introductions and the annual Demo Day, held each spring on campus.</p></div>
        </li>
      </ul>
    </div>
  </section>

  <section class="stage" id="demo-day" aria-labelledby="stage-h">
    <div class="container">
      <div class="photo photo--cinema" data-slot="demo"><img src="../img/dd25-tresidder-wide.jpg" alt="A full hall at Demo Day" loading="lazy"></div>
      <div class="stage-row">
        <div class="stage-text">
          <h2 id="stage-h">Every spring at Stanford</h2>
          <p class="lead">Follow us on Luma to hear about the next Demo Day first.</p>
        </div>
        <a class="btn btn--band" href="{luma}">Follow on Luma</a>
      </div>
    </div>
  </section>

  <section class="values" aria-labelledby="values-h">
    <div class="container">
      <div class="head-split">
        <h2 id="values-h">Mission &amp; Values</h2>
        <p class="lead">Support each other.</p>
      </div>
      <div class="principles">
        <article class="principle">
          <div class="photo" data-slot="v1"><img src="../img/ai-social-event.jpg" alt="Members gathered outside on campus" loading="lazy"></div>
          <h3>Where We Fit</h3>
          <p>Stanford already has StartX, GSB E-Club, BASES, ASES, STVP and more. We help earlier: when graduate students move from research to a startup and need a new community.</p>
          <a class="more" href="../../resources.html">Explore 85 Stanford resources</a>
        </article>
        <article class="principle">
          <div class="photo" data-slot="v2"><img src="../img/demo-team-group.jpg" alt="A group photo of the team at Demo Day" loading="lazy"></div>
          <h3>Values</h3>
          <p>Diversity, collaboration and integrity, in a community where founders push and support each other.</p>
        </article>
        <article class="principle">
          <div class="photo" data-slot="v3"><img src="../img/event-dinner.jpg" alt="A long club dinner in a hall" loading="lazy"></div>
          <h3>Community</h3>
          <p>Graduate founders from every school, connected with resources, investors and like-minded co-founders.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="doors" aria-labelledby="doors-h">
    <div class="container">
      <h2 id="doors-h" class="visually-hidden">Get involved</h2>
      <ul class="door-grid">
        <li class="door door--1"><a href="{form}"><span class="door-name">Join the community</span><span class="door-line">Graduate students and affiliates</span></a></li>
        <li class="door door--2"><a href="{luma}"><span class="door-name">Events every week on Luma</span><span class="door-line">Open to all</span></a></li>
        <li class="door door--3"><a href="{list}"><span class="door-name">Mailing list</span><span class="door-line">Announcements and Demo Day</span></a></li>
        <li class="door door--4"><a href="../../contact.html"><span class="door-name">Sponsor, speak, or press</span><span class="door-line">For partners and investors</span></a></li>
      </ul>
    </div>
  </section>

</main>

<footer class="site-foot">
  <div class="container foot-grid">
    <div class="foot-brand">
      <img src="../brand/sfc-mark-{foot_mark}.svg" alt="" width="74" height="81">
      <p class="foot-name">Stanford Founders&rsquo; Club</p>
    </div>
    <div>
      <h2 class="foot-h">Connect</h2>
      <ul>
        <li><a href="https://www.instagram.com/stanford_founders/">Instagram</a></li>
        <li><a href="https://www.linkedin.com/company/stanford-founders/">LinkedIn</a></li>
        <li><a href="../../events.html">Events &amp; Calendar</a></li>
        <li><a href="tel:+18884333195">Text / WhatsApp (888) 433-3195</a></li>
        <li><a href="mailto:hello@intake.stanfordfoundersclub.com">hello@intake.stanfordfoundersclub.com</a></li>
        <li><a href="{list}">Mailing List</a></li>
      </ul>
    </div>
    <div>
      <h2 class="foot-h">For Partners</h2>
      <ul>
        <li><a href="../../contact.html">Sponsor a Mixer</a></li>
        <li><a href="../../contact.html">Speaker Inquiries</a></li>
        <li><a href="../../contact.html">Press</a></li>
      </ul>
    </div>
    <p class="legal">2026 Stanford Founders&rsquo; Club. Stanford&trade; is a trademark of The Board of Trustees of the Leland Stanford Junior University.</p>
  </div>
</footer>

<script>document.querySelectorAll('[data-slot] img').forEach((i) => {{ if (i.complete && !i.naturalWidth) i.remove(); else i.addEventListener('error', () => i.remove(), {{ once: true }}); }});</script>
</body>
</html>
"""

for slug, v in VARIANTS.items():
    d = ROOT / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(TEMPLATE.format(form=FORM, luma=LUMA, list=LIST, **v))
    print("wrote", d / "index.html")
