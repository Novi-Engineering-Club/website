<script lang="ts">
  import { onMount } from 'svelte';
  import Sidebar from '$lib/components/Sidebar.svelte';
  import { Moon, Sun } from 'lucide-svelte';

  let { children } = $props();

  type Theme = 'light' | 'dark';
  const THEME_KEY = 'nec-theme';
  let theme = $state<Theme>('light');

  const setTheme = (nextTheme: Theme) => {
    theme = nextTheme;
    document.documentElement.setAttribute('data-theme', nextTheme);
    localStorage.setItem(THEME_KEY, nextTheme);
  };

  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };

  onMount(() => {
    const storedTheme = localStorage.getItem(THEME_KEY);
    if (storedTheme === 'light' || storedTheme === 'dark') {
      setTheme(storedTheme);
      return;
    }

    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    setTheme(prefersDark ? 'dark' : 'light');
  });
</script>

<svelte:head>
  <title>Novi Engineering Club</title>
  <meta
    name="description"
    content="The Novi Engineering Club is a student-led group focused on designing, building, and testing real-world solutions."
  />
</svelte:head>

<button
  class="theme-toggle"
  type="button"
  aria-label={theme === 'light' ? 'Enable dark mode' : 'Enable light mode'}
  onclick={toggleTheme}
>
  {#if theme === 'light'}
    <Moon size={16} aria-hidden="true" />
  {:else}
    <Sun size={16} aria-hidden="true" />
  {/if}
</button>

<div class="shell">
  <Sidebar />

  <main class="page">
    {@render children()}
  </main>
</div>

<style global>
  @import "./universal.css";

  .shell {
    display: grid;
    grid-template-columns: 260px minmax(0, 1fr);
    min-height: 100vh;
    width: 100%;
  }

  .page {
    width: min(1050px, 100%);
    padding: 60px 40px 100px;
  }

  .theme-toggle {
    position: fixed;
    top: 18px;
    right: 20px;
    width: 38px;
    height: 38px;
    border: 1px solid var(--border-strong);
    border-radius: 10px;
    background: var(--surface-elevated);
    color: var(--ink-muted);
    display: grid;
    place-items: center;
    cursor: pointer;
    z-index: 1000;
    box-shadow: var(--shadow-sm);
    transition: all 0.2s ease;
  }

  .theme-toggle:hover {
    color: var(--ink);
    border-color: var(--accent);
    transform: translateY(-1px);
    box-shadow: var(--shadow-md);
  }

  @media (max-width: 1024px) {
    .shell {
      grid-template-columns: 1fr;
    }

    .page {
      padding: 40px 24px 80px;
    }

    .theme-toggle {
      top: 14px;
      right: 14px;
      width: 36px;
      height: 36px;
    }
  }
</style>
