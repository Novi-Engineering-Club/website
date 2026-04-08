<script lang="ts">
  import ProjectPage from '$lib/components/ProjectPage.svelte';
</script>

<ProjectPage
  icon="✈️"
  title="Project Plane"
  description="Build a plane"
  goals={[
    { text: 'Design and 3D print custom plane parts' },
    { text: 'Integrate electronics and motor systems' },
    { text: 'Test performance and iterate on design' }
  ]}
  skills={[
    { text: '3D modeling and printing' },
    { text: 'Electronics and wiring' },
    { text: 'Remote control systems' }
  ]}
/>
