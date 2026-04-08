<script lang="ts">
  import ProjectPage from '$lib/components/ProjectPage.svelte';
</script>

<ProjectPage
  icon="✈️"
  title="Project Fly"
  description="Modify and build a remote controlled car utilizing 3D printing and electronics."
  goals={[
    { text: 'Design and 3D print custom RC car parts' },
    { text: 'Integrate electronics and motor systems' },
    { text: 'Test performance and iterate on design' }
  ]}
  skills={[
    { text: '3D modeling and printing' },
    { text: 'Electronics and wiring' },
    { text: 'Remote control systems' }
  ]}
/>
