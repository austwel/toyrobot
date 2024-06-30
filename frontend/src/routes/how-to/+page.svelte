<svelte:head>
	<title>How to use the toy robot</title>
	<meta name="description" content="How to use the toy robot" />
</svelte:head>

<script lang="ts">
	$: active = false;

	function handleClick(event: MouseEvent) {
		active = !active
	}
</script>

<div class="text-column">
	<h1>How to use the toy robot</h1>

	<p>
		The toy robot coding challenge by <a href="https://joneaves.wordpress.com/2014/07/21/toy-robot-coding-test/">Jon Eaves</a>, is
		a competency test to gauge candidates development and communications skills. It allows developers to have an opportunity to talk about their code.
	</p>

	<p>
		The robot is a very simple simulation of a moveable object on a 5 by 5 grid. The robot has a moveset of five options:
	</p>
	
	<ul>
		<li>PLACE X,Y,F</li>
		<li>MOVE</li>
		<li>LEFT</li>
		<li>RIGHT</li>
		<li>REPORT</li>
	</ul>

	<p>
		For this webapp demonstration I have simplified these moves to mouse and keyboard actions.
	</p>

	<div class="cell">
		<button on:click={handleClick}>{active ? '>' : ' '}</button>
	</div><br>
	<div class="movement">
		<button>Left</button>
		<button>Move</button>
		<button>Right</button>
	</div>

	<p>
		The <button class="demobutton">Left</button> button will rotate the toy robot 90 degrees counter-clockwise. The 
		<button class="demobutton">Right</button> button will similarly rotate the robot clockwise. <button class="demobutton">Move</button> 
		will shift the robot's location forwards one cell in the direction it is currently facing.
	</p>
	
	<p>
		These commands can also be entered by keypress. Left arrow will rotate left, right arrow will rotate right, and the up
		arrow will move the toy robot.
	</p>

	<p>
		Placing the robot works by clicking on the cell you wish to place it on. The robot will start facing east for the first time
		but will retain the direction it was facing when placed at a new location afterwards.
	</p>

	<p>Time to get playing! Click <a href='/gui'><strong>here</strong></a> to return to the game.</p>
</div>

<style>	
	.cell {
		aspect-ratio: 1;
		width: 10%;
		display: flex;
		align-self: center;
		justify-self: center;
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

	.cell button {
		width: 100%;
		height: 100%;
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

	.demobutton {
		--size: min(16vw, 12vh, 65px);
		background-color: white;
		color: black;
		width: calc(var(--size) * 0.8);
		border: none;
		border-radius: 2px;
		font-size: calc(var(--size) * 0.25);
		margin: 0;
	}

	.demobutton:hover {
		background: rgba(0, 0, 255, 0.2);
		color: white;
		outline: none;
	}

	.demobutton:active {
		background: blue;
		color: white;
		outline: none;
	}

	.movement {
		align-self: center;
		justify-self: center;
		--gap: 0.2rem;
		position: relative;
		display: flex;
		flex-direction: row;
		gap: var(--gap);
		height: 100%;
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
</style>