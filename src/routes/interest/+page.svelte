<svelte:head>
  <title>Engineering Interest Group | Novi Engineering Club</title>
  <meta
    name="description"
    content="Join Novi Engineering Club's Engineering Interest Group, fill out the interest form, and access project handouts and group links."
  />
</svelte:head>

<section class="hero">
  <div class="hero-content">
    <span class="hero-badge">Engineering Interest Group</span>
    <h1>Welcome to Novi High School activities fair!</h1>
    <p>
      Interested in engineering? Fill out the interest form, explore our resources, and join the club communities.
    </p>
    <a class="cta-btn" href="/">Home Page</a>
  </div>
</section>

<section id="form" class="section card">
  <div class="section-header">
    <h2>Interest form</h2>
  </div>
  <div class="frame-wrapper">
    <iframe
      src="https://docs.google.com/forms/d/e/1FAIpQLSefGavRiXDvLPTQ7wB8GJhhBd-Syl5nQ_0aGQ-UJC7LIHP6vg/viewform?embedded=true"
      title="Engineering Interest Group Interest Form"
      frameborder="0"
      marginheight="0"
      marginwidth="0"
    >
      Loading…
    </iframe>
  </div>
</section>

<section id="docs" class="section card">
  <div class="section-header">
    <h2>Documentation</h2>
  </div>
  <div class="link-list">
    <a href="https://noviengineering.club/documents/project_fly_handout.pdf" target="_blank" rel="noopener">
      Project Fly Handout
    </a>
    <a href="https://noviengineering.club/documents/project_fly_poster.pdf" target="_blank" rel="noopener">
      Project Fly Poster Board
    </a>
    <a href="https://noviengineering.club/documents/project_tt02.pdf" target="_blank" rel="noopener">
      Project TT02
    </a>
  </div>
</section>

<section id="join" class="section card">
  <div class="section-header">
    <h2>Join Engineering Interest Group</h2>
  </div>
  <div class="join-copy">
    <p>
      Schoology Group:
      <a href="https://novi.schoology.com/group/7553052030" target="_blank" rel="noopener">
        Engineering Interest Group
      </a>
    </p>
    <p>
      GroupMe:
      <a href="https://groupme.com/join_group/104854219/05ltImUw" target="_blank" rel="noopener">
        Engineering Interest Group
      </a>
    </p>
  </div>
</section>

<footer class="page-footer">
  <p>Website made by Smit Patil &amp; Pranav Somalinga</p>
  <p>
    Contact us:
    <a href="mailto:noviengineeringig@gmail.com">noviengineeringig@gmail.com</a>
  </p>
  <p>
    Instagram:
    <a href="https://instagram.com/noviengineeringig" target="_blank" rel="noopener">
      @noviengineeringig
    </a>
  </p>
</footer>

<style>
  .hero {
    padding: 60px 0 40px;
    max-width: 920px;
    animation: fadeInUp 0.8s ease;
  }

  .hero-content {
    background: linear-gradient(180deg, rgba(14, 106, 55, 0.1), transparent 75%);
    border: 1px solid var(--border);
    border-radius: 28px;
    padding: 42px 38px;
    box-shadow: var(--shadow-sm);
  }

  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-family: var(--font-display);
    font-size: 0.8rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 1rem;
  }

  h1 {
    margin: 0 0 20px;
    font-family: var(--font-display);
    font-size: clamp(2.4rem, 4vw, 3.6rem);
    line-height: 1.05;
    color: var(--ink);
  }

  p {
    margin: 0 0 18px;
    font-family: var(--font-main);
    color: var(--ink-muted);
    line-height: 1.8;
    font-size: 1rem;
  }

  .cta-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 14px 24px;
    border-radius: 999px;
    background: var(--accent);
    color: white;
    text-decoration: none;
    font-weight: 700;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }

  .cta-btn:hover {
    transform: translateY(-1px);
    box-shadow: 0 14px 30px rgba(14, 106, 55, 0.25);
  }

  .section {
    margin-top: 32px;
    border-radius: 28px;
    padding: 32px;
    background: var(--surface-elevated);
    border: 1px solid var(--border);
    box-shadow: var(--shadow-sm);
  }

  .section-header {
    margin-bottom: 20px;
  }

  .section-header h2 {
    font-family: var(--font-display);
    font-size: 1.7rem;
    margin: 0;
    color: var(--ink);
  }

  .frame-wrapper {
    border: 1px solid var(--border);
    border-radius: 20px;
    overflow: hidden;
  }

  iframe {
    width: 100%;
    min-height: 840px;
    border: 0;
  }

  .link-list {
    display: grid;
    gap: 12px;
  }

  .link-list a,
  .join-copy a {
    color: var(--accent);
    text-decoration: none;
    font-weight: 600;
  }

  .link-list a:hover,
  .join-copy a:hover {
    text-decoration: underline;
  }

  .join-copy p {
    margin: 0 0 12px;
    color: var(--ink-muted);
    line-height: 1.8;
  }

  .page-footer {
    margin: 40px 0 0;
    padding: 24px 0;
    border-top: 1px solid var(--border);
    color: var(--ink-light);
  }

  .page-footer p {
    margin: 10px 0;
  }

  .page-footer a {
    color: var(--accent);
    text-decoration: none;
  }

  .page-footer a:hover {
    text-decoration: underline;
  }

  @media (max-width: 840px) {
    .hero-content,
    .section {
      padding: 28px;
    }

    iframe {
      min-height: 720px;
    }
  }

  @media (max-width: 640px) {
    .hero-content,
    .section {
      padding: 22px;
    }

    .cta-btn {
      width: 100%;
    }
  }
</style>
