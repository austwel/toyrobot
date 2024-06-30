import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		proxy: {
			'/left': 'https://toyrobot-webapp.azurewebsites.net',
			'/right': 'https://toyrobot-webapp.azurewebsites.net',
			'/move': 'https://toyrobot-webapp.azurewebsites.net',
			'/place': 'https://toyrobot-webapp.azurewebsites.net',
			'/report': 'https://toyrobot-webapp.azurewebsites.net',
		}
	}
});
