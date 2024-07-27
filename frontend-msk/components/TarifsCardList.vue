<script setup>
import axios from 'axios'

const props = defineProps({
	setOperators: Function,
	setFilter: Function,
	setShowSort: Function,
	setFirstPrices: Function,
})

const regionForApi = inject('regionForApi')

const gigabytes = inject('gigabytes')

const networkError = inject('networkError')

const filtersLoading = inject('filtersLoading')

const sortIsActive = inject('sortIsActive')

const filterIsChanged = ref(false)

const sortName = ref('Сортировать')

const showSort = inject('showSort')

const showTopTarrifs = ref(false)

const topTarrifs = ref([])

const prices = inject('prices')

const category = inject('category')

const filter = inject('filter')

const operator = inject('operator')

const search = inject('search')

const isOnlyFavorite = inject('isOnlyFavorite')

const favoritesLength = inject('favoritesLength')

const defaultLoadind = [1, 2, 3, 4, 5, 6, 7, 8]
const items = ref([])
let isLoading = inject('isLoading')

const setSortName = e => {
	sortName.value = e.target.dataset.visible
}

const setSort = e => {
	filter.value = e.target.dataset.value
}

const setTopTarrifs = () => {
	if (filter.value === '') {
		showTopTarrifs.value = false
	} else {
		showTopTarrifs.value = true
	}
}

const deleteTopTarrifs = () => {
	topTarrifs.value = []
}

const deleteFilters = () => {
	filter.value = ''
	operator.value = []
	search.value = ''
	prices.min = ''
	prices.max = ''
	sortName.value = 'Сортировать'
	deleteTopTarrifs()
	document.querySelectorAll('.priceinp').forEach(el => {
		el.checked = false
	})
	document.querySelectorAll('.filter-inp').forEach(el => {
		el.checked = false
	})
	document.querySelectorAll('.operator').forEach(el => {
		el.checked = false
	})
	document.querySelectorAll('.search').forEach(el => {
		el.value = ''
	})
	document.querySelectorAll('.price-input').forEach(el => {
		el.value = ''
	})
}

const getItems = async () => {
	try {
		networkError.value = false
		if (operator.value.length === 0) {
			if (prices.max === '') {
				prices.max = '99999'
			}
			const queryString = `http://127.0.0.1:8000/api/v1/${category.value}/${regionForApi}?sortBy=${filter.value}&name=*${search.value}*&price_from=${prices.min}&price_to=${prices.max}`
			let { data } = await axios.get(queryString)
			if (showTopTarrifs.value && data.length > 3 && !isOnlyFavorite.value) {
				topTarrifs.value = data.slice(0, 3)
				data = data.slice(3)
			}
			items.value = data
			getFavorites()
			if (isOnlyFavorite.value) {
				items.value = items.value.filter(item => item.isFavorite)
			}
		} else {
			let queryString = `http://127.0.0.1:8000/api/v1/${category.value}/${regionForApi}?sortBy=${filter.value}&name=*${search.value}*&price_from=${prices.min}&price_to=${prices.max}&operator=`

			operator.value.map(item => {
				queryString += `${item},`
			})

			let { data } = await axios.get(queryString)

			if (showTopTarrifs.value && data.length > 3 && !isOnlyFavorite.value) {
				topTarrifs.value = data.slice(0, 3)
				data = data.slice(3)
			}
			items.value = data
			getFavorites()
			if (isOnlyFavorite.value) {
				items.value = items.value.filter(item => item.isFavorite)
			}
		}
		isLoading.value = false
		favoritesLength.value =
			items.value.filter(item => item.isFavorite).length +
			topTarrifs.value.filter(item => item.isFavorite).length
	} catch (error) {
		networkError.value = true
		console.log(error)
	}
}

let updateScenario = null

onMounted(async () => {
	await getItems()
	props.setOperators(items.value)
	props.setFirstPrices(items.value)
})

watch(filter, async () => {
	if (updateScenario !== 'category') {
		updateScenario = 'filter'
		setTopTarrifs()
		deleteTopTarrifs()
		isLoading.value = true
		await getItems()
		updateScenario = null
	}
})

watch(category, async () => {
	updateScenario = 'category'
	filtersLoading.value = true
	isLoading.value = true
	deleteFilters()
	setTopTarrifs()
	await getItems()
	await props.setOperators(items.value)
	await props.setFirstPrices(items.value)
	filtersLoading.value = false
	updateScenario = null
})

watch(
	operator,
	() => {
		if (updateScenario !== 'category') {
			updateScenario = 'operator'
			deleteTopTarrifs()
			setTopTarrifs()
			isLoading.value = true
			getItems()
			updateScenario = null
		}
	},
	{ deep: true }
)

watch(search, async () => {
	if (updateScenario !== 'category') {
		updateScenario = 'search'
		deleteTopTarrifs()
		setTopTarrifs()
		isLoading.value = true
		await getItems()
		updateScenario = null
	}
})

watch(
	prices,
	async () => {
		if (updateScenario !== 'category') {
			updateScenario = 'prices'
			deleteTopTarrifs()
			isLoading.value = true
			await getItems()
			setTopTarrifs()
			updateScenario = null
		}
	},
	{ deep: true }
)

const getFavorites = () => {
	try {
		const favorites = JSON.parse(localStorage.getItem('favorites')) || []
		items.value.map(item => {
			if (favorites.includes(item.id)) {
				item.isFavorite = true
			}
		})
		if (topTarrifs.value.length > 0) {
			topTarrifs.value.map(item => {
				if (favorites.includes(item.id)) {
					item.isFavorite = true
				}
			})
		}
	} catch (error) {
		console.error('An error occurred while retrieving favorites:', error)
		return []
	}
}

const addFavorite = async id => {
	try {
		const favorites = JSON.parse(localStorage.getItem('favorites')) || []
		if (!favorites.includes(id)) {
			favorites.push(id)
			localStorage.setItem('favorites', JSON.stringify(favorites))
			items.value.map(item => {
				if (item.id === id) {
					item.isFavorite = true
				}
			})
			if (topTarrifs.value.length > 0) {
				topTarrifs.value.map(item => {
					if (item.id === id) {
						item.isFavorite = true
					}
				})
			}
		} else {
			favorites.splice(favorites.indexOf(id), 1)
			localStorage.setItem('favorites', JSON.stringify(favorites))
			items.value.map(item => {
				if (item.id === id) {
					item.isFavorite = false
				}
			})
			if (topTarrifs.value.length > 0) {
				topTarrifs.value.map(item => {
					if (item.id === id) {
						item.isFavorite = false
					}
				})
			}
			getItems()
		}
		favoritesLength.value =
			items.value.filter(item => item.isFavorite).length +
			topTarrifs.value.filter(item => item.isFavorite).length
	} catch (error) {
		console.error('An error occurred while adding favorites:', error)
	}
}

const showOnlyFavorite = () => {
	const favorites = JSON.parse(localStorage.getItem('favorites')) || []
	items.value.push(...topTarrifs.value)
	showTopTarrifs.value = false
	items.value = items.value.filter(item => favorites.includes(item.id))
}

provide('addFavorite', addFavorite)
watch(isOnlyFavorite, async () => {
	if (!isOnlyFavorite.value) {
		deleteTopTarrifs()
		setTopTarrifs()
		isLoading.value = true
		await getItems()
	} else {
		showOnlyFavorite()
		deleteTopTarrifs()
		setTopTarrifs()
		isLoading.value = true
		await getItems()
	}
})
watch(favoritesLength, async () => {
	if (favoritesLength.value === 0) {
		isOnlyFavorite.value = false
		document.querySelector('#fav').checked = false
		await getItems()
	}
})

/* watch(gigabytes, async () => {
  if (updateScenario !== "category") {
    updateScenario = "gigabytes";
    deleteTopTarrifs();
    isLoading.value = true;
    await getItems();
    setTopTarrifs();
    updateScenario = null;
  }
}); */
</script>

<template>
	<div class="w-full">
		<div class="flex">
			<div class="flex flex-col items-center md:w-64 max-md:w-52 relative">
				<div
					:class="
						!sortIsActive
							? 'sort show-sort relative block md:mt-8 md:w-64 max-md:w-52 bg-white border-2 border-slate-300 px-3 2xl:py-2 lg:py-1 md:py-0.5 max-md:py-0.5 max-md:mt-2 rounded-lg outline-none cursor-pointer hover:border-indigo-500 transition-all focus:border-indigo-500 appearance-none ml-2 placeholder:text-white'
							: 'sort-active show-sort relative block md:mt-8 max-md:mt-2 md:w-64 max-md:w-52 bg-white border-2 border-indigo-500 cursor-pointer px-3 2xl:py-2 lg:py-1 md:py-0.5 max-md:py-0.5 rounded-lg outline-none appearance-none ml-2 placeholder:text-white'
					"
				>
					<span
						class="show-sort select-none text-slate-500 2xl:text-base md:text-sm max-md:text-sm"
						>{{ sortName }}</span
					>
					<input
						type="text"
						v-model="filter"
						readonly
						class="absolute bg-gray-50 w-0 h-0 left-0 select-none hidden appearance-none -z-10"
					/>
				</div>

				<ul
					v-if="showSort"
					class="sort-anim flex flex-col ml-2 items-center mt-2 absolute w-full shadow-[0_0_12px_0_rgba(0,0,0,0.1)] md:top-16 max-md:top-9 min-h-0 px-2 rounded-lg cursor-pointer py-0 bg-[#FFFFFF] z-10 overflow-hidden"
				>
					<li
						class="py-1 border-b border-slate-200 text-slate-800 2xl:text-base md:text-sm max-md:text-sm text-left md:px-3 max-md:px-2 md:w-64 max-md:w-52 hover:text-white hover:bg-indigo-500 transition-all last:border-none"
						data-value="price"
						data-visible="Сначала дешевле"
						@click="
							e => {
								setSort(e)
								setSortName(e)
							}
						"
					>
						Сначала дешевле
					</li>
					<li
						class="py-1 border-b border-slate-200 text-slate-800 2xl:text-base md:text-sm text-left px-3 max-md:px-2 max-md:text-sm md:w-64 max-md:w-52 hover:text-white hover:bg-indigo-500 transition-all last:border-none"
						data-value="-price"
						data-visible="Сначала дороже"
						@click="
							e => {
								setSort(e)
								setSortName(e)
							}
						"
					>
						Сначала дороже
					</li>
					<li
						v-if="
							category === 'mobile' ||
							category === 'modems' ||
							category === 'internet' ||
							category === 'smart'
						"
						class="py-1 border-b border-slate-200 text-slate-800 2xl:text-base md:text-sm text-left px-3 max-md:px-2 max-md:text-sm md:w-64 max-md:w-52 hover:text-white hover:bg-indigo-500 transition-all last:border-none"
						data-value="-gigabytes"
						data-visible="Сначала больше ГБ"
						@click="
							e => {
								setSort(e)
								setSortName(e)
							}
						"
					>
						Сначала больше ГБ
					</li>
					<li
						v-if="category === 'mobile' || category === 'smart'"
						class="py-1 border-b border-slate-200 text-slate-800 2xl:text-base md:text-sm text-left px-3 max-md:px-2 max-md:text-sm md:w-64 max-md:w-52 hover:text-white hover:bg-indigo-500 transition-all last:border-none"
						data-value="-minutes"
						data-visible="Сначала больше минут"
						@click="
							e => {
								setSort(e)
								setSortName(e)
							}
						"
					>
						Сначала больше минут
					</li>
					<li
						v-if="category === 'mobile' || category === 'smart'"
						class="py-1 border-b border-slate-200 text-slate-800 2xl:text-base md:text-sm text-left px-3 max-md:px-2 max-md:text-sm md:w-64 max-md:w-52 hover:text-white hover:bg-indigo-500 transition-all last:border-none"
						data-value="-sms"
						data-visible="Сначала больше SMS"
						@click="
							e => {
								setSort(e)
								setSortName(e)
							}
						"
					>
						Сначала больше SMS
					</li>
				</ul>
			</div>
		</div>

		<div class="w-full" v-if="topTarrifs.length">
			<div v-if="showTopTarrifs" class="top-wrapper overflow-visible">
				<h2
					class="top-text 2xl:text-3xl xl:text-2xl md:text-xl max-md:text-xl font-bold text-left block bg-clip-text bg-gradient-to-r from-indigo-500 to-violet-500 2xl:mt-8 md:mt-4 max-md:mt-4 uppercase"
				>
					Самые подходящие тарифы
				</h2>

				<div
					class="rounded-2xl top relative 2xl:mt-8 md:mt-2 w-full 2xl:py-5 g-py-4 md:py-2 bg-gradient-to-r from-indigo-500 to-violet-500 min-h-[0px] overflow-visible"
				>
					<TopBg :top-tarrifs="topTarrifs" />
				</div>

				<h2
					class="top-text 2xl:text-3xl xl:text-2xl md:text-xl max-md:text-xl font-bold text-left block bg-clip-text bg-gradient-to-r from-indigo-500 to-violet-500 2xl:mt-8 md:mt-4 max-md:mt-4 uppercase"
				>
					Другие тарифы
				</h2>
			</div>
		</div>

		<div
			class="not-found flex flex-col mt-10 justify-center"
			v-if="networkError"
		>
			<p
				class="2xl:text-3xl lg:text-2xl md:text-xl max-md:text-xl text-center uppercase w-full text-slate-800"
			>
				нет сети. Проверьте интернет
			</p>
			<div class="2xl:h-[500px] md:h-[300px] max-md:h-[250px]">
				<svg
					class="w-full h-full"
					version="1.1"
					id="error-404-img"
					xmlns="http://www.w3.org/2000/svg"
					xmlns:xlink="http://www.w3.org/1999/xlink"
					x="0px"
					y="0px"
					viewBox="0 0 344.7 276.7"
					style="enable-background: new 0 0 344.7 276.7"
					xml:space="preserve"
				>
					<g id="decorations">
						<polygon
							class="st0"
							points="245,52.8 241.7,49.5 238.5,52.6 235.4,49.5 232.1,52.8 235.2,55.9 232.1,59.1 235.4,62.4 238.5,59.2
		241.7,62.4 245,59.1 241.8,55.9 	"
						/>
						<polygon
							class="st0"
							points="42.7,172 39.4,168.7 36.2,171.8 33.1,168.7 29.8,172 32.9,175.1 29.8,178.3 33.1,181.6 36.2,178.4
		39.4,181.6 42.7,178.3 39.5,175.1 	"
						/>
						<polygon
							class="st0"
							points="102.9,30.8 99.6,27.5 96.4,30.7 93.3,27.5 90,30.8 93.1,34 90,37.2 93.3,40.5 96.4,37.3 99.6,40.5
		102.9,37.2 99.8,34 	"
						/>
						<polygon
							class="st0"
							points="311,196.3 307.7,192.9 304.5,196.1 301.4,192.9 298.1,196.3 301.2,199.4 298.1,202.6 301.4,205.9
		304.5,202.7 307.7,205.9 311,202.6 307.9,199.4 	"
						/>
						<g>
							<path
								class="st0"
								d="M42.7,67.2c-2.7,0-4.8-2.2-4.8-4.8c0-2.7,2.2-4.8,4.8-4.8c2.7,0,4.8,2.2,4.8,4.8
			C47.5,65.1,45.4,67.2,42.7,67.2z M42.7,59.6c-1.6,0-2.8,1.3-2.8,2.8s1.3,2.8,2.8,2.8s2.8-1.3,2.8-2.8S44.3,59.6,42.7,59.6z"
							/>
						</g>
						<g>
							<path
								class="st0"
								d="M183.1,23.3c-2.7,0-4.8-2.2-4.8-4.8s2.2-4.8,4.8-4.8c2.7,0,4.8,2.2,4.8,4.8S185.8,23.3,183.1,23.3z
			 M183.1,15.7c-1.6,0-2.8,1.3-2.8,2.8s1.3,2.8,2.8,2.8s2.8-1.3,2.8-2.8S184.7,15.7,183.1,15.7z"
							/>
						</g>
						<g>
							<path
								class="st0"
								d="M318.6,91c-2.7,0-4.8-2.2-4.8-4.8c0-2.7,2.2-4.8,4.8-4.8c2.7,0,4.8,2.2,4.8,4.8C323.5,88.9,321.3,91,318.6,91
			z M318.6,83.4c-1.6,0-2.8,1.3-2.8,2.8s1.3,2.8,2.8,2.8s2.8-1.3,2.8-2.8S320.2,83.4,318.6,83.4z"
							/>
						</g>
						<g>
							<path
								class="st0"
								d="M257,170.8c-2.7,0-4.8-2.2-4.8-4.8c0-2.7,2.2-4.8,4.8-4.8c2.7,0,4.8,2.2,4.8,4.8
			C261.8,168.7,259.6,170.8,257,170.8z M257,163.2c-1.6,0-2.8,1.3-2.8,2.8s1.3,2.8,2.8,2.8s2.8-1.3,2.8-2.8S258.5,163.2,257,163.2z"
							/>
						</g>
						<g>
							<path
								class="st0"
								d="M90,232c-2.7,0-4.8-2.2-4.8-4.8c0-2.7,2.2-4.8,4.8-4.8c2.7,0,4.8,2.2,4.8,4.8C94.8,229.8,92.6,232,90,232z
			 M90,224.3c-1.6,0-2.8,1.3-2.8,2.8s1.3,2.8,2.8,2.8s2.8-1.3,2.8-2.8S91.5,224.3,90,224.3z"
							/>
						</g>
						<circle class="st0" cx="98.9" cy="65.3" r="9" />
						<circle class="st0" cx="103.3" cy="168.8" r="4.5" />
						<path
							class="st0"
							d="M332.5,154.2c0,2.5-2,4.5-4.5,4.5s-4.5-2-4.5-4.5c0-2.5,2-4.5,4.5-4.5S332.5,151.8,332.5,154.2z"
						/>
						<path
							class="st0"
							d="M17.3,96.3c0,2.5-2,4.5-4.5,4.5c-2.5,0-4.5-2-4.5-4.5s2-4.5,4.5-4.5C15.3,91.8,17.3,93.9,17.3,96.3z"
						/>
						<path
							class="st0"
							d="M243.1,96.3c0,2.5-2,4.5-4.5,4.5c-2.5,0-4.5-2-4.5-4.5s2-4.5,4.5-4.5C241,91.8,243.1,93.9,243.1,96.3z"
						/>
						<circle class="st0" cx="229.1" cy="222.3" r="6.8" />
					</g>
					<g id="_x34_-gauche">
						<g class="st1">
							<path
								class="st0"
								d="M60.6,168.4v-21.1H19.3v-16.8l47.4-60.8h12.9v60.7H92v17H79.5v21.1H60.6z M38.2,130.3h24.5v-32L38.2,130.3z"
							/>
						</g>
						<g>
							<path
								class="st2"
								d="M58.6,166.4v-21.1H17.3v-16.8l47.4-60.8h12.9v60.7H90v17H77.5v21.1H58.6z M36.2,128.3h24.5v-32L36.2,128.3z"
							/>
						</g>
					</g>
					<path
						id="ombre-loupe"
						class="st3"
						d="M238.6,173l0.4-0.3c0.6-0.5,0.6-1.4,0.1-1.9l-7.6-8.3c7.8-9.8,12.7-22.1,13.3-35.6
	c1.5-34.1-24.9-62.9-58.9-64.4c-34.1-1.5-62.9,24.9-64.4,58.9c-1.5,34.1,24.9,62.9,58.9,64.4c13.5,0.6,26.2-3.2,36.7-10.1l7.6,8.3
	c0.5,0.6,1.4,0.6,1.9,0.1l0.4-0.3l56.2,61.4h21.4L238.6,173z"
					/>
					<g id="_x34_-droite">
						<g class="st1">
							<path
								class="st0"
								d="M281.3,168.4v-21.1H240v-16.8l47.4-60.8h12.9v60.7h12.4v17h-12.4v21.1H281.3z M259,130.3h24.5v-32L259,130.3z
			"
							/>
						</g>
						<g>
							<path
								class="st2"
								d="M279.3,166.4v-21.1H238v-16.8l47.4-60.8h12.9v60.7h12.4v17h-12.4v21.1H279.3z M257,128.3h24.5v-32L257,128.3z
			"
							/>
						</g>
					</g>

					<g id="loupe">
						<path
							class="st4"
							d="M311.4,252.6L219.8,161L208,172.8l91.6,91.6c3.4,3.4,9.1,3.2,12.2-0.5h0C314.6,260.5,314.4,255.6,311.4,252.6z
		"
						/>
						<path
							class="st5"
							d="M199.5,167.1l11.1,11.1c0.6,0.6,1.5,0.6,2,0l12.5-12.5c0.6-0.6,0.6-1.5,0-2l-11.1-11.1L199.5,167.1z"
						/>
						<polygon
							class="st6"
							points="215.8,154.2 217.2,155.7 205.4,173 200.2,167.8 	"
						/>
						<polygon
							class="st7"
							points="213,177.8 224.8,166 225.6,166.8 216.4,181.1 	"
						/>
						<path
							class="st8"
							d="M164,51.9c-36,0-65.1,29.2-65.1,65.1s29.2,65.1,65.1,65.1s65.1-29.2,65.1-65.1S200,51.9,164,51.9z M164,168.7
		c-28.5,0-51.7-23.1-51.7-51.7c0-28.5,23.1-51.7,51.7-51.7s51.7,23.1,51.7,51.7C215.7,145.5,192.5,168.7,164,168.7z"
						/>
						<circle class="st9" cx="164" cy="117" r="51.7" />
						<path
							class="st2"
							d="M129.7,82.7c-7.5,7.5-12,15.1-10,17c1.9,1.9,9.6-2.6,17-10c7.5-7.5,12-15.1,10-17
		C144.8,70.7,137.2,75.2,129.7,82.7z"
						/>
					</g>
				</svg>
			</div>
		</div>

		<div
			class="not-found flex flex-col mt-10 justify-center"
			v-else-if="items.length === 0 && !isLoading"
		>
			<p
				class="2xl:text-3xl lg:text-2xl md:text-xl max-md:text-xl text-center uppercase w-full text-slate-800"
			>
				Нет подходящих тарифов
			</p>
			<img
				src="/not-found.png"
				class="select-none 2xl:h-[500px] lg:h-[300px] object-contain"
				alt="not found"
			/>
			<div
				class="absolute 2xl:w-[200px] md:w-[100px] md:h-[100px] 2xl:h-[200px] md:m-[100px] 2xl:m-[150px] 2xl:top-1/3 2xl:left-1/3 md:top-6/12 md:left-9/12 hidden"
			>
				<img
					src="/glass.png"
					alt="glass"
					class="glass absolute 2xl:h-[200px] md:h-[100px]"
				/>
			</div>
		</div>

		<div v-else class="">
			<ul
				v-if="!isLoading"
				class="relative ul-anim 2xl:mt-8 md:mt-2 grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 max-md:grid-cols-2 max-md:mt-2 w-full"
			>
				<TarifsCardItem
					v-for="item in items"
					:id="item.id"
					:key="item.id"
					:name="item.name"
					:price="item.price"
					:minutes="item.minutes"
					:gb="item.gigabytes"
					:img="item.img"
					:bonus="item.bonus"
					:sms="item.sms"
					:link="item.link"
					:operator="item.head"
					:descr="item.bonustext"
					:speed="item.speed"
					:tv="item.tv"
					:is-favorite="item.isFavorite"
					:is-loading="isLoading"
					@add-favorite="addFavorite"
				/>
			</ul>
			<ul
				v-else
				class="mt-8 grid xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2 w-full max-md:grid-cols-2"
			>
				<TarifsCardItem
					v-for="item in defaultLoadind"
					:is-loading="isLoading"
					:key="item"
				/>
			</ul>
		</div>
	</div>
</template>

<style scoped>
#error-404-img {
	max-width: 700px;
	display: block;
	margin: 0 auto;
}

#loupe {
	animation: bounceInUp 2s ease forwards;
}

#ombre-loupe {
	animation: fadeIn 2s 3s ease forwards;
}

#_x34_-gauche,
#_x34_-droite,
#ombre-loupe,
#decorations {
	opacity: 0;
}

#_x34_-gauche,
#_x34_-droite {
	animation: fadeIn 2s ease forwards;
}

#_x34_-gauche {
	animation-delay: 1s;
}

#_x34_-droite {
	animation-delay: 2s;
}

#decorations {
	transform-origin: center;
	animation: fadeIn 2s ease forwards, rotate-grow 50s linear infinite alternate;
	animation-delay: 4s;
}

@-webkit-keyframes rotate-grow {
	from {
		-webkit-transform: rotate(0) scale(0.5);
		transform: rotate(0) scale(0.5);
	}

	to {
		-webkit-transform: rotate(360deg) scale(0.7);
		transform: rotate(360deg) scale(0.7);
	}
}

@keyframes rotate-grow {
	from {
		-webkit-transform: rotate(0) scale(0.5);
		transform: rotate(0) scale(0.5);
	}

	to {
		-webkit-transform: rotate(360deg) scale(0.7);
		transform: rotate(360deg) scale(0.7);
	}
}

@-webkit-keyframes fadeInLeft {
	from {
		opacity: 0;
		-webkit-transform: translate3d(-100%, 0, 0);
		transform: translate3d(-100%, 0, 0);
	}

	to {
		opacity: 1;
		-webkit-transform: translate3d(0, 0, 0);
		transform: translate3d(0, 0, 0);
	}
}
@-webkit-keyframes fadeInRight {
	from {
		opacity: 0;
		-webkit-transform: translate3d(100%, 0, 0);
		transform: translate3d(100%, 0, 0);
	}

	to {
		opacity: 1;
		-webkit-transform: translate3d(0, 0, 0);
		transform: translate3d(0, 0, 0);
	}
}

@keyframes fadeInRight {
	from {
		opacity: 0;
		-webkit-transform: translate3d(100%, 0, 0);
		transform: translate3d(100%, 0, 0);
	}

	to {
		opacity: 1;
		-webkit-transform: translate3d(0, 0, 0);
		transform: translate3d(0, 0, 0);
	}
}

@keyframes fadeInLeft {
	from {
		opacity: 0;
		-webkit-transform: translate3d(-100%, 0, 0);
		transform: translate3d(-100%, 0, 0);
	}

	to {
		opacity: 1;
		-webkit-transform: translate3d(0, 0, 0);
		transform: translate3d(0, 0, 0);
	}
}

@-webkit-keyframes fadeIn {
	from {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

@keyframes fadeIn {
	from {
		opacity: 0;
	}

	to {
		opacity: 1;
	}
}

@-webkit-keyframes bounceInUp {
	from,
	60%,
	75%,
	90%,
	to {
		-webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
		animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
	}

	from {
		opacity: 0;
		-webkit-transform: translate3d(0, 3000px, 0);
		transform: translate3d(0, 3000px, 0);
	}

	60% {
		opacity: 1;
		-webkit-transform: translate3d(0, -20px, 0);
		transform: translate3d(0, -20px, 0);
	}

	75% {
		-webkit-transform: translate3d(0, 10px, 0);
		transform: translate3d(0, 10px, 0);
	}

	90% {
		-webkit-transform: translate3d(0, -5px, 0);
		transform: translate3d(0, -5px, 0);
	}

	to {
		-webkit-transform: translate3d(0, 0, 0);
		transform: translate3d(0, 0, 0);
	}
}

@keyframes bounceInUp {
	from,
	60%,
	75%,
	90%,
	to {
		-webkit-animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
		animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
	}

	from {
		opacity: 0;
		-webkit-transform: translate3d(0, 3000px, 0);
		transform: translate3d(0, 3000px, 0);
	}

	60% {
		opacity: 1;
		-webkit-transform: translate3d(0, -20px, 0);
		transform: translate3d(0, -20px, 0);
	}

	75% {
		-webkit-transform: translate3d(0, 10px, 0);
		transform: translate3d(0, 10px, 0);
	}

	90% {
		-webkit-transform: translate3d(0, -5px, 0);
		transform: translate3d(0, -5px, 0);
	}

	to {
		-webkit-transform: translate3d(0, 0, 0);
		transform: translate3d(0, 0, 0);
	}
}

.bounceInUp {
	-webkit-animation-name: bounceInUp;
	animation-name: bounceInUp;
}

.st0 {
	fill: #6366f1;
}
.st1 {
	opacity: 0.2;
}
.st2 {
	fill: #6366f1;
}
.st3 {
	fill: rgba(132, 121, 114, 0.4);
}
.st4 {
	fill: #6366f1;
}
.st5 {
	fill: #6366f1;
}
.st6 {
	fill: #6366f1;
}
.st7 {
	opacity: 0.64;
	fill: #6366f1;
}
.st8 {
	fill: #6366f1;
}
.st9 {
	opacity: 0.8;
	fill: #6366f1;
}

/* .top {
	overflow: ;
} */

.top-wrapper {
	animation: top-anim 1.5s ease-in-out;
	animation-fill-mode: forwards;
}

.sort-anim {
	animation: sort-anim 0.3s ease-in-out forwards;
}

.top-text {
	color: transparent;
}

.sort::after {
	content: '';
	position: absolute;
	top: 50%;
	transform: translateY(-50%);
	right: 3%;
	width: 13px;
	height: 7px;
	background: url('/sort-arrow.svg') center center/cover no-repeat;
}

.sort-active::after {
	content: '';
	position: absolute;
	top: 50%;
	transform: translateY(-50%) rotate(180deg);
	right: 3%;
	width: 13px;
	height: 7px;
	background: url('/sort-arrow.svg') center center/cover no-repeat;
}

.not-found {
	animation: not-found-anim 1s ease-in-out;
	animation-fill-mode: forwards;
}

.glass {
	animation: glass-anim 3s linear infinite;
}

@keyframes sort-anim {
	0% {
		transform: translateY(-3%);
		opacity: 0;
	}
	100% {
		transform: translateY(0);
		opacity: 1;
	}
}

@keyframes not-found-anim {
	0% {
		opacity: 0;
	}
	100% {
		opacity: 1;
	}
}

@keyframes top-anim {
	0% {
		opacity: 0;
		transform: translateY(-7%);
	}
	50% {
		opacity: 0;
		transform: translateY(-7%);
	}
	100% {
		opacity: 1;
		transform: translateY(0);
	}
}

@keyframes glass-anim {
	from {
		transform: rotate(0deg) translateX(30px) rotate(0deg);
	}
	to {
		transform: rotate(360deg) translateX(30px) rotate(-360deg);
	}
}
</style>
