<template>
	<button
		v-if="showButton"
		@click="scrollToTop"
		class="scroll-to-top-button border-none rounded-full lg:w-14 lg:h-14 max-md:w-10 md:w-12 max-md:h-10 md:h-12 fixed bottom-6 right-6 text-slate-700 font-light lg:text-4xl md:text-3xl max-md:text-3xl flex justify-center items-center bg-slate-100 shadow-md"
	>
		<span class="mb-1"> ↑ </span>
	</button>
</template>

<script setup>
import { onBeforeUnmount, onMounted, ref } from 'vue'

const showButton = ref(false)

const scrollToTop = () => {
	window.scrollTo({
		top: 0,
		behavior: 'smooth',
	})
}

const checkScroll = () => {
	showButton.value = window.scrollY > 100
}

onMounted(() => {
	window.addEventListener('scroll', checkScroll)
})

onBeforeUnmount(() => {
	window.removeEventListener('scroll', checkScroll)
})
</script>

<style scoped>
.scroll-to-top-button {
	animation: scroll 0.3s ease-in-out;
}

@keyframes scroll {
	0% {
		transform: scale(0);
		opacity: 0;
	}
	100% {
		transform: scale(1);
		opacity: 1;
	}
}
</style>
