import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		proxy: {
			'/left': 'http://localhost:5000',
			'/right': 'http://localhost:5000',
			'/move': 'http://localhost:5000',
			'/place': 'http://localhost:5000',
			'/report': 'http://localhost:5000',
		}
	}
});
