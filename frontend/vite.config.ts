import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		proxy: {
			'/left': 'http://127.0.0.1:5000',
			'/right': 'http://127.0.0.1:5000',
			'/move': 'http://127.0.0.1:5000',
			'/place': 'http://127.0.0.1:5000'
		}
	}
});
