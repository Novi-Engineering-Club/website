<script lang="ts">
  import { Menu } from 'lucide-svelte';

  let { menuOpen = false, toggleMenu = () => {}, clubNameLines = [] } = $props<{
    menuOpen?: boolean;
    toggleMenu?: () => void;
    clubNameLines?: string[];
  }>();
</script>

<div class="mobileHeader">
  <div class="mobileName">
    {#each clubNameLines as line}
      {line}<br />
    {/each}
  </div>
</div>

<button
  class="menuButton"
  aria-label="Toggle menu"
  aria-expanded={menuOpen}
  on:click={toggleMenu}
>
  <Menu size={20} aria-hidden="true" />
</button>
