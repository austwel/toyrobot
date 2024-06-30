<script lang="ts">

	$: blocked = false; //TODO fade out the move button if against the edge

	$: x = 0
	$: y = 0
	$: direction = 'EAST'
	let updater = 0

	async function update(event: MouseEvent) {
		const key = (event.target as HTMLButtonElement).getAttribute(
			'data-key'
		);

		let method = ''
		if (key === 'Left') {
			method = './left'
		} else if (key === 'Right') {
			method = './right'
		} else if (key === 'Move') {
			method = './move'
		}
		await fetch(method, {method: 'POST'})
		updater++
	}

	async function place(event: MouseEvent) {
		const key = (event.target as HTMLButtonElement).getAttribute(
			'data-key'
		)
		const x = key?.split(',')[0]
		const y = key?.split(',')[1]
		await fetch('./place?x='+x+'&y='+y+'&direction='+direction, {method: 'POST'})
		updater++
	}

	async function report() {
		try {
			const res = await fetch('./report', {method: 'GET'})
			const text = await res.text()
			const state = JSON.parse(text)
			if('location' in state) {
				x = state.location[0]
				y = state.location[1]
				direction = state.direction
			} else {
				x = 0
				y = 0
				direction = 'EAST'
			}
			return state
		} catch (error) {
			const state = {
				error: true
			}
			return state
		}
		
	}

	function keydown(event: KeyboardEvent) {
		if (event.metaKey) return;
		let action;

		if(event.key === 'ArrowLeft') {
			action = 'Left'
		} else if (event.key === 'ArrowRight') {
			action = 'Right'
		} else if (event.key === 'ArrowUp') {
			action = 'Move'
		} else {
			return
		}

		document.querySelector(`[data-key="${action}" i]`)
		?.dispatchEvent(new MouseEvent('click', { cancelable: true }))
	}

</script>

<svelte:window on:keydown={keydown} />

{#key updater}
<div class="grid">
	{#await report()}
		{#each Array.from(Array(5).keys()) as row (row)}
		<h2 class="visually-hidden">Row {row + 1}</h2>
		<div class="row">
			{#each Array.from(Array(5).keys()) as column (column)}
				<button
					on:click={place}
					class="cell"
					data-key="{column},{4-row}"
				>
					{' '}
					<span class="visually-hidden">
						empty
					</span>
				</button>
			{/each}
		</div>
		{/each}
	{:then state}
		{#each Array.from(Array(5).keys()) as row (row)}
		<h2 class="visually-hidden">Row {row + 1}</h2>
		<div class="row">
			{#each Array.from(Array(5).keys()) as column (column)}
			{#if 'location' in state}
				{@const x = state.location[0]}
				{@const y = state.location[1]}
				{@const direction = state.direction}
				{@const value = x === column && y === 4-row ? (direction === 'NORTH' ? '^' : direction === 'EAST' ? '>' : direction === 'SOUTH' ? 'v' : '<') : ''}
				<button
					on:click={place}
					class="cell"
					data-key="{column},{4-row}"
				>
					{value}
					<span class="visually-hidden">
						empty
					</span>
				</button>
			{:else}
				<button
					on:click={place}
					class="cell"
					data-key="{column},{4-row}"
				>
					{' '}
					<span class="visually-hidden">
						empty
					</span>
				</button>
				{/if}
			{/each}
		</div>
		{/each}
	{/await}
</div>
{/key}
<br>
<div class="controls">
	<div class="movement">
		{#each ['Left', 'Move', 'Right'] as move}
			<button
				on:click|preventDefault={update}
				data-key={move}
				class="move"
				disabled={blocked}
				formaction="?/update"
				name="key"
				value={move}
				aria-label="{move}"
			>{move}</button>
		{/each}
	</div>
	<div class="placement">

	</div>
</div>

<style>
	.grid {
		--width: min(100vw, 40vh, 380px);
		max-width: var(--width);
		align-self: center;
		justify-self: center;
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: flex-start;
	}

	.grid .row {
		display: grid;
		grid-template-columns: repeat(5, 1fr);
		grid-gap: 0.2rem;
		margin: 0 0 0.2rem 0;
	}

	.cell {
		aspect-ratio: 1;
		width: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		text-align: center;
		box-sizing: border-box;
		text-transform: lowercase;
		border: none;
		font-size: calc(0.05 * var(--width));
		border-radius: 2px;
		background: white;
		margin: 0;
		color: rgba(0, 0, 0, 0.7);
	}

	.controls {
		text-align: center;
		justify-content: center;
		height: min(18vh, 10rem);
	}

	.movement {
		--gap: 0.2rem;
		position: relative;
		display: flex;
		flex-direction: row;
		gap: var(--gap);
		height: 50%;
	}

	.movement button {
		--size: min(16vw, 12vh, 80px);
		background-color: white;
		color: black;
		width: var(--size);
		border: none;
		border-radius: 2px;
		font-size: calc(var(--size) * 0.25);
		margin: 0;
	}

	.movement button:hover {
		background: rgba(0, 0, 255, 0.2);
		color: white;
		outline: none;
	}

	.movement button:active {
		background: blue;
		color: white;
		outline: none;
	}

	.movement button[data-key='^']:disabled {
		opacity: 0.5;
	}
</style>
