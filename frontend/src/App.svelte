<script>
	import Jug from "./Jug.svelte";
	let x_gallons = 5;
	let y_gallons = 3;
	let z_gallons = 4;
	let result;

	let x_result = 5;
	let y_result = 0;

	const draw_step = (steps, index) => {
		x_result = steps[index].jug_x.current_level;
		y_result = steps[index].jug_y.current_level;
		if (index + 1 < steps.length) {
			setTimeout(draw_step, 1000, steps, index + 1);
		}
	};

	const solveRiddle = async () => {
		x_result = 0;
		y_result = 0;
		result = await fetch(
			`http://localhost:5000/solve?` +
				new URLSearchParams({
					x: x_gallons,
					y: y_gallons,
					z: z_gallons,
				}),
			{
				method: "POST",
			}
		).then((r) => r.json());
		if (result.status == "FOUND") {
			draw_step(result.steps, 0);
		}
	};
</script>

<main class="container">
	<h2>The Water Jug Riddle</h2>

	<form on:submit|preventDefault={solveRiddle}>
		<label for="jug_x">
			Jug X
			<input
				type="number"
				id="jug_x"
				bind:value={x_gallons}
				placeholder="Jug X"
				required
			/>
		</label>

		<label for="jug_y">
			Jug Y
			<input
				type="number"
				id="jug_y"
				bind:value={y_gallons}
				placeholder="Jug Y"
				required
			/>
		</label>

		<label for="z_gallons">
			Z gallons
			<input
				type="number"
				id="z_gallons"
				bind:value={z_gallons}
				placeholder="Z gallons"
				required
			/>
		</label>

		<button type="submit">Solve</button>
	</form>

	{#await result}
		Loading...
	{:then data}
		{#if data && data.steps}
			<!-- promise was fulfilled -->
			{#if data.status == "NOT_FOUND"}
				<h2>
					Riddle could not be solved. (tryed {data.steps.length} steps)
				</h2>
			{:else}
				<h2>Riddle simulation</h2>
				<div class="grid">
					<Jug bind:max_value={x_gallons} bind:value={x_result} />
					<Jug bind:max_value={y_gallons} bind:value={y_result} />
				</div>
				<details>
					<summary>Steps detail</summary>
					<table role="grid">
						<thead>
							<tr>
								<th>#</th>
								<th>Jug X Level</th>
								<th>Jug Y Level</th>
							</tr>
						</thead>
						<tbody>
							{#each data.steps as step, index}
								<tr>
									<td>{index}</td>
									<td>{step.jug_x.current_level}</td>
									<td>{step.jug_y.current_level}</td>
								</tr>
							{/each}
						</tbody>
					</table>
				</details>
			{/if}
		{:else if data && data.reason}
			<div class="warning">{data.reason}</div>
		{/if}
	{/await}
</main>

<style>
	.warning {
		color: rgb(227, 85, 85);
	}
</style>
