<template>
	<div>
		<div class="bg-white">
			<Header @toggle-overlay="toggleOverlay" />
			<!-- <Banner v-if="!user" /> -->
			<div
				class="mx-auto xl:w-11/12 2xl:w-9/12 md:w-11/12 pb-10 max-md:w-11/12"
			>
				<slot />
			</div>
		</div>
		<div v-if="overlayIsOpen" @click="toggleOverlay" class="overlay">
			<div
				class="popup absolute top-1/2 left-1/2 translate-x-1/2 -translate-y-1/2 md:w-2/3 max-md:w-10/12 h-2/3 bg-white rounded-xl overflow-y-auto shadow-2xl box-border z-50 border-8 md:p-5 max-md:p-1 border-white"
				id="popup"
				@click.stop
			>
				<div class="sticky mx-auto rounded-sm p-1 -top-5 w-11/12 z-50 bg-white">
					<div
						@click="toggleOverlay"
						class="close cursor-pointer absolute top-0 right-0 bg-slate-100 rounded-lg md:w-10 md:h-10 hover:transform hover:scale-110 transition-all max-md:w-7 max-md:h-7"
					></div>
					<span class="block 2xl:text-4xl lg:text-3xl md:text-xl max-md:text-xl"
						>Выбор региона</span
					>
					<div
						class="relative w-full border-2 border-slate-300 rounded-lg pl-2 mt-4 mb-4"
					>
						<input
							v-model="query"
							type="text"
							placeholder="Поиск"
							class="search bg-white w-11/12 rounded-xl 2xl:h-10 lg:h-8 2xl:placeholder:text-base md:placeholder:text-sm max-md:placeholder:text-sm 2xl:text-base lg:text-sm md:p-2 max-md:p-1 ml-4 outline-none"
						/>
						<svg
							class="absolute block top-1/2 transform -translate-y-1/2"
							width="18"
							height="18"
							viewBox="0 0 18 18"
							fill="none"
							xmlns="http://www.w3.org/2000/svg"
						>
							<path
								d="M15.9667 18L10.1917 11.7C9.73333 12.1 9.20625 12.4167 8.61042 12.65C8.01458 12.8833 7.38056 13 6.70833 13C5.04306 13 3.63383 12.3707 2.48067 11.112C1.3275 9.85333 0.750611 8.316 0.75 6.5C0.75 4.68333 1.32689 3.146 2.48067 1.888C3.63444 0.63 5.04367 0.000666667 6.70833 0C8.37361 0 9.78314 0.629333 10.9369 1.888C12.0907 3.14667 12.6673 4.684 12.6667 6.5C12.6667 7.23333 12.5597 7.925 12.3458 8.575C12.1319 9.225 11.8417 9.8 11.475 10.3L17.25 16.6L15.9667 18ZM6.70833 11C7.85417 11 8.82828 10.5627 9.63067 9.688C10.4331 8.81333 10.8339 7.75067 10.8333 6.5C10.8333 5.25 10.4324 4.18767 9.63067 3.313C8.82889 2.43833 7.85478 2.00067 6.70833 2C5.5625 2 4.58869 2.43767 3.78692 3.313C2.98514 4.18833 2.58394 5.25067 2.58333 6.5C2.58333 7.75 2.98453 8.81267 3.78692 9.688C4.58931 10.5633 5.56311 11.0007 6.70833 11Z"
								fill="#9CA3AF"
							/>
						</svg>
					</div>
				</div>

				<div
					v-if="regions.length > 0"
					class="list overflow-y-auto mt-2 w-11/12 mx-auto"
				>
					<div v-for="(regions, letter) in groupedRegions" :key="letter">
						<h2 class="lg:text-xl md:text-lg font-bold ml-2">{{ letter }}</h2>
						<ul>
							<li>
								<a
									:href="region.link"
									class="block lg:base max-md:text-sm md:text-sm rounded-md w-full hover:bg-indigo-500 hover:text-white transition-all p-2"
									v-for="region in regions"
									:key="region.id"
								>
									{{ region.name }}
								</a>
							</li>
						</ul>
					</div>
				</div>
				<div class="pl-3 mt-2 w-11/12 mx-auto text-slate-600" v-else>
					По запросу "{{ query }}" ничего не найдено
				</div>
			</div>
		</div>
		<!-- <div v-if="noAuthOverlayIsOpen" @click="toggleAuthOverlay" class="overlay">
			<div
				class="popup absolute top-1/2 left-1/2 translate-x-1/2 -translate-y-1/2 w-1/3 min-h-0 p-5 bg-white rounded-xl overflow-y-auto shadow-2xl box-border z-50 border-white"
				id="popup"
				@click.stop
			>
				<div class="">
					<div
						@click="toggleAuthOverlay"
						class="close cursor-pointer absolute top-3 right-3 bg-slate-100 rounded-lg w-5 h-5 hover:transform hover:scale-110 transition-all"
					></div>
					<span
						class="font-bold text-center block 2xl:text-2xl lg:text-xl md:text-lg"
						>Войдите, чтобы добавлять тарифы в избранное</span
					>
					<nuxt-link to="/login"
						><button
							@click="toggleAuthOverlay"
							class="w-full border-2 border-slate-300 rounded-lg mt-5 p-2 hover:bg-indigo-500 hover:text-white transition-all"
						>
							Войти
						</button></nuxt-link
					>
				</div>
			</div>
		</div> -->
	</div>
	<ScrollToTop />
</template>

<script setup>
import axios from 'axios'
import { useAuthStore } from '~/store/index'

/* Регион!!! */
const region = 'Ленинградская область'
const regionForApi = 'piter'

const authStore = useAuthStore()
const user = computed(() => authStore.user)

const screenWidth = ref(0)

onMounted(() => {
	screenWidth.value = window.innerWidth
	window.addEventListener('resize', () => {
		screenWidth.value = window.innerWidth
	})
})

const overlayIsOpen = ref(false)

/* const noAuthOverlayIsOpen = ref(false)

const toggleAuthOverlay = () => {
	noAuthOverlayIsOpen.value = !noAuthOverlayIsOpen.value

	if (noAuthOverlayIsOpen.value) {
		document.body.style.overflow = 'hidden'
	} else {
		document.body.style.overflow = 'auto'
	}
} */

const toggleOverlay = e => {
	overlayIsOpen.value = !overlayIsOpen.value

	if (overlayIsOpen.value) {
		document.body.style.overflow = 'hidden'
	} else {
		query.value = ''
		document.body.style.overflow = 'auto'
	}
}

const regions = ref([])
const query = ref('')

const getRegions = async query => {
	try {
		let { data } = await axios.get(
			`http://127.0.0.1:8000/api/v1/regions?name=*${query}*`
		)
		data = data.filter(region => region.isPublic)
		regions.value = data.sort((a, b) => a.name.localeCompare(b.name, 'ru'))
	} catch (error) {
		console.log(error)
	}
}

const groupedRegions = computed(() => {
	const groups = regions.value.reduce((acc, region) => {
		const firstLetter = region.name[0].toUpperCase()
		if (!acc[firstLetter]) {
			acc[firstLetter] = []
		}
		acc[firstLetter].push(region)
		return acc
	}, {})
	return Object.keys(groups)
		.sort()
		.reduce((acc, letter) => {
			acc[letter] = groups[letter]
			return acc
		}, {})
})

const isMobileFitersShow = ref(false)

const toggleMobileFilters = () => {
	isMobileFitersShow.value = !isMobileFitersShow.value
}

const openMobileFilters = () => {
	if (screenWidth.value < 768) {
		isMobileFitersShow.value = true
	}
}

provide('region', region)
provide('regionForApi', regionForApi)
provide('isMobileFitersShow', isMobileFitersShow)
provide('toggleMobileFilters', toggleMobileFilters)
provide('screenWidth', screenWidth)

watch(query, async query => await getRegions(query))

onMounted(async () => await getRegions(query.value))
onMounted(() => openMobileFilters())

/* provide('noAuthOverlayIsOpen', noAuthOverlayIsOpen) */
</script>

<style scoped>
.overlay {
	position: fixed;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 999;
	background-color: rgba(0, 0, 0, 0.4);
	transition: all 1s ease-in-out;
}
.popup {
	animation: popup 0.5s ease-in-out forwards;
}

.close::before,
.close::after {
	content: '';
	position: absolute;
	top: 50%;
	left: 50%;
	width: 55%;
	height: 2px;
	background-color: #393939;
	transform-origin: center;
}

.close::before {
	transform: translate(-50%, -50%) rotate(45deg);
}

.close::after {
	transform: translate(-50%, -50%) rotate(-45deg);
}

#popup::-webkit-scrollbar {
	width: 5px;
}

#popup::-webkit-scrollbar-track {
	background-color: white;
	border-radius: 5px;
}

#popup::-webkit-scrollbar-thumb {
	border-radius: 5px;
	background: linear-gradient(180deg, #6366f1, #8b5cf6);
}

@keyframes popup {
	0% {
		transform: translateY(-70%) translateX(-50%);
		opacity: 0;
	}
	100% {
		transform: translateY(-50%) translateX(-50%);
		opacity: 1;
	}
}
</style>
