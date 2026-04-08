<script lang="ts">
    import { page } from "$app/stores";
    import { projects } from "$lib/projects";
    import {
        ChevronDown,
        Instagram,
        Mail,
        MessageSquare,
        Send,
    } from "lucide-svelte";
</script>

<aside class="sidebar">
    <a href="/" class="brand">
        <span>Novi</span>
        <span>Engineering</span>
        <span>Club</span>
    </a>

    <nav class="nav">
        <a class="nav-link" class:active={$page.url.pathname === "/"} href="/">
            Home
        </a>
        <details class="nav-dropdown">
            <summary
                class:active={($page.url.pathname ?? "").startsWith(
                    "/projects",
                )}
            >
                <span class="summary-label">
                    Projects
                </span>
                <ChevronDown class="summary-chevron" size={16} aria-hidden="true" />
            </summary>
            <div class="dropdown-links">
                <a
                    href="/projects"
                    class:active={$page.url.pathname === "/projects"}
                >
                    All Projects
                </a>
                {#each projects as project}
                    <a
                        href="/projects/{project.slug}"
                        class:active={$page.url.pathname ===
                            `/projects/${project.slug}`}
                    >
                        {project.title}
                    </a>
                {/each}
            </div>
        </details>
        <a
            class="nav-link"
            class:active={$page.url.pathname === "/sponsors"}
            href="/sponsors"
        >
            Sponsors
        </a>
        <a
            class="nav-link"
            class:active={$page.url.pathname === "/contact"}
            href="/contact"
        >
            Contact
        </a>
    </nav>

    <div class="socials">
        <a
            class="social-icon"
            href="https://groupme.com"
            target="_blank"
            rel="noopener"
            aria-label="GroupMe"
        >
            <Send size={18} aria-hidden="true" />
        </a>
        <a
            class="social-icon"
            href="https://instagram.com"
            target="_blank"
            rel="noopener"
            aria-label="Instagram"
        >
            <Instagram size={18} aria-hidden="true" />
        </a>
        <a
            class="social-icon"
            href="mailto:novpatils09@stu.novik12.org"
            aria-label="Email"
        >
            <Mail size={18} aria-hidden="true" />
        </a>
        <a
            class="social-icon"
            href="https://discord.com"
            target="_blank"
            rel="noopener"
            aria-label="Discord"
        >
            <MessageSquare size={18} aria-hidden="true" />
        </a>
    </div>
</aside>

<style>
    .sidebar {
        position: sticky;
        top: 0;
        align-self: start;
        height: 100vh;
        padding: 40px 28px;
        border-right: 2px solid var(--border);
        background: var(--surface-elevated);
        display: flex;
        flex-direction: column;
        gap: 40px;
        box-shadow: var(--shadow-sm);
        animation: slideInRight 0.6s cubic-bezier(0.16, 1, 0.3, 1);
        width: 260px;
    }

    .brand {
        font-family: var(--font-display);
        font-size: 1.5rem;
        line-height: 1.05;
        letter-spacing: -0.02em;
        color: var(--ink);
        font-weight: 800;
        position: relative;
        padding-bottom: 18px;
        transition: color 0.3s ease;
    }

    .brand:hover {
        color: var(--accent);
    }

    .brand::after {
        content: "";
        position: absolute;
        bottom: 0;
        left: 0;
        width: 40px;
        height: 4px;
        background: linear-gradient(90deg, var(--accent), var(--accent-dark));
        border-radius: 2px;
    }

    .brand span {
        display: block;
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) backwards;
    }

    .brand span:nth-child(1) {
        animation-delay: 0.1s;
    }
    .brand span:nth-child(2) {
        animation-delay: 0.2s;
    }
    .brand span:nth-child(3) {
        animation-delay: 0.3s;
    }

    .nav {
        display: grid;
        gap: 6px;
        font-size: 0.88rem;
        font-weight: 500;
        letter-spacing: 0.02em;
        font-family: var(--font-mono);
    }

    .nav-link,
    .nav-dropdown summary {
        color: var(--ink-muted);
        display: inline-flex;
        align-items: center;
        justify-content: space-between;
        gap: 10px;
        padding: 12px 16px;
        border-radius: 5px;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .summary-label {
        display: inline-flex;
        align-items: center;
        gap: 10px;
    }

    .summary-chevron {
        transition: transform 0.25s ease;
    }

    .nav-dropdown[open] .summary-chevron {
        transform: rotate(180deg);
    }

    .nav-link::before,
    .nav-dropdown summary::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        width: 3px;
        height: 100%;
        background: var(--accent);
        transform: scaleY(0);
        transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .nav-link:hover,
    .nav-dropdown summary:hover {
        background: var(--surface-subtle);
        color: var(--ink);
        transform: translateX(4px);
    }

    .nav-link:hover::before,
    .nav-dropdown summary:hover::before {
        transform: scaleY(1);
    }

    .nav-link.active {
        background: var(--accent);
        color: white;
        font-weight: 600;
        box-shadow: 0 4px 12px var(--accent-glow);
    }

    .nav-link.active::before {
        display: none;
    }

    .nav-dropdown {
        display: grid;
        gap: 6px;
    }

    .nav-dropdown summary {
        list-style: none;
        user-select: none;
    }

    .nav-dropdown summary::-webkit-details-marker {
        display: none;
    }

    .nav-dropdown summary.active {
        background: linear-gradient(135deg, var(--accent), var(--accent-dark));
        color: white;
        font-weight: 600;
        box-shadow: 0 4px 12px var(--accent-glow);
    }

    .nav-dropdown summary.active::before {
        display: none;
    }

    .dropdown-links {
        display: grid;
        gap: 4px;
        padding-left: 16px;
        margin-top: 6px;
        font-size: 0.82rem;
        letter-spacing: 0.01em;
    }

    .dropdown-links a {
        color: var(--ink-light);
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 16px;
        border-radius: 6px;
        transition: all 0.2s ease;
    }

    .dropdown-links a:hover {
        background: var(--surface-subtle);
        color: var(--ink-muted);
        transform: translateX(4px);
    }

    .dropdown-links a.active {
        color: var(--accent-dark);
        font-weight: 600;
        background: var(--accent-glow);
    }

    .socials {
        margin-top: auto;
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
    }

    .social-icon {
        width: 44px;
        height: 44px;
        border-radius: 100px;
        border: 2px solid var(--border);
        display: grid;
        place-items: center;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        background: var(--surface);
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
        overflow: hidden;
    }

    .social-icon::before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, var(--accent), var(--accent-dark));
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .social-icon :global(svg) {
        position: relative;
        z-index: 1;
        transition: color 0.3s ease;
    }

    .social-icon:hover {
        transform: translateY(-3px) scale(1.05);
        box-shadow: var(--shadow-md);
        border-color: var(--accent);
    }

    .social-icon:hover::before {
        opacity: 1;
    }

    .social-icon:hover :global(svg) {
        color: white;
    }

    @media (max-width: 1024px) {
        .sidebar {
            position: static;
            height: auto;
            width: 100%;
            border-right: none;
            border-bottom: 2px solid var(--border);
            padding: 28px 24px;
        }

        .brand {
            font-size: 1.3rem;
        }
    }
</style>
