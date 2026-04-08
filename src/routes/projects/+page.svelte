<script lang="ts">
    import { projects } from "$lib/projects";
    import {
        ArrowRight,
        FolderKanban,
        Gauge,
        Rocket,
    } from "lucide-svelte";

    const getProjectIcon = (slug: string) => {
        if (slug === "plane") return Rocket;
        if (slug === "tt02") return Gauge;
        return FolderKanban;
    };
</script>

<section class="hero">
    <div class="badge">ALL TRACKS</div>
    <h1>Build tracks designed for real-world impact</h1>
    <p class="lede">
        Each project has its own page with goals, build phases, and
        documentation expectations. Pick a track that matches your curiosity.
    </p>
</section>

<section class="grid">
    {#each projects as project, index}
        <a class="card" href="/projects/{project.slug}">
            <div class="card-header">
                <svelte:component
                    this={getProjectIcon(project.slug)}
                    class="card-icon"
                    size={30}
                    aria-hidden="true"
                />
                <div class="card-number">
                    {String(index + 1).padStart(2, "0")}
                </div>
            </div>
            <h2>{project.title}</h2>
            <p>{project.description}</p>
            <ArrowRight class="card-arrow" size={24} aria-hidden="true" />
        </a>
    {/each}
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
        border-radius: 6px;
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

    .grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 24px;
        padding: 56px 0 40px;
    }

    .card {
        border: 2px solid var(--border);
        border-radius: 5px;
        padding: 32px;
        background: var(--surface-elevated);
        box-shadow: var(--shadow-sm);
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        display: flex;
        flex-direction: column;
        gap: 16px;
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) backwards;
    }

    .card:nth-child(1) {
        animation-delay: 0.1s;
    }
    .card:nth-child(2) {
        animation-delay: 0.2s;
    }
    .card:nth-child(3) {
        animation-delay: 0.3s;
    }
    .card:nth-child(4) {
        animation-delay: 0.4s;
    }

    .card::before {
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

    .card:hover {
        transform: translateY(-6px);
        box-shadow: var(--shadow-lg);
        border-color: var(--accent);
    }

    .card:hover::before {
        transform: scaleX(1);
    }

    .card:hover .card-arrow {
        transform: translateX(8px);
        color: var(--accent);
    }

    .card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .card-icon {
        color: var(--accent-dark);
        flex-shrink: 0;
    }

    .card-number {
        font-family: var(--font-display);
        font-size: 0.8rem;
        font-weight: 800;
        letter-spacing: 0.1em;
        color: var(--ink-light);
    }

    .card h2 {
        font-family: var(--font-display);
        margin: 0;
        font-size: 1.5rem;
        font-weight: 700;
        letter-spacing: -0.01em;
        color: var(--ink);
    }

    .card p {
        font-family: var(--font-mono);
        margin: 0;
        color: var(--ink-muted);
        line-height: 1.6;
        font-size: 0.9rem;
        flex: 1;
    }

    .card-arrow {
        color: var(--ink-light);
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        align-self: flex-start;
    }

    @media (max-width: 700px) {
        .grid {
            grid-template-columns: 1fr;
        }
    }
</style>
