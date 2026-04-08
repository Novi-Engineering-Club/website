<script lang="ts">
  type NavItem = { href: string; label: string };

  let {
    pageTitle,
    navItems = [],
    activePath = '',
    closeMenu = () => {},
    clubNameLines = [],
    shortName = ''
  } = $props<{
    pageTitle: string;
    navItems?: NavItem[];
    activePath?: string;
    closeMenu?: () => void;
    clubNameLines?: string[];
    shortName?: string;
  }>();
</script>

<aside class="menu">
  <p>{shortName}</p>
  <h1>{pageTitle}</h1>
  <h1>
    {#each clubNameLines as line}
      {line}<br />
    {/each}
  </h1>

  {#each navItems as item}
    <a
      href={item.href}
      class:active={activePath === item.href}
      on:click={closeMenu}
    >
      {item.label}
    </a>
  {/each}

  <div class="socials"></div>
</aside>
