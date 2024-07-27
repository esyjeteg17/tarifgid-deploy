<script setup>
import axios from 'axios'
import BonusSVG from './BonusSVG.vue'
import { useAuthStore } from '~/store/index'

/* const noAuthOverlayIsOpen = inject('noAuthOverlayIsOpen') */

const authStore = useAuthStore()
const user = computed(() => authStore.user)

const props = defineProps({
	id: Number,
	name: String,
	price: Number,
	minutes: Number,
	gb: Number,
	/* isLoading: Boolean, */
	img: String,
	bonus: String,
	sms: Number,
	link: String,
	descr: String,
	speed: String,
	tv: Number,
	operator: String,
	isFavorite: Boolean,
})

const isLoading = inject('isLoading')

const isFlipped = ref(false)

const flipCard = () => {
	isFlipped.value = !isFlipped.value
}

const addFavorite = defineEmits(['add-favorite'])
</script>

<template>
	<li
		v-if="!isFlipped"
		class="card-li relative flex flex-col bg-white rounded-2xl shadow-lg md:m-3 max-md:m-1 2xl:px-7 md:px-5 2xl:pt-5 md:pt-4 max-md:pt-4 max-md:px-4 box-border lg:hover:translate-y-[-10px] lg:hover:shadow-3xl transition-all card-item pb-20 border-2 border-slate-100"
	>
		<button
			title="Добавить в избранное"
			@click="addFavorite('add-favorite', id)"
			v-if="!isLoading"
			class="absolute top-5 right-5 w-5 h-5"
		>
			<img
				:src="isFavorite ? '/heart.png' : '/heart-outline.png'"
				alt="heart"
			/>
		</button>
		<h3
			v-if="!isLoading"
			class="head bg-clip-text bg-gradient-to-l from-indigo-500 to-violet-500 2xl:text-2xl md:text-xl font-bold max-md:text-xl"
		>
			{{ operator }}
		</h3>
		<h3 v-else class="skeleton block w-1/2 h-10 bg-[#ededed] rounded-2xl"></h3>
		<p v-if="!isLoading" class="text-sm font-semibold mt-3 text-slate-900">
			<span
				class="2xl:text-4xl text-slate-900 inline-block font-bold -mr-1 md:text-3xl max-md:text-2xl max-md:-mt-3 2xl:mt-0 md:-mt-3"
				>{{ price }} ₽</span
			>/месяц
		</p>
		<div
			v-else
			class="skeleton block w-full h-14 mt-3 bg-[#ededed] rounded-2xl"
		></div>
		<h4
			v-if="!isLoading"
			class="text-sm font-bold text-slate-600 2xl:mt-3 md:mt-1"
		>
			Тариф "{{ name }}"
		</h4>
		<div
			v-else
			class="skeleton block w-1/2 h-6 mt-3 bg-[#ededed] rounded-2xl"
		></div>
		<ul v-if="!isLoading" class="flex flex-col mt-3 w-full relative">
			<div v-if="speed">
				<li class="feature mb-2 font-semibold text-sm text-slate-900">
					{{ speed }}
				</li>
			</div>
			<div v-if="gb">
				<li
					v-if="gb !== 99999"
					class="feature mb-2 font-semibold text-sm text-slate-900"
				>
					{{ gb }} ГБ
				</li>
				<li
					v-else
					class="feature mb-2 font-semibold text-base text-slate-900 flex"
				>
					<img class="h-6 mr-2" src="/infinity.png" alt="infinity" />
					<span>ГБ</span>
				</li>
			</div>
			<div v-if="minutes">
				<li
					v-if="minutes !== 99999"
					class="feature mb-2 font-semibold text-sm text-slate-900"
				>
					{{ minutes }} минут
				</li>
				<li
					v-else
					class="feature mb-2 font-semibold text-sm text-slate-900 flex"
				>
					<img src="/infinity.png" class="h-6 mr-2" alt="infinity" />
					<span>минут</span>
				</li>
			</div>
			<div v-if="tv">
				<li class="feature mb-2 font-semibold text-sm text-slate-900">
					{{ tv }} ТВ
				</li>
			</div>
			<div v-if="sms">
				<li
					v-if="sms !== 99999"
					class="feature mb-2 font-semibold text-sm text-slate-900"
				>
					{{ sms }} СМС
				</li>
				<li
					v-else
					class="feature mb-2 font-semibold text-sm text-slate-900 flex"
				>
					<img src="/infinity.png" class="h-6 mr-2" alt="infinity" />
					<span>СМС</span>
				</li>
			</div>

			<div
				@click="flipCard"
				v-if="bonus"
				class="flex items-center w-full trigger cursor-pointer"
			>
				<div
					class="trigger feature 2xl:mb-2 md:mb-0 max-md:mb-0 feature-bonus font-semibold text-sm text-slate-900 underline underline-offset-2 decoration-dashed"
				>
					{{ bonus }}
				</div>
				<div class="h-4 w-4 ml-1 2xl:mb-2 md:mb-0 max-md:mb-0">
					<BonusSVG />
				</div>
			</div>
		</ul>

		<div
			v-else
			class="skeleton block w-full mt-3 bg-[#ededed] rounded-2xl h-24"
		></div>

		<button
			v-if="!isLoading"
			class="block absolute bottom-5 w-10/12 inset-x-2/4 -translate-x-1/2 bg-gradient-to-r from-indigo-500 to-violet-500 rounded-xl text-white 2xl:h-12 max-md:h-10 md:h-10 font-bold text-base transition-all ease-in-out"
		>
			<a
				class="absolute w-full top-0 left-0 h-full flex justify-center items-center"
				:href="link"
				target="_blank"
				>К тарифу</a
			>
		</button>

		<button
			v-else
			class="block absolute bottom-5 w-10/12 inset-x-2/4 -translate-x-1/2 bg-gradient-to-r from-indigo-500 to-violet-500 mt-3 rounded-xl text-white h-12 font-bold text-base transition-all ease-in-out disabled:from-slate-300 disabled:to-slate-300 disabled:cursor-not-allowed"
			disabled
		>
			<a class="w-full" :href="link">К тарифу</a>
		</button>
	</li>
	<li
		v-else
		class="card-li relative flex flex-col bg-white rounded-2xl shadow-lg md:m-3 max-md:m-1 2xl:px-7 md:px-5 2xl:pt-5 md:pt-4 max-md:pt-4 max-md:px-4 box-border lg:hover:translate-y-[-10px] lg:hover:shadow-3xl transition-all card-item pb-5 border-2 border-slate-100"
	>
		<div class="">
			<ul class="descr text-sm" v-html="descr"></ul>

			<div
				@click="flipCard"
				class="2xl:mb-2 md:mb-0 max-md:mb-0 font-semibold text-sm text-slate-900 underline underline-offset-2 decoration-dashed cursor-pointer mt-2"
			>
				К карточке
			</div>
		</div>
	</li>
</template>

<style scoped>
.feature {
	position: relative;
	padding-left: 20px;
}
.feature::before {
	content: '';
	background: url('/vector.svg') center center/contain no-repeat;
	display: block;
	position: absolute;
	left: 0;
	top: 50%;
	transform: translateY(-50%);
	width: 15px;
	height: 15px;
	margin-right: 5px;
}
.feature-bonus::before {
	content: '';
	background: url('/bonus.svg') center center/contain no-repeat;
	display: block;
	position: absolute;
	left: 0;
	top: 50%;
	transform: translateY(-50%);
	width: 15px;
	height: 15px;
	margin-right: 5px;
}
.head {
	color: transparent;
}

.skeleton {
	position: relative;
}
.skeleton::before {
	content: '';
	width: 100%;
	height: 100%;
	border-radius: 15px;
	position: absolute;
	left: 0;
	top: 0;
	background: linear-gradient(90deg, #ededed 0%, #f7f7f7 50%, #ededed 100%);
	background-size: 200% 100%;
	animation: loading 2s ease-in-out infinite;
}

.info-block {
	position: absolute;
	display: none;
	left: 50%;
	transform: translateX(-50%);
	bottom: 35px;
	width: 300px;
	min-height: 0px;
	background-color: #ffffff;
	padding: 10px;
	border: 1px solid #ccc;
	border-radius: 10px;
	animation: info 0.3s ease-in-out;
}

.trigger:hover + .info-block {
	display: block;
	z-index: 100;
}

.trigger:hover ~ .info-block {
	display: block;
	z-index: 100;
}

.info-block p {
	font-size: 16px;
	line-height: 1.5;
	margin-bottom: 15px;
}

.info-block a {
	color: #007bff;
	text-decoration: underline;
}

.info-block a:hover {
	color: #0056b3;
	text-decoration: none;
}

.card-li {
	animation: card-li 0.5s ease-in-out forwards;
}

.descr {
	list-style: disc;
	list-style-position: inside;
}

@keyframes card-li {
	0% {
		opacity: 0;
	}
	100% {
		opacity: 1;
	}
}

@keyframes loading {
	0% {
		background-position: 0 0;
	}
	50% {
		background-position: 100% 0;
	}
	100% {
		background-position: 0 0;
	}
}

@keyframes info {
	0% {
		opacity: 0;
	}
	100% {
		opacity: 1;
	}
}

/* sm	640px	 */
@media (min-width: 640px) {
}
/* md	768px */
@media (min-width: 768px) {
	.info-block span {
		display: block;
		font-size: 12px;
		line-height: 1.5;
	}
	.info-block {
		width: 300px;
	}
}
/* lg	1024px */
@media (min-width: 1024px) {
	.info-block span {
		font-size: 14px;
		line-height: 1;
	}
	.info-block {
		width: 240px;
	}
}
/* xl	1280px */
@media (min-width: 1280px) {
	.info-block span {
		font-size: 14px;
		line-height: 1.5;
	}
	.info-block {
		width: 275px;
	}
}
/* 2xl	1536px */
@media (min-width: 1536px) {
	.info-block span {
		font-size: 14px;
		line-height: 1.5;
	}
	.info-block {
		position: absolute;
		display: none;
		left: 50%;
		transform: translateX(-50%);
		bottom: 35px;
		width: 300px;
		min-height: 0px;
		background-color: #ffffff;
		padding: 10px;
		border: 1px solid #ccc;
		border-radius: 10px;
		animation: info 0.3s ease-in-out;
		z-index: 1000;
	}
}
</style>
