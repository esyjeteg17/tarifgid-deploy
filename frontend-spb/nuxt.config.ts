// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
	app: {
		head: {
			link: [
				{ rel: 'icon', type: 'image/x-icon', href: '/favicon/favicon.ico' },
				{
					rel: 'icon',
					type: 'image/png',
					sizes: '16x16',
					href: '/favicon/favicon-16x16.png',
				},
				{
					rel: 'icon',
					type: 'image/png',
					sizes: '32x32',
					href: '/favicon/favicon-32x32.png',
				},
				{
					rel: 'icon',
					type: 'image/png',
					sizes: '192x192',
					href: '/favicon/android-chrome-192x192.png',
				},
				{
					rel: 'icon',
					type: 'image/png',
					sizes: '512x512',
					href: '/favicon/android-chrome-512x512.png',
				},
				{
					rel: 'apple-touch-icon',
					sizes: '180x180',
					href: '/favicon/apple-touch-icon.png',
				},
				{ rel: 'manifest', href: '/favicon/site.webmanifest' },
				{
					rel: 'mask-icon',
					href: '/favicon/safari-pinned-tab.svg',
					color: '#5bbad5',
				},
				{ rel: 'msapplication-config', href: '/favicon/browserconfig.xml' },
			],
			meta: [
				{ name: 'msapplication-TileColor', content: '#2b5797' },
				{
					name: 'msapplication-TileImage',
					content: '/favicon/mstile-70x70.png',
				},
				{
					name: 'msapplication-TileImage',
					content: '/favicon/mstile-144x144.png',
				},
				{
					name: 'msapplication-TileImage',
					content: '/favicon/mstile-150x150.png',
				},
				{
					name: 'msapplication-TileImage',
					content: '/favicon/mstile-310x150.png',
				},
				{
					name: 'msapplication-TileImage',
					content: '/favicon/mstile-310x310.png',
				},
			],
		},
	},

	colorMode: {
		preference: 'light',
	},

	devtools: { enabled: true },
	css: ['~/assets/css/main.css', 'nprogress/nprogress.css'],

	postcss: {
		plugins: {
			tailwindcss: {},
			autoprefixer: {},
		},
	},

	modules: ['nuxt-yandex-metrika', 'nuxt-gtag', '@pinia/nuxt', '@nuxt/ui'],

	plugins: ['./plugins/nprogress.client.js', './plugins/axios.js'],

	yandexMetrika: {
		id: 'XXXXXX',
		// debug: process.env.NODE_ENV !== "production",
		// delay: 0,
		// cdn: false,
		// verification: null, // Verification in Yandex Webmaster
		// options: {
		//  webvisor: true
		// },
	},

	gtag: {
		id: 'G-XXXXXXXXXX',
	},

	compatibilityDate: '2024-07-16',
})
