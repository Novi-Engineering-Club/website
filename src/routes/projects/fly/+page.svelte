<svelte:head>
  <title>RC Airplane | Novi Engineering Club</title>
  <meta
    name="description"
    content="Explore the Novi Engineering Club's RC airplane program, including the 3D printed Eclipson Model T and plans for the 2026 aircraft project."
  />
</svelte:head>

<section class="hero">
  <div class="hero-content">
    <span class="hero-badge">RC Airplane Project</span>
    <h1>3D Printed Aircraft Development</h1>
    <p>
      Novi Engineering Club is building a 3D printed RC airplane fleet, starting with the Eclipson Model T and planning the next generation project for 2026.
    </p>
  </div>
</section>

<section class="section-grid overview-grid">
  <article class="card">
    <h2>Project Overview</h2>
    <p><strong>Model:</strong> Eclipson Model T (Aircraft 1) & Undecided (Aircraft 2)</p>
    <p><strong>Year Started:</strong> 2025 (Aircraft 1) & 2026 (Aircraft 2)</p>
    <p><strong>Status:</strong> Aircraft 1 – Assembly & Wiring | Aircraft 2 – Planning</p>
  </article>

  <article class="card">
    <h2>Aircraft 1: Eclipson Model T</h2>
    <p>
      In 2025, we began building an RC airplane that is fully 3D printed. The project demonstrates our capability in advanced manufacturing, aerospace design, and rapid prototyping.
    </p>
  </article>
</section>

<section class="section-grid details-grid">
  <article class="card">
    <h2>Technical Specifications</h2>
    <ul>
      <li><strong>Model:</strong> Eclipson Model T</li>
      <li><strong>Wingspan:</strong> 1.2 meters</li>
      <li><strong>Motor:</strong> SunnySky 1250 Kv Brushless Outrunner</li>
      <li><strong>Flight Controller:</strong> Hobbypower 30A</li>
      <li><strong>Transmitter:</strong> Radiolink T8FB</li>
      <li><strong>Receiver:</strong> R8EF</li>
      <li><strong>Power:</strong> 3S LiPo Battery</li>
      <li><strong>Construction:</strong> 100% 3D Printed</li>
    </ul>
  </article>

  <article class="card">
    <h2>Current Progress</h2>
    <ul>
      <li>Fully assembled airframe completed</li>
      <li>Ready to begin wiring process</li>
      <li>Expected completion: Early December 2025</li>
    </ul>
  </article>
</section>

<section class="section-grid overview-grid">
  <article class="card">
    <h2>Aircraft 2: 2026 Project</h2>
    <p>
      A second RC airplane is planned for 2026. Details and specifications will be updated as the project advances.
    </p>
  </article>

  <article class="card">
    <h2>Aircraft 2 Details</h2>
    <p><strong>Model:</strong> Undecided</p>
    <p><strong>Status:</strong> Planning Phase</p>
    <p><strong>More information:</strong> Coming soon...</p>
  </article>
</section>

<section class="gallery-section">
  <div class="gallery-header">
    <h2>Gallery</h2>
    <p>Images from the RC airplane project will appear here as the build progresses.</p>
  </div>
  <div class="gallery-placeholder">
    <p>Gallery coming soon — check back when the Aircraft 1 wiring and flight testing begin.</p>
  </div>
</section>

<footer class="page-footer">
  <p>© 2026 Novi Engineering Club. All rights reserved.</p>
</footer>

<style>
  .hero {
    padding: 48px 0 24px;
    max-width: 980px;
    animation: fadeInUp 0.8s ease;
  }

  .hero-content {
    background: linear-gradient(180deg, rgba(14, 106, 55, 0.08), transparent 80%);
    border: 1px solid var(--border);
    border-radius: 28px;
    padding: 40px 36px;
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
    margin: 0 0 18px;
    font-family: var(--font-display);
    font-size: clamp(2.4rem, 4vw, 3.6rem);
    line-height: 1.05;
    color: var(--ink);
  }

  p {
    margin: 0;
    font-family: var(--font-main);
    color: var(--ink-muted);
    line-height: 1.8;
    font-size: 1rem;
  }

  .section-grid {
    display: grid;
    gap: 24px;
    margin-top: 32px;
  }

  .overview-grid,
  .details-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .card {
    position: relative;
    overflow: hidden;
    background: var(--surface-elevated);
    border: 2px solid transparent;
    border-radius: 5px;
    padding: 28px;
    box-shadow: 0 14px 32px rgba(10, 14, 20, 0.06);
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
  }

  .card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, var(--accent), var(--accent-dark));
    transform-origin: left;
    transform: scaleX(0);
    transition: transform 0.3s ease;
  }

  .card:hover::before {
    transform: scaleX(1);
  }

  .card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 48px rgba(10, 14, 20, 0.12);
    border-color: rgba(14, 106, 55, 1);
  }

  .card h2 {
    margin: 0 0 18px;
    font-family: var(--font-display);
    font-size: 1.5rem;
    color: var(--ink);
  }

  .card ul {
    list-style: disc;
    padding-left: 20px;
    margin: 0;
    color: var(--ink-muted);
  }

  .card ul li,
  .card p {
    margin-bottom: 12px;
  }

  .card ul li:last-child,
  .card p:last-child {
    margin-bottom: 0;
  }

  .gallery-section {
    margin-top: 40px;
  }

  .gallery-header {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 16px;
    align-items: flex-end;
    margin-bottom: 24px;
  }

  .gallery-header h2 {
    font-family: var(--font-display);
    font-size: 1.8rem;
    margin: 0;
    color: var(--ink);
  }

  .gallery-header p {
    margin: 0;
    max-width: 620px;
    color: var(--ink-muted);
  }

  .gallery-placeholder {
    background: var(--surface-elevated);
    border: 1px dashed var(--border);
    border-radius: 20px;
    padding: 32px;
    color: var(--ink-muted);
    text-align: center;
    font-family: var(--font-main);
  }

  .page-footer {
    margin: 48px 0 0;
    padding: 24px 0;
    border-top: 1px solid var(--border);
    text-align: center;
    color: var(--ink-light);
  }

  @media (max-width: 900px) {
    .overview-grid,
    .details-grid {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 640px) {
    .hero-content {
      padding: 28px 20px;
    }
  }
</style>
