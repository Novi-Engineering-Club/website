<script lang="ts">
    import { Mail } from "lucide-svelte";
</script>

<section class="hero">
    <div class="badge">GET IN TOUCH</div>
    <h1>Join our engineering community</h1>
    <p class="lede">
        Tell us about yourself and why you're interested in joining the Novi
        Engineering Club. We'd love to hear from you!
    </p>
</section>

<section class="form-container">
    <form
        action="https://formspree.io/f/mkobkyzb"
        method="POST"
        class="contact-form"
        aria-label="Interest form"
    >
        <div class="form-row">
            <label class="form-label">
                Full name
                <input
                    type="text"
                    name="name"
                    required
                    placeholder="First and last name"
                />
            </label>
            <label class="form-label">
                Email
                <input
                    type="email"
                    name="email"
                    required
                    placeholder="your.email@example.com"
                />
            </label>
        </div>

        <div class="form-row">
            <label class="form-label">
                Grade
                <select name="grade" required>
                    <option value="9">9</option>
                    <option value="10">10</option>
                    <option value="11">11</option>
                    <option value="12">12</option>
                </select>
            </label>
            <label class="form-label">
                Phone (optional)
                <input
                    type="tel"
                    name="phone"
                    placeholder="(123) 456-7890"
                />
            </label>
        </div>

        <label class="form-label">
            Message
            <textarea
                name="message"
                rows="4"
                placeholder="Tell us why you want to join or any experience"
            ></textarea>
        </label>

        <input type="hidden" name="_subject" value="New interest form submission" />
        <button type="submit" class="submit-btn">
            <Mail size={18} aria-hidden="true" />
            <span>Send</span>
        </button>
    </form>
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

    .form-container {
        padding: 56px 0 40px;
        max-width: 600px;
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1);
        animation-delay: 0.1s;
    }

    .contact-form {
        display: flex;
        flex-direction: column;
        gap: 24px;
    }

    .form-row {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 16px;
    }

    .form-label {
        display: flex;
        flex-direction: column;
        gap: 8px;
        font-family: var(--font-mono);
        font-size: 0.9rem;
        font-weight: 500;
        color: var(--ink);
    }

    .form-label input,
    .form-label select,
    .form-label textarea {
        padding: 12px 14px;
        border: 2px solid var(--border);
        border-radius: 5px;
        background: var(--surface-elevated);
        color: var(--ink);
        font-size: 0.9rem;
        font-family: var(--font-mono);
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .form-label input::placeholder,
    .form-label textarea::placeholder,
    .form-label select {
        color: var(--ink-light);
    }

    .form-label input:focus,
    .form-label select:focus,
    .form-label textarea:focus {
        outline: none;
        border-color: var(--accent);
        box-shadow: 0 0 0 3px var(--accent-glow);
        background: var(--surface-elevated);
    }

    .form-label select {
        appearance: none;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%232e3440' d='M1.5 4.5l4.5 3 4.5-3'/%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-position: right 12px center;
        padding-right: 36px;
    }

    :root[data-theme="dark"] .form-label select {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%238e9bb0' d='M1.5 4.5l4.5 3 4.5-3'/%3E%3C/svg%3E");
    }

    .submit-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        background: var(--accent);
        color: white;
        border: none;
        padding: 14px 28px;
        border-radius: 5px;
        font-size: 0.95rem;
        font-weight: 600;
        font-family: var(--font-mono);
        cursor: pointer;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
        margin-top: 8px;
    }

    .submit-btn:hover {
        background: var(--accent-dark);
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(14, 106, 55, 0.3);
    }

    .submit-btn:active {
        transform: translateY(0);
    }

    @media (max-width: 700px) {
        .form-row {
            grid-template-columns: 1fr;
        }

        .contact-form {
            gap: 20px;
        }

        h1 {
            font-size: 2rem;
        }
    }
</style>
