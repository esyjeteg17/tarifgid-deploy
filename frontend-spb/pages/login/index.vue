<template>
	<div>
		<div
			class="mt-20 flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8"
		>
			<div class="md:mx-auto md:w-full md:max-w-sm">
				<img class="mx-auto h-10 w-auto" src="/logo2.svg" alt="Your Company" />
				<h2
					class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900"
				>
					Войдите в аккаунт
				</h2>
			</div>

			<div class="mt-10 md:mx-auto md:w-full md:max-w-sm">
				<form class="space-y-6" @submit.prevent="login">
					<div>
						<label
							for="username"
							class="block text-sm font-medium leading-6 text-gray-900"
							>Имя пользователя</label
						>
						<div class="mt-2">
							<input
								id="username"
								name="username"
								type="text"
								autocomplete="username"
								required="true"
								v-model="username"
								class="p-3 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 md:text-sm md:leading-6"
							/>
						</div>
					</div>

					<div>
						<div class="flex items-center justify-between">
							<label
								for="password"
								class="block text-sm font-medium leading-6 text-gray-900"
								>Пароль</label
							>
							<!-- <div class="text-sm">
								<a
									href="#"
									class="font-semibold text-indigo-600 hover:text-indigo-500"
									>Забыли пароль?</a
								>
							</div> -->
						</div>
						<div class="mt-2">
							<input
								id="password"
								name="password"
								type="password"
								autocomplete="current-password"
								required="true"
								v-model="password"
								class="p-3 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 md:text-sm md:leading-6"
							/>
						</div>
					</div>

					<span class="text-red-500 block mx-auto text-center text-sm">{{
						error
					}}</span>

					<div>
						<button
							type="submit"
							class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
						>
							Войти
						</button>
					</div>
				</form>

				<p class="mt-10 text-center text-sm text-gray-500">
					Впервые у нас?
					<nuxt-link
						href="/register"
						class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500"
						>Зарегистрироваться</nuxt-link
					>
				</p>
			</div>
		</div>
	</div>
</template>

<script setup>
import { useHead } from '#app'
import { useAuthStore } from '~/store/index'

useHead({
	title: 'Войдите в аккаунт',
	meta: [
		{
			name: 'description',
			content: 'Войдите в аккаунт',
		},
	],
})

const authStore = useAuthStore()
const username = ref('')
const password = ref('')
const { $api } = useNuxtApp()
const router = useRouter()
const error = ref('')

const login = async () => {
	try {
		const response = await $api.post('http://127.0.0.1:8000/api/token/', {
			username: username.value,
			password: password.value,
		})
		const data = response.data
		authStore.setToken(data.access)
		await authStore.fetchUser()
		router.push('/')
	} catch (e) {
		console.error(e)
		error.value = 'Неверное имя пользователя или пароль'
	}
}
</script>

<style lang="scss" scoped></style>
