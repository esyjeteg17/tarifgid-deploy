<script setup>
import { useHead } from '#app'
import { useAuthStore } from '~/store'

useHead({
	title:
		'Подбор тарифов – сравнить тарифы всех операторов в Москве и Московской области',
	meta: [
		{
			name: 'description',
			content: 'Тарифы',
		},
	],
})
const category = ref('mobile')
const filter = ref('')
const operator = ref([])
const search = ref('')

const gigabytes = ref([0, 99999])

const filtersLoading = ref(false)

const isLoading = ref(true)

const prices = reactive({
	min: '',
	max: '',
})

const firstPrices = {
	min: '',
	max: '',
}

const operators = ref([])

const showSort = ref(false)

const sortIsActive = ref(false)

const networkError = ref(false)

const setShowSort = e => {
	if (e.target.classList.contains('show-sort')) {
		showSort.value = !showSort.value
		sortIsActive.value = !sortIsActive.value
	} else {
		showSort.value = false
		sortIsActive.value = false
	}
}

const setOperators = items => {
	const uniqueOperators = items.filter(
		(item, index, self) =>
			index === self.findIndex(t => t.operator === item.operator)
	)

	operators.value = uniqueOperators.map(item => item.operator)
}

const setFilter = e => {
	filter.value = e.target.value
}

const setPrices = e => {
	if (e.target.id === 'pricemin') {
		prices.min = e.target.value
		document.querySelectorAll('.priceinp').forEach(el => {
			el.checked = false
		})
	}
	if (e.target.id === 'pricemax') {
		prices.max = e.target.value
		document.querySelectorAll('.priceinp').forEach(el => {
			el.checked = false
		})
	}
	if (e.target.id === '1') {
		prices.min = firstPrices.min
		prices.max = `${2 * Math.round(firstPrices.max / 6 / 100) * 100}`
		document.querySelectorAll('.price-input').forEach(el => {
			el.value = ''
		})
	}
	if (e.target.id === '1-2') {
		e.target.value = ''
		prices.min = `${2 * Math.round(firstPrices.max / 6 / 100) * 100}`
		prices.max = `${3 * Math.round(firstPrices.max / 6 / 100) * 100}`
		document.querySelectorAll('.price-input').forEach(el => {
			el.value = ''
		})
	}
	if (e.target.id === '2-3') {
		prices.min = `${3 * Math.round(firstPrices.max / 6 / 100) * 100}`
		prices.max = `${4 * Math.round(firstPrices.max / 6 / 100) * 100}`
		document.querySelectorAll('.price-input').forEach(el => {
			el.value = ''
		})
	}
	if (e.target.id === '3-4') {
		prices.min = `${4 * Math.round(firstPrices.max / 6 / 100) * 100}`
		prices.max = `${5 * Math.round(firstPrices.max / 6 / 100) * 100}`
		document.querySelectorAll('.price-input').forEach(el => {
			el.value = ''
		})
	}
	if (e.target.id === 'more') {
		prices.min = `${5 * Math.round(firstPrices.max / 6 / 100) * 100}`
		prices.max = firstPrices.max
		document.querySelectorAll('.price-input').forEach(el => {
			el.value = ''
		})
	}
}

const resetPrices = () => {
	prices.min = firstPrices.min
	prices.max = firstPrices.max
	document.querySelectorAll('.price-input').forEach(el => {
		el.value = ''
	})
	document.querySelectorAll('.priceinp').forEach(el => {
		el.checked = false
	})
}

const setOperator = e => {
	if (e.target.checked) {
		operator.value.push(e.target.value)
	}
	if (!e.target.checked) {
		operator.value.splice(operator.value.indexOf(e.target.value), 1)
	}
}

const setSearch = e => {
	search.value =
		e.target.value.charAt(0).toUpperCase() + e.target.value.slice(1)
}

const setFirstPrices = items => {
	if (items.length === 0) {
		return
	}
	const maxPrice = items.reduce(
		(max, item) => (item.price > max ? item.price : max),
		0
	)

	prices.max = maxPrice

	const minPrice = items.reduce(
		(min, item) => (item.price < min ? item.price : min),
		items[0].price
	)

	prices.min = minPrice

	firstPrices.min = minPrice
	firstPrices.max = maxPrice
}

const isOnlyFavorite = ref(false)

const favoritesLength = ref(0)

const screenWidth = inject('screenWidth')

const isMobileFitersShow = inject('isMobileFitersShow')
const toggleMobileFilters = inject('toggleMobileFilters')

provide('filter', filter)
provide('category', category)
provide('operator', operator)
provide('search', search)
provide('prices', prices)
provide('operators', operators)
provide('showSort', showSort)
provide('sortIsActive', sortIsActive)
provide('maxPrice', prices.max)
provide('isLoading', isLoading)
provide('firstPrices', firstPrices)
provide('filtersLoading', filtersLoading)
provide('networkError', networkError)
provide('gigabytes', gigabytes)
provide('isOnlyFavorite', isOnlyFavorite)
provide('favoritesLength', favoritesLength)
</script>

<template>
	<div
		@scroll="setShadow"
		@click="e => setShowSort(e)"
		class="relative grid w-full h-full"
		:class="screenWidth < 768 ? '' : 'wrapper'"
	>
		<div
			v-if="screenWidth > 768"
			class="2xl:w-56 lg:w-60 max-md:w-full md:w-52 sticky top-0"
		>
			<Filters
				v-if="!filtersLoading"
				:set-filter="setFilter"
				:set-operator="setOperator"
				:set-search="setSearch"
				:set-prices="setPrices"
				:reset-prices="resetPrices"
			/>
		</div>

		<div v-else>
			<button
				v-if="!isMobileFitersShow"
				@click="toggleMobileFilters"
				class="absolute top-14 right-1 flex items-center text-sm py-1 pr-2 pl-1 border-2 text-slate-500 border-slate-300 rounded-lg"
			>
				<img src="/filters-icon.svg" class="w-3 mr-1" alt="filters" />
				Фильтры
			</button>
			<button
				v-if="isMobileFitersShow"
				@click="toggleMobileFilters"
				class="absolute top-14 right-1 flex items-center text-sm py-1 pr-2 pl-1 border-2 text-slate-500 border-slate-300 rounded-lg"
			>
				<img src="/filters-icon.svg" class="w-3 mr-1" alt="filters" />
				Закрыть фильтры
			</button>

			<Filters
				v-if="isMobileFitersShow"
				:set-filter="setFilter"
				:set-operator="setOperator"
				:set-search="setSearch"
				:set-prices="setPrices"
				:reset-prices="resetPrices"
			/>
		</div>

		<div class="w-full 2xl:pl-8 lg:pl-6 md:pl-4 xl:pt-12 max-md:pt-12 md:pt-8">
			<!-- <ChoiceTabs :category="category" /> -->
			<TarifsCardList
				:set-operators="setOperators"
				:set-filter="setFilter"
				:set-show-sort="setShowSort"
				:set-first-prices="setFirstPrices"
			/>
		</div>
	</div>
</template>

<style scoped>
.wrapper {
	grid-template-columns: 1fr 6fr;
}
</style>
