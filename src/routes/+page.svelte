<script lang="ts">
    import { FlaskConical, MapPin, Rocket, Users } from "lucide-svelte";
</script>

<main class="home">
    <div class="hero-section">
        <h1 class="title">
            <span class="title-line">Novi</span>
            <span class="title-line">Engineering</span>
            <span class="title-line accent-word">Club</span>
        </h1>
    </div>

    <div class="content-grid">
        <div class="feature-card primary">
            <div class="card-meta">
                <div class="card-number">01</div>
                <Rocket class="card-icon" size={20} aria-hidden="true" />
            </div>
            <h2>Build real projects with real tools</h2>
            <p>
                From concept to prototype, work with industry-standard equipment
                and methodologies.
            </p>
        </div>

        <div class="feature-card">
            <div class="card-meta">
                <div class="card-number">02</div>
                <FlaskConical class="card-icon" size={20} aria-hidden="true" />
            </div>
            <h2>Learn through prototyping</h2>
            <p>
                Hands-on experience with testing, iteration, and problem-solving
                in real-world scenarios.
            </p>
        </div>

        <div class="feature-card">
            <div class="card-meta">
                <div class="card-number">03</div>
                <Users class="card-icon" size={20} aria-hidden="true" />
            </div>
            <h2>Open to all experience levels</h2>
            <p>
                Whether you're a beginner or advanced, there's a place for you
                to grow and contribute.
            </p>
        </div>

        <a href="/minutes" class="info-banner">
            <div class="info-icon">
                <MapPin size={28} aria-hidden="true" />
            </div>
            <div>
                <h3>Weekly Meetings</h3>
                <p>
                    Join us after school every week. Check sidebar for projects
                    and sponsors.
                </p>
            </div>
        </a>
    </div>
</main>

<style>
    .home {
        padding: 60px 0 80px;
        max-width: 900px;
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .hero-section {
        position: relative;
        margin-bottom: 80px;
        padding: 40px 0;
    }

    .badge {
        font-family: var(--font-mono);
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.15em;
        color: var(--accent);
        background: var(--accent-glow);
        padding: 8px 16px;
        border-radius: 100px;
        display: inline-block;
        margin-bottom: 32px;
        border: 1px solid var(--accent);
        animation: fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.2s backwards;
    }

    .title {
        font-family: var(--font-display);
        font-size: clamp(3rem, 7vw, 5.5rem);
        line-height: 0.95;
        letter-spacing: -0.03em;
        font-weight: 800;
        margin: 0;
        color: var(--ink);
    }

    .title-line {
        display: block;
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) backwards;
    }

    .title-line:nth-child(1) {
        animation-delay: 0.3s;
    }
    .title-line:nth-child(2) {
        animation-delay: 0.4s;
    }
    .title-line:nth-child(3) {
        animation-delay: 0.5s;
    }

    .accent-word {
        background: linear-gradient(135deg, var(--accent), var(--accent-dark));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        position: relative;
    }

    .diagonal-accent {
        position: absolute;
        top: 50%;
        right: -40px;
        width: 200px;
        height: 6px;
        background: linear-gradient(90deg, var(--accent), transparent);
        transform: translateY(-50%) rotate(-15deg);
        opacity: 0.3;
        animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) 0.6s backwards;
    }

    .content-grid {
        display: grid;
        gap: 24px;
    }

    .feature-card {
        background: var(--surface-elevated);
        border: 2px solid var(--border);
        border-radius: 5px;
        padding: 32px;
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) backwards;
    }

    .feature-card:nth-child(1) {
        animation-delay: 0.6s;
    }
    .feature-card:nth-child(2) {
        animation-delay: 0.7s;
    }
    .feature-card:nth-child(3) {
        animation-delay: 0.8s;
    }
    .feature-card:nth-child(4) {
        animation-delay: 0.9s;
    }

    .feature-card::before {
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
    }

    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg);
        border-color: var(--accent);
    }

    .feature-card:hover::before {
        transform: scaleX(1);
    }

    .feature-card.primary {
        background: linear-gradient(
            135deg,
            var(--accent) 0%,
            var(--accent-dark) 100%
        );
        color: white;
        border-color: var(--accent-dark);
        box-shadow: 0 8px 32px var(--accent-glow);
    }

    .feature-card.primary h2,
    .feature-card.primary p {
        color: white;
    }

    .feature-card.primary .card-number {
        color: rgba(255, 255, 255, 0.5);
    }

    .card-number {
        font-family: var(--font-display);
        font-size: 0.85rem;
        font-weight: 800;
        letter-spacing: 0.1em;
        color: var(--accent);
        margin: 0;
    }

    .card-meta {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 16px;
    }

    .card-icon {
        flex-shrink: 0;
    }

    .feature-card h2 {
        font-family: var(--font-display);
        font-size: clamp(1.3rem, 2.5vw, 1.7rem);
        font-weight: 700;
        line-height: 1.2;
        margin: 0 0 12px;
        color: var(--ink);
        letter-spacing: -0.01em;
    }

    .feature-card p {
        font-family: var(--font-mono);
        font-size: 0.92rem;
        line-height: 1.6;
        margin: 0;
        color: var(--ink-muted);
        font-weight: 400;
    }

    .info-banner {
        display: flex;
        align-items: flex-start;
        gap: 20px;
        background: var(--surface-subtle);
        border: 2px solid var(--border-strong);
        border-radius: 5px;
        padding: 28px 32px;
        margin-top: 16px;
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) 0.9s backwards;
        text-decoration: none;
        color: inherit;
        cursor: pointer;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .info-banner:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg);
        border-color: var(--accent);
        background: var(--surface-elevated);
    }

    .info-icon {
        display: grid;
        place-items: center;
        flex-shrink: 0;
        color: var(--accent-dark);
    }

    .info-banner h3 {
        font-family: var(--font-display);
        font-size: 1.1rem;
        font-weight: 700;
        margin: 0 0 8px;
        color: var(--ink);
    }

    .info-banner p {
        font-family: var(--font-mono);
        font-size: 0.88rem;
        line-height: 1.5;
        margin: 0;
        color: var(--ink-muted);
    }

    @media (max-width: 900px) {
        .diagonal-accent {
            display: none;
        }

        .hero-section {
            margin-bottom: 60px;
        }

        .feature-card {
            padding: 24px;
        }
    }
</style>
