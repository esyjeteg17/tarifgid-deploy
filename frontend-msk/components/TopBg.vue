<script setup>
const props = defineProps({
	topTarrifs: Array,
})

const addFavorite = inject('addFavorite')
</script>

<template>
	<div
		class="flex w-full items-center h-full justify-center xl:px-16 lg:px-4 overflow-visible max-md:py-2 max-md:mt-2 max-md:mb-2"
	>
		<!-- <img
			src="/top-bg.png"
			class="absolute h-[300%] w-full top[-100%] left-0 m-0 border-0"
			alt="bacground"
		/> -->
		<div class="absolute w-full h-full overflow-hidden rounded-2xl">
			<FrameTop />
		</div>

		<UCarousel
			v-if="topTarrifs.length"
			v-slot="{ item }"
			:items="topTarrifs"
			:ui="{
				item: 'basis-full md:basis-2/3 md:basis-1/1 overflow-visible',
				container: 'md:max-w-[450px] w-full mx-auto max-md:max-w-[350px]',
			}"
			:prev-button="{
				color: 'gray',
				icon: 'i-heroicons-arrow-left-20-solid',
				class: '-left-10',
			}"
			:next-button="{
				color: 'gray',
				icon: 'i-heroicons-arrow-right-20-solid',
				class: '-right-10',
			}"
			arrows
			class="w-9/12 mx-auto lg:hidden relative overflow-visible"
		>
			<TarifsCardItem
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
				@add-favorite="addFavorite"
				class="w-full"
				draggable="false"
			/>
		</UCarousel>

		<ul
			class="relative overdivw-visible lg:grid justify-center md:grid-cols-3 lg:grid-cols-3 items-stretch w-full mx-auto md:hidden max-md:hidden"
		>
			<TarifsCardItem
				v-for="item in topTarrifs"
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
				@add-favorite="addFavorite"
			/>
		</ul>
	</div>
</template>
