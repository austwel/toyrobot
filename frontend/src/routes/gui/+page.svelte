<script>
	import GUI from './Gui.svelte';
</script>

<svelte:head>
	<title>Toy Robot GUI</title>
	<meta name="description" content="Toy Robot GUI Demonstration" />
</svelte:head>

<section>
	<GUI />
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}
</style>
