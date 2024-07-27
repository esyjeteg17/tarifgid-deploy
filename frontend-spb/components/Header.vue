<template>
	<header
		class="w-full md:shadow-sm absolute top-0 left-0 z-10 bg-white md:py-3 max-md:py-3"
	>
		<div
			class="mx-auto relative w-full flex justify-between items-center xl:w-11/12 2xl:w-9/12 md:w-11/12 max-md:w-11/12"
		>
			<div class="block">
				<nuxt-link to="/" class="flex items-center"
					><img class="xl:h-8 md:h-7 max-md:h-6" src="/logo2.svg" alt="logo" />
					<p
						class="md:ml-2 max-md:ml-1 2xl:text-lg md:text-md max-md:text-sm text-slate-900 font-bold"
					>
						тариф<span class="text-indigo-500">гид</span>
					</p></nuxt-link
				>
			</div>

			<div class="flex relative">
				<img
					class="md:w-4 md:h-4 max-md:h-3 max-md:mt-1 max-md:w-3 md:mr-1"
					src="/geo.png"
					alt="location"
				/>
				<button
					class="text-sm hover:text-indigo-500 transition-all"
					@click="toggleOverlay"
				>
					{{ region }}
				</button>
				<div
					v-if="isRegionQuestionOpen"
					class="region-question mt-2 absolute top-full left-1/3 -translate-x-1/2 right-12 p-4 rounded-xl shadow-2xl bg-white w-80 border-2 border-slate-100"
				>
					<span class="text-sm"
						>Ваш регион <b>{{ region }}?</b></span
					>
					<div class="flex w-full justify-between mt-3">
						<button
							@click="isRegionQuestionOpen = false"
							class="text-sm rounded-md bg-indigo-500 px-3 py-2 text-white"
						>
							Да, верно
						</button>
						<button
							@click="toggleOverlay"
							class="text-sm underline underline-offset-2 decoration-dashed"
						>
							Нет, изменить регион
						</button>
					</div>
				</div>
			</div>

			<!-- <nav class="ml-auto">
				<ul class="ml-auto flex justify-end h-full items-center">
					<li>
						<nuxt-link to="/sravni"
							><button
								class="border-2 2xl:px-7 xl:px-5 lg:px-3 text-sm xl:py-2 lg:py-1 bg-white rounded-3xl border-slate-400 text-slate-700 box-border hover:bg-indigo-500 hover:text-white transition-all hover:border-opacity-0"
							>
								Подобрать тариф
							</button></nuxt-link
						>
					</li>
					<li>
						<nuxt-link to="/sravni"
							><button
								class="border-2 2xl:px-7 xl:px-5 lg:px-3 text-sm xl:py-2 lg:py-1 bg-white rounded-3xl border-slate-400 text-slate-700 box-border hover:bg-indigo-500 hover:text-white transition-all hover:border-opacity-0"
							>
								Главная
							</button></nuxt-link
						>
					</li>
					<li v-if="!user">
						<nuxt-link to="/login">
							<button
								class="border-2 2xl:px-7 md:px-6 text-sm font-md md:py-1 2xl:py-2 bg-white rounded-3xl border-slate-400 text-slate-700 box-border hover:bg-indigo-500 hover:text-white transition-all min-h-0 hover:border-opacity-0"
							>
								Войти
							</button>
						</nuxt-link>
					</li>
					<li v-else>
						<button
							class="ml-2 border-2 px-7 text-sm font-md py-1 bg-white rounded-3xl border-slate-400 text-slate-700 box-border hover:bg-indigo-500 hover:text-white transition-all h-10 hover:border-opacity-0"
						>
							Выйти, {{ user.username }}
						</button>
					</li>
				</ul>
			</nav> -->
		</div>
	</header>
</template>

<script setup>
import { computed } from 'vue'
import { useAuthStore } from '~/store/index'

const region = inject('region')

const authStore = useAuthStore()
const user = computed(() => authStore.user)

const emit = defineEmits(['toggle-overlay'])

const toggleOverlay = () => {
	isRegionQuestionOpen.value = false
	emit('toggle-overlay')
}

const isRegionQuestionOpen = ref(true)
</script>

<style scoped>
.region-question {
	animation: question 0.3s ease-in-out;
}

@keyframes question {
	from {
		opacity: 0;
	}
	to {
		opacity: 1;
	}
}
</style>
