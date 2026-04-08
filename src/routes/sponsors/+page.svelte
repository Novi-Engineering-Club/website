<script lang="ts">
    import { ArrowRight, Mail, Trophy } from "lucide-svelte";
</script>

<section class="hero">
    <h1>Partners who help us build</h1>
    <p class="lede">
        Sponsors provide tools, mentorship, and resources that make hands-on
        engineering possible. We highlight their support in showcases and
        community events.
    </p>
</section>

<section class="sponsors-grid">
    <div class="sponsor-card">
        <div class="card-content">
            <Trophy class="sponsor-icon" size={30} aria-hidden="true" />
            <h2>MAHLE</h2>
            <p>Monetary funds</p>
        </div>
        <img class="sponsor-image" src="/mahle.png" alt="MAHLE" />
    </div>

    <div class="sponsor-card">
        <div class="card-content">
            <Trophy class="sponsor-icon" size={30} aria-hidden="true" />
            <h2>Nankin Farmington</h2>
            <p>Monetary funds</p>
        </div>
        <img class="sponsor-image" src="/nankin_logo.png" alt="Nankin Farmington" />
    </div>

    <div class="sponsor-card">
        <div class="card-content">
            <Trophy class="sponsor-icon" size={30} aria-hidden="true" />
            <h2>NEF</h2>
            <p>Resources and support</p>
        </div>
        <img class="sponsor-image" src="/nefTrue.png" alt="NEF" />
    </div>
</section>

<section class="cta">
    <div class="cta-content">
        <h2>Interested in sponsoring?</h2>
        <p>We welcome partners who want to support student-led engineering.</p>
    </div>
    <a class="button" href="/contact">
        <Mail class="button-icon" size={18} aria-hidden="true" />
        <span>Get in touch</span>
        <ArrowRight class="arrow" size={18} aria-hidden="true" />
    </a>
</section>

<style>
    .hero {
        padding: 60px 0 48px;
        max-width: 720px;
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .badge {
        font-family: var(--font-mono);
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.18em;
        color: var(--accent);
        background: var(--accent-glow);
        padding: 6px 14px;
        border-radius: 100px;
        display: inline-block;
        margin-bottom: 24px;
        border: 1px solid var(--accent);
    }

    h1 {
        font-family: var(--font-display);
        font-size: clamp(2.4rem, 4.5vw, 3.8rem);
        margin: 0 0 20px;
        line-height: 1.1;
        letter-spacing: -0.02em;
        font-weight: 800;
        color: var(--ink);
    }

    .lede {
        font-family: var(--font-mono);
        color: var(--ink-muted);
        max-width: 620px;
        line-height: 1.7;
        margin: 0;
        font-size: 0.95rem;
    }

    .sponsors-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 24px;
        padding: 56px 0 40px;
    }

    .sponsor-card {
        border: 2px solid var(--border);
        border-radius: 5px;
        padding: 32px;
        background: var(--surface-elevated);
        box-shadow: var(--shadow-sm);
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) backwards;
        display: flex;
        flex-direction: column;
        gap: 16px;
        align-items: center;
        text-align: center;
        min-height: 300px;
    }

    .card-content {
        display: flex;
        flex-direction: column;
        gap: 16px;
        align-items: center;
        text-align: center;
        position: relative;
        z-index: 2;
        transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .sponsor-image {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        opacity: 0;
        transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        z-index: 1;
    }

    .sponsor-card:hover .sponsor-image {
        opacity: 1;
    }

    .sponsor-card:hover .card-content {
        opacity: 0;
    }

    .sponsor-card:nth-child(1) {
        animation-delay: 0.1s;
    }
    .sponsor-card:nth-child(2) {
        animation-delay: 0.2s;
    }
    .sponsor-card:nth-child(3) {
        animation-delay: 0.3s;
    }

    .sponsor-card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, var(--accent), var(--accent-dark));
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
        z-index: 3;
    }

    .sponsor-card:hover {
        transform: translateY(-6px);
        box-shadow: var(--shadow-lg);
        border-color: var(--accent);
    }

    .sponsor-card:hover::before {
        transform: scaleX(1);
    }

    .sponsor-icon {
        color: var(--accent-dark);
        flex-shrink: 0;
    }

    .sponsor-card h2 {
        font-family: var(--font-display);
        margin: 0;
        font-size: 1.5rem;
        font-weight: 700;
        letter-spacing: -0.01em;
        color: var(--ink);
    }

    .sponsor-card p {
        font-family: var(--font-mono);
        margin: 0;
        color: var(--ink-muted);
        line-height: 1.6;
        font-size: 0.9rem;
    }

    .cta {
        border: 2px solid var(--border-strong);
        border-radius: 5px;
        padding: 40px;
        background: var(--surface-subtle);
        display: flex;
        justify-content: space-between;
        gap: 32px;
        align-items: center;
        margin-top: 24px;
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.3s backwards;
    }

    .cta::before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, var(--accent-glow), transparent);
        opacity: 0.5;
    }

    .cta-content {
        position: relative;
        z-index: 1;
    }

    .cta h2 {
        font-family: var(--font-display);
        margin: 0 0 12px;
        font-size: 1.6rem;
        font-weight: 700;
        letter-spacing: -0.01em;
        color: var(--ink);
    }

    .cta p {
        font-family: var(--font-mono);
        margin: 0;
        color: var(--ink-muted);
        font-size: 0.92rem;
        line-height: 1.5;
    }

    .button {
        position: relative;
        z-index: 1;
        padding: 16px 28px;
        border-radius: 5px;
        background: linear-gradient(135deg, var(--accent), var(--accent-dark));
        color: white;
        font-family: var(--font-mono);
        font-weight: 600;
        font-size: 0.92rem;
        display: inline-flex;
        align-items: center;
        gap: 12px;
        box-shadow: 0 4px 16px var(--accent-glow);
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        white-space: nowrap;
    }

    .button .arrow {
        transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .button .button-icon {
        flex-shrink: 0;
    }

    .button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px var(--accent-glow);
    }

    .button:hover .arrow {
        transform: translateX(4px);
    }

    @media (max-width: 700px) {
        .cta {
            flex-direction: column;
            align-items: flex-start;
            padding: 32px 24px;
        }
    }
</style>
