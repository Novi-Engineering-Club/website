<script lang="ts">
    import { ArrowRight, Gem, Mail, Trophy } from "lucide-svelte";
</script>

<section class="hero">
    <h1>Partners who help us build</h1>
    <p class="lede">
        Sponsors provide tools, mentorship, and resources that make hands-on
        engineering possible. We highlight their support in showcases and
        community events.
    </p>
</section>

<section class="tiers">
    <div class="tier platinum">
        <div class="tier-header">
            <div class="tier-badge platinum-badge">Platinum</div>
            <Gem class="tier-icon" size={30} aria-hidden="true" />
        </div>
        <h2>MAHLE</h2>
        <p>Monetary funds</p>
        <div class="tier-decoration"></div>
    </div>

    <div class="tier gold">
        <div class="tier-header">
            <div class="tier-badge gold-badge">Gold</div>
            <Trophy class="tier-icon" size={30} aria-hidden="true" />
        </div>
        <h2>Nankin Farmington</h2>
        <p>Monetary funds</p>
        <div class="tier-decoration"></div>
    </div>
</section>

<section class="cta">
    <div class="cta-content">
        <h2>Interested in sponsoring?</h2>
        <p>We welcome partners who want to support student-led engineering.</p>
    </div>
    <a class="button" href="mailto:novpatils09@stu.novik12.org">
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

    .tiers {
        display: grid;
        gap: 24px;
        padding: 56px 0 40px;
    }

    .tier {
        border: 2px solid var(--border);
        border-radius: 5px;
        padding: 32px;
        background: var(--surface-elevated);
        box-shadow: var(--shadow-sm);
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) backwards;
    }

    .tier:nth-child(1) {
        animation-delay: 0.1s;
    }
    .tier:nth-child(2) {
        animation-delay: 0.2s;
    }

    .tier::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 6px;
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .tier.platinum::before {
        background: linear-gradient(90deg, #e5e4e2, #b8b8b8);
    }

    .tier.gold::before {
        background: linear-gradient(90deg, #ffd700, #b8860b);
    }

    .tier:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg);
    }

    .tier:hover::before {
        transform: scaleX(1);
    }

    .tier-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }

    .tier-badge {
        font-family: var(--font-mono);
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.15em;
        padding: 6px 12px;
        border-radius: 6px;
        border: 1px solid;
        background-size: 200% 200%;
        animation: badgeGradientShift 4s ease-in-out infinite;
    }

    .platinum-badge {
        background-image: linear-gradient(
            120deg,
            rgba(245, 245, 245, 0.35),
            rgba(215, 215, 215, 0.45),
            rgba(183, 183, 183, 0.35),
            rgba(245, 245, 245, 0.35)
        );
        color: #6f6f6f;
        border-color: rgba(184, 184, 184, 0.8);
    }

    .gold-badge {
        background-image: linear-gradient(
            120deg,
            rgba(255, 228, 106, 0.35),
            rgba(255, 200, 56, 0.45),
            rgba(204, 140, 0, 0.35),
            rgba(255, 228, 106, 0.35)
        );
        color: #8e5f00;
        border-color: rgba(255, 215, 0, 0.85);
    }

    :global(:root[data-theme="dark"]) .platinum-badge {
        background-image: linear-gradient(
            120deg,
            rgba(244, 247, 252, 0.3),
            rgba(220, 227, 239, 0.45),
            rgba(168, 183, 208, 0.3),
            rgba(244, 247, 252, 0.3)
        );
        color: #f3f7ff;
        border-color: rgba(236, 242, 252, 0.85);
    }

    :global(:root[data-theme="dark"]) .gold-badge {
        background-image: linear-gradient(
            120deg,
            rgba(255, 231, 148, 0.35),
            rgba(255, 203, 89, 0.5),
            rgba(214, 151, 34, 0.35),
            rgba(255, 231, 148, 0.35)
        );
        color: #fff0c5;
        border-color: rgba(255, 220, 116, 0.9);
    }

    @keyframes badgeGradientShift {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }

    @media (prefers-reduced-motion: reduce) {
        .tier-badge {
            animation: none;
        }
    }

    .tier-icon {
        color: var(--ink-light);
        flex-shrink: 0;
    }

    .tier h2 {
        font-family: var(--font-display);
        margin: 0 0 12px;
        font-size: 1.8rem;
        font-weight: 800;
        letter-spacing: -0.01em;
        color: var(--ink);
    }

    .tier p {
        font-family: var(--font-mono);
        margin: 0;
        color: var(--ink-muted);
        line-height: 1.6;
        font-size: 0.9rem;
    }

    .tier-decoration {
        position: absolute;
        bottom: -20px;
        right: -20px;
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background: radial-gradient(circle, var(--accent-glow), transparent);
        opacity: 0.3;
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
