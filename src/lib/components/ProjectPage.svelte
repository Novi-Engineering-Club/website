<script lang="ts">
    import { Cog, FolderKanban, Gauge, Rocket, Target } from "lucide-svelte";

    interface Goal {
        text: string;
    }

    interface Skill {
        text: string;
    }

    let {
        icon = "📦",
        title = "Project",
        description = "",
        goals = [],
        skills = [],
    }: {
        icon?: string;
        title?: string;
        description?: string;
        goals?: Goal[];
        skills?: Skill[];
    } = $props();

    const getHeroIcon = (projectTitle: string) => {
        if (projectTitle.toLowerCase().includes("fly")) return Rocket;
        if (projectTitle.toLowerCase().includes("tt-02")) return Gauge;
        return FolderKanban;
    };
</script>

<section class="hero">
    <div class="badge">
        <svelte:component
            this={getHeroIcon(title)}
            class="badge-icon"
            size={14}
            aria-hidden="true"
        />
        PROJECT
    </div>
    <h1>{title}</h1>
    <p class="lede">
        {description}
    </p>
</section>

<section class="content">
    <div class="card goals">
        <div class="card-header">
            <h2>Current goals</h2>
            <Target class="card-icon" size={28} aria-hidden="true" />
        </div>
        <ul>
            {#each goals as goal}
                <li>{goal.text}</li>
            {/each}
        </ul>
    </div>
    <div class="card skills">
        <div class="card-header">
            <h2>Skills focus</h2>
            <Cog class="card-icon" size={28} aria-hidden="true" />
        </div>
        <ul>
            {#each skills as skill}
                <li>{skill.text}</li>
            {/each}
        </ul>
    </div>
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
        display: inline-flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 24px;
        border: 1px solid var(--accent);
    }

    .badge-icon {
        flex-shrink: 0;
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

    .content {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 24px;
        padding: 56px 0 40px;
    }

    .card {
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

    .card:nth-child(1) {
        animation-delay: 0.1s;
    }
    .card:nth-child(2) {
        animation-delay: 0.2s;
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
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg);
        border-color: var(--accent);
    }

    .card:hover::before {
        transform: scaleX(1);
    }

    .card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }

    .card h2 {
        font-family: var(--font-display);
        font-size: 1.4rem;
        font-weight: 700;
        letter-spacing: -0.01em;
        margin: 0;
        color: var(--ink);
    }

    .card-icon {
        color: var(--accent-dark);
        flex-shrink: 0;
    }

    ul {
        font-family: var(--font-mono);
        margin: 0;
        padding-left: 20px;
        color: var(--ink-muted);
        line-height: 1.8;
        font-size: 0.9rem;
    }

    li {
        margin-bottom: 8px;
        padding-left: 8px;
    }

    li:last-child {
        margin-bottom: 0;
    }

    @media (max-width: 700px) {
        .content {
            grid-template-columns: 1fr;
        }
    }
</style>
