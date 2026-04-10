<script lang="ts">
    import { ArrowLeft } from "lucide-svelte";

    interface Meeting {
        date: string;
        attendees: string;
        topics: string[];
        notes: string;
    }

    interface PageData {
        meetings: Meeting[];
        error: string | null;
    }

    let { data } = $props<{ data: PageData }>();

    let meetings = $derived(data.meetings);
    let error = $derived(data.error);


</script>

<svelte:head>
    <title>Meeting Minutes - Novi Engineering Club</title>
</svelte:head>

<main class="minutes">
    <div class="header">
        <a href="/" class="back-link">
            <ArrowLeft size={20} aria-hidden="true" />
            Back to Home
        </a>
        <h1>Weekly Meeting Minutes</h1>
    </div>

    {#if error}
        <div class="error">Error: {error}</div>
    {:else if meetings.length === 0}
        <div class="empty">No meeting minutes found.</div>
    {:else}
        <div class="meetings-list">
            {#each meetings as meeting, index (meeting.date)}
                <div class="meeting-card" class:alternate={index % 2 === 1}>
                    <div class="meeting-header">
                        <h2 class="meeting-date">{meeting.date}</h2>
                        <span class="attendees">{meeting.attendees}</span>
                    </div>

                    <div class="meeting-content">
                        <div class="section">
                            <h3>Topics</h3>
                            <ul>
                                {#each meeting.topics as topic}
                                    <li>{topic}</li>
                                {/each}
                            </ul>
                        </div>

                        {#if meeting.notes}
                            <div class="section">
                                <h3>Notes</h3>
                                <p>{meeting.notes}</p>
                            </div>
                        {/if}
                    </div>
                </div>
            {/each}
        </div>
    {/if}
</main>

<style>
    .minutes {
        padding: 40px 0 80px;
        max-width: 900px;
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .header {
        margin-bottom: 48px;
    }

    .back-link {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        color: var(--accent);
        text-decoration: none;
        font-family: var(--font-mono);
        font-size: 0.9rem;
        font-weight: 600;
        margin-bottom: 24px;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .back-link:hover {
        transform: translateX(-4px);
        opacity: 0.8;
    }

    .header h1 {
        font-family: var(--font-display);
        font-size: clamp(2rem, 5vw, 3rem);
        font-weight: 800;
        line-height: 1.1;
        margin: 0;
        color: var(--ink);
        letter-spacing: -0.02em;
    }

    .loading,
    .error,
    .empty {
        padding: 40px;
        text-align: center;
        border-radius: 5px;
        font-family: var(--font-mono);
        font-size: 1rem;
    }

    .error {
        color: #e74c3c;
        background: rgba(231, 76, 60, 0.1);
        border: 2px solid #e74c3c;
    }

    .empty {
        color: var(--ink-muted);
        background: var(--surface-subtle);
        border: 2px solid var(--border);
    }

    .meetings-list {
        display: flex;
        flex-direction: column;
        gap: 24px;
    }

    .meeting-card {
        background: var(--surface-elevated);
        border: 2px solid var(--border);
        border-radius: 5px;
        padding: 32px;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) backwards;
        position: relative;
        overflow: hidden;
    }

    .meeting-card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(180deg, var(--accent), var(--accent-dark));
        transform: scaleY(0);
        transform-origin: top;
        transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .meeting-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-lg);
        border-color: var(--accent);
    }

    .meeting-card:hover::before {
        transform: scaleY(1);
    }

    .meeting-card:nth-child(1) {
        animation-delay: 0.2s;
    }
    .meeting-card:nth-child(2) {
        animation-delay: 0.3s;
    }
    .meeting-card:nth-child(3) {
        animation-delay: 0.4s;
    }
    .meeting-card:nth-child(4) {
        animation-delay: 0.5s;
    }
    .meeting-card:nth-child(5) {
        animation-delay: 0.6s;
    }

    .meeting-card.alternate {
        background: var(--surface-subtle);
    }

    .meeting-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 16px;
        margin-bottom: 24px;
        padding-bottom: 16px;
        border-bottom: 2px solid var(--border);
    }

    .meeting-date {
        font-family: var(--font-display);
        font-size: 1.4rem;
        font-weight: 700;
        margin: 0;
        color: var(--ink);
        letter-spacing: -0.01em;
    }

    .attendees {
        font-family: var(--font-mono);
        font-size: 0.85rem;
        color: var(--accent);
        background: var(--accent-glow);
        padding: 6px 12px;
        border-radius: 100px;
        border: 1px solid var(--accent);
        white-space: nowrap;
        font-weight: 600;
    }

    .meeting-content {
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .section {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .section h3 {
        font-family: var(--font-display);
        font-size: 1.05rem;
        font-weight: 700;
        margin: 0;
        color: var(--accent);
        letter-spacing: -0.01em;
    }

    .section ul {
        list-style: none;
        padding: 0;
        margin: 0;
        display: flex;
        flex-direction: column;
        gap: 8px;
    }

    .section li {
        font-family: var(--font-mono);
        font-size: 0.92rem;
        color: var(--ink-muted);
        line-height: 1.6;
        padding-left: 24px;
        position: relative;
    }

    .section li::before {
        content: "→";
        position: absolute;
        left: 0;
        color: var(--accent);
        font-weight: 700;
    }

    .section p {
        font-family: var(--font-mono);
        font-size: 0.92rem;
        color: var(--ink-muted);
        line-height: 1.6;
        margin: 0;
    }

    @media (max-width: 900px) {
        .minutes {
            padding: 40px 0 60px;
        }

        .meeting-header {
            flex-direction: column;
            align-items: flex-start;
            gap: 12px;
        }

        .meeting-date {
            font-size: 1.2rem;
        }

        .meeting-card {
            padding: 24px;
        }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
</style>
