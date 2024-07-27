<template>
	<ul role="list" class="divide-y divide-gray-100 mt-20">
		<li
			v-for="item in items"
			:key="item.id"
			class="flex justify-between gap-x-6 py-5"
		>
			<div class="flex min-w-0 gap-x-4">
				<img
					class="h-12 w-12 flex-none rounded-full bg-gray-50"
					src="/megafon-logo.png"
					alt=""
				/>
				<div class="min-w-0 flex-auto">
					<p class="text-sm font-semibold leading-6 text-gray-900">
						{{ item.name }}
					</p>
					<p class="mt-1 truncate text-xs leading-5 text-gray-500">
						{{ item.operator }}
					</p>
				</div>
			</div>
			<div class="hidden shrink-0 md:flex md:flex-col md:items-end">
				<p class="text-sm leading-6 text-gray-900">{{ item.price }}</p>
				<p v-if="item.lastSeen" class="mt-1 text-xs leading-5 text-gray-500">
					<time :datetime="item.lastSeenDateTime">{{ item.price }}</time>
				</p>
				<div v-else class="mt-1 flex items-center gap-x-1.5">
					<div class="flex-none rounded-full bg-emerald-500/20 p-1">
						<div class="h-1.5 w-1.5 rounded-full bg-emerald-500" />
					</div>
					<!-- <p class="text-xs leading-5 text-gray-500">Online</p> -->
				</div>
			</div>
		</li>
	</ul>
</template>

<script setup>
import axios from 'axios'

const items = ref([])

const getFavoritesItems = async () => {
	try {
		const { data } = await axios.get('http://127.0.0.1:8000/api/v1/mobile')
		items.value = data.filter(item => item.isFavotite)
		console.log(items.value)
	} catch (e) {
		console.log(e)
	}
}

onMounted(async () => {
	await getFavoritesItems()
})
</script>
