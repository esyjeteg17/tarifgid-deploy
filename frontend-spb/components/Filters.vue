<script setup>
defineProps({
	setFilter: Function,
	setOperator: Function,
	setSearch: Function,
	setPrices: Function,
	resetPrices: Function,
})

const gigabytes = inject('gigabytes')

/* const category = inject("category"); */

const operators = inject('operators')

const firstPrices = inject('firstPrices')

const prices = inject('prices')

const favoritesLength = inject('favoritesLength')

const isOnlyFavorite = inject('isOnlyFavorite')

const screenWidth = inject('screenWidth')
</script>

<template>
	<div
		class="filter w-full flex items-left flex-col select-none xl:mt-20 md:mt-16 max-md:mt-24 max-md:-mb-10 max-md:bg-slate-50 max-md:p-5 max-md:rounded-xl"
	>
		<form class="form flex justify-between flex-col">
			<div class="relative w-full border-2 border-slate-300 rounded-lg pl-2">
				<input
					type="text"
					placeholder="Поиск по названию"
					class="search w-11/12 rounded-xl 2xl:h-10 lg:h-8 md:h-7 max-md:h-7 2xl:placeholder:text-base lg:placeholder:text-sm 2xl:text-base md:text-sm max-md:text-sm p-2 ml-4 outline-none max-md:bg-slate-50"
					@change="setSearch"
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

			<label
				for="fav"
				class="custom-favcheckbox md:mt-5 max-md:mt-3 flex items-center w-full border-2 border-slate-100 md:hover:bg-slate-100 transition-all py-2 px-2 rounded-lg"
				:class="{
					'cursor-not-allowed': favoritesLength === 0,
					'cursor-pointer': favoritesLength !== 0,
					'border-slate-200': screenWidth < 768,
				}"
			>
				<input
					:disabled="favoritesLength === 0"
					@change="isOnlyFavorite = !isOnlyFavorite"
					type="checkbox"
					name="fav"
					id="fav"
					class="hidden"
				/>
				<img
					v-if="!isOnlyFavorite"
					class="block lg:w-5 md:w-4 max-md:w-4"
					src="/public/heart-outline.png"
					alt="favorite"
				/>
				<img
					v-else
					class="block lg:w-5 md:w-4 max-md:w-4"
					src="/public/heart.png"
					alt="favorite"
				/>
				<span
					v-if="favoritesLength"
					class="checkmark lg:ml-2 md:ml-1 max-md:ml-1 text-left md:text-sm max-md:text-sm"
					>Только избранные</span
				>
				<span v-else class="checkmark ml-2 text-left md:text-sm max-md:text-sm"
					>Нет избранных</span
				>
				<span
					v-if="favoritesLength"
					class="ml-auto md:text-sm max-md:text-sm rounded-full bg-indigo-500 text-white px-2"
					>{{ favoritesLength }}</span
				>
			</label>

			<h3
				class="mt-5 font-bold 2xl:text-lg md:text-md max-md:text-md text-slate-900"
			>
				Сотовый оператор
			</h3>
			<ul class="filters-mobile relative flex flex-col mt-3">
				<li class="max-md:grid max-md:grid-cols-2">
					<label
						v-for="operator in operators"
						class="li-anim custom-checkbox"
						:for="operator"
						:key="operator"
					>
						<input
							class="operator"
							:name="operator"
							type="checkbox"
							:id="operator"
							:value="operator"
							@change="setOperator"
						/>
						<span class="checkmark">
							<img
								v-if="operator === 'megafon'"
								src="/megafon-logo.png"
								alt="logo"
							/>
							<img v-if="operator === 'mts'" src="/mts-logo.png" alt="logo" />
							<img
								v-if="operator === 'tele2'"
								src="/tele2-logo.png"
								alt="logo"
							/>
							<img v-if="operator === 'yota'" src="/yota-logo.png" alt="logo" />
							<img
								v-if="operator === 'beeline'"
								src="/beeline-logo.png"
								alt="logo"
							/>
							<img v-if="operator === 'sber'" src="/sber-logo.jpg" alt="logo" />
							<img
								v-if="operator === 'tinkoff'"
								src="/tinkoff-logo.png"
								alt="logo"
							/>
						</span>
						<span v-if="operator === 'megafon'">Мегафон </span>
						<span v-if="operator === 'mts'">МТС</span>
						<span v-if="operator === 'beeline'">Билайн</span>
						<span v-if="operator === 'tele2'">Теле2</span>
						<span v-if="operator === 'yota'">Йота</span>
						<span v-if="operator === 'sber'">Сбер Мобайл</span>
						<span v-if="operator === 'tinkoff'">Т-Мобайл</span>
					</label>
				</li>
			</ul>

			<!-- <Slider v-model="prices" range class="w-56 h-52 block" /> -->

			<div class="flex w-full flex-col mt-5">
				<p
					class="block 2xl:text-lg md:text-md max-md:text-md text-slate-900 font-bold"
				>
					Цена
				</p>
				<div class="flex items-center justify-between mt-2 w-full">
					<div
						class="flex items-center relative border-2 border-indigo-500 rounded-md mr-2 w-full"
					>
						<label
							for="pricemin"
							class="absolute z-20 text-slate-400 my-1 mx-2 2xl:text-base lg:text-sm"
							>от</label
						>
						<input
							v-if="prices.min !== '0'"
							@change="setPrices"
							id="pricemin"
							type="number"
							class="price-input text-slate-900 w-full block relative outline-none pl-8 my-1 mx-2 appearence-none 2xl:placeholder:text-base md:placeholder:text-sm max-md:placeholder:text-sm 2xl:pl-8 lg:pl-6 2xl:mx-2 md:mx-1 max-md:mx-1 2xl:text-base md:text-sm max-md:text-sm max-md:bg-slate-50"
							:placeholder="prices.min"
						/>
						<input
							v-else
							@change="setPrices"
							id="pricemin"
							type="number"
							class="price-input w-full block relative outline-none pl-8 my-1 mx-2 appearence-none 2xl:placeholder:text-base md:placeholder:text-sm max-md:placeholder:text-sm 2xl:pl-8 lg:pl-6 2xl:mx-2 md:mx-1 max-md:mx-1 2xl:text-base md:text-sm max-md:text-sm max-md:bg-slate-50"
							placeholder=""
						/>
					</div>

					<div
						class="flex items-center relative border-2 border-indigo-500 rounded-md mr-2 w-full"
					>
						<label
							for="pricemax"
							class="absolute z-20 text-slate-400 my-1 mx-2 box-border 2xl:text-base lg:text-sm"
							>до</label
						>
						<input
							v-if="prices.max !== '99999'"
							@change="setPrices"
							id="pricemax"
							type="number"
							class="price-input w-full block relative outline-none pl-8 my-1 mx-2 appearence-none box-border 2xl:placeholder:text-base md:placeholder:text-sm max-md:placeholder:text-sm 2xl:pl-8 md:pl-7 max-md:pl-7 2xl:mx-2 md:mx-1 max-md:mx-1 2xl:text-base md:text-sm max-md:text-sm max-md:bg-slate-50"
							:placeholder="prices.max"
						/>
						<input
							v-else
							@change="setPrices"
							id="pricemax"
							type="number"
							class="price-input w-full block relative outline-none 2xl:pl-8 md:pl-7 max-md:pl-7 my-1 2xl:mx-2 max-md:mx-1 appearence-none box-border 2xl:placeholder:text-base md:placeholder:text-sm max-md:placeholder:text-sm 2xl:text-base md:text-sm max-md:text-sm max-md:bg-slate-50"
							placeholder=""
						/>
					</div>
				</div>
				<span
					class="cursor-pointer text-slate-500 underline flex w-full justify-end pr-3 2xl:text-sm md:text-sm max-md:text-sm"
					@click="resetPrices"
				>
					Сбросить
				</span>
				<div
					class="max-md:grid max-md:mt-2 max-md:grid-cols-2 md:flex md:flex-col"
				>
					<label class="li-anim custom-radio-button" for="1">
						<input
							@change="setPrices"
							class="priceinp"
							id="1"
							name="bonus"
							type="radio"
							value=""
						/>
						<!-- <span class="text-slate-900"
            >до
            {{ firstPrices.min + Math.round(firstPrices.max / 5 / 100) * 100 }}
            ₽</span
          > -->
						<span class="text-slate-900"
							>до
							{{ 2 * Math.round(firstPrices.max / 6 / 100) * 100 }}
							₽</span
						>

						<span class="checkmark"></span>
					</label>
					<label for="1-2" class="li-anim custom-radio-button">
						<input
							@change="setPrices"
							class="priceinp"
							id="1-2"
							name="bonus"
							type="radio"
							value=""
						/>
						<span class="text-slate-900"
							>{{ 2 * Math.round(firstPrices.max / 6 / 100) * 100 }}
							-
							{{ 3 * Math.round(firstPrices.max / 6 / 100) * 100 }}
							₽</span
						>

						<span class="checkmark"></span>
					</label>
					<label for="2-3" class="li-anim custom-radio-button">
						<input
							@change="setPrices"
							class="priceinp"
							id="2-3"
							name="bonus"
							type="radio"
							value=""
						/>
						<span class="text-slate-900"
							>{{ 3 * Math.round(firstPrices.max / 6 / 100) * 100 }}
							-
							{{ 4 * Math.round(firstPrices.max / 6 / 100) * 100 }}
							₽</span
						>
						<span class="checkmark"></span>
					</label>
					<label for="3-4" class="li-anim custom-radio-button">
						<input
							@change="setPrices"
							class="priceinp"
							id="3-4"
							name="bonus"
							type="radio"
							value=""
						/>
						<span class="text-slate-900"
							>{{ 4 * Math.round(firstPrices.max / 6 / 100) * 100 }}
							-
							{{ 5 * Math.round(firstPrices.max / 6 / 100) * 100 }}
							₽</span
						>
						<span class="checkmark"></span>
					</label>
					<label
						for="more"
						class="li-anim custom-radio-button"
						v-if="
							firstPrices.min <
							Math.round((4 * firstPrices.max) / 5 / 100) * 100
						"
					>
						<input
							@change="setPrices"
							class="priceinp"
							id="more"
							name="bonus"
							type="radio"
							value=""
						/>
						<span class="text-slate-900"
							>более
							{{ 5 * Math.round(firstPrices.max / 6 / 100) * 100 }} ₽</span
						>
						<span class="checkmark"></span>
					</label>
				</div>
			</div>
			<!-- <Slider v-model="gigabytes" range class="mt-10 w-full h-1" />
      <p v-if="gigabytes[1] !== '99999'">
        {{ gigabytes[0] }} - {{ gigabytes[1] }}
      </p> -->
		</form>
	</div>
</template>

<style scoped>
/* .form :deep(.p-slider-range) {
	background: #6366f1;
} */

.price-input::placeholder {
	color: rgb(145, 145, 145);
}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
	-webkit-appearance: none;
	margin: 0;
}

.custom-checkbox input {
	position: absolute;
	opacity: 0;
	cursor: pointer;
}

.custom-checkbox {
	display: flex;
	align-items: center;
	position: relative;
	height: 30px;
	padding-left: 50px;
	margin-bottom: 20px;
	cursor: pointer;
	font-size: 14px;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

.custom-checkbox span {
	font-weight: 500;
	font-size: 16px;
	color: rgb(15 23 42 / 1);
	margin-top: 5px;
}

/* Создание кастомного стилизованного чекбокса */
.custom-checkbox .checkmark {
	position: absolute;
	top: 50%;
	left: 0;
	transform: translateY(-50%);
	height: 35px;
	width: 35px;
	background-color: #ffffff;
	box-shadow: 0 0 6px 0 rgba(0, 0, 0, 0.25);
	border-radius: 6px;
	transition: 0.3s all;
	border: #ffffff 2px solid;
}

.custom-checkbox .checkmark img {
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	height: 80%;
	width: 80%;
}

.custom-checkbox img {
	position: absolute;
	left: 0;
}

/* При наведении меняем цвет фона */
.custom-checkbox:hover .checkmark {
	border: #9b9cd8 2px solid;
}

/* При выборе чекбокса меняем цвет фона и отображаем галочку */
.custom-checkbox input:checked ~ .checkmark {
	border: #6366f1 2px solid;
}

.custom-favcheckbox:has(input:checked) {
	background-color: rgb(241, 245, 249);
}

.filter {
	animation: filter 0.75s ease-in-out forwards;
}

/* Скрываем стандартный радио-инпут */
.custom-radio-button input {
	opacity: 0;
	position: fixed;
	width: 0;
}

/* Создаем кастомный радио-инпут */
.custom-radio-button {
	margin-top: 3px;
	display: inline-block;
	position: relative;
	padding-left: 20px;
	font-size: 16px;
	cursor: pointer;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
	transition: 0.3s all;
}

/* Создаем круг, который будет выступать в роли фона для кнопки */
.custom-radio-button .checkmark {
	position: absolute;
	top: 45%;
	transform: translateY(-50%);
	left: 0;
	height: 14px;
	width: 14px;
	background-color: #ffffff;
	border-radius: 50%;
	border: 1px solid #6366f1;
}

/* Создаем внутренний круг, который отобразится при выборе опции */
.custom-radio-button input:checked ~ .checkmark {
	background-color: #ffffff;
	border: 1px solid #6366f1;
}

/* Создаем внутренний круг в круге, чтобы имитировать выбор опции */
.custom-radio-button .checkmark:after {
	content: '';
	position: absolute;
	display: none;
}

/* Отображаем внутренний круг при выборе */
.custom-radio-button input:checked ~ .checkmark:after {
	display: block;
}

.custom-radio-button input:hover ~ .checkmark:after {
	background: #9b9cd8;
	display: block;
}

/* Стиль внутреннего круга (белый круг в центре) */
.custom-radio-button .checkmark:after {
	top: 50%;
	left: 50%;
	transform: translateX(-50%) translateY(-50%);
	width: 8px;
	height: 8px;
	border-radius: 50%;
	background: #6366f1;
}

.li-anim {
	animation: lianim 0.5s ease-in-out;
}

@keyframes filter {
	0% {
		opacity: 0;
		transform: translateX(-15%);
	}
	100% {
		opacity: 1;
		transform: translateX(0);
	}
}

@keyframes lianim {
	0% {
		opacity: 0;
	}
	100% {
		opacity: 1;
	}
}

@keyframes mobile-filter {
	0% {
		opacity: 0;
		transform: translateY(-5%);
	}
	100% {
		opacity: 1;
		transform: translateY(0);
	}
}

@media not all and (min-width: 768px) {
	.custom-favcheckbox:has(input:checked) {
		background-color: rgb(226 232 240);
	}
	.filter {
		animation: mobile-filter 0.5s ease-in-out forwards;
	}
	.custom-checkbox:hover .checkmark {
		border: #ffffff 2px solid;
	}
	.custom-radio-button {
		font-size: 14px;
	}
	.custom-checkbox {
		display: flex;
		align-items: center;
		position: relative;
		height: 25px;
		padding-left: 45px;
		margin-bottom: 20px;
		cursor: pointer;
		font-size: 14px;
		-webkit-user-select: none;
		-moz-user-select: none;
		-ms-user-select: none;
		user-select: none;
	}

	.custom-checkbox span {
		font-weight: 500;
		font-size: 14px;
		color: rgb(15 23 42 / 1);
		margin-top: 5px;
	}
}
/* md	768px	 */
@media (min-width: 768px) {
	.custom-radio-button {
		font-size: 14px;
	}
	.custom-checkbox {
		display: flex;
		align-items: center;
		position: relative;
		height: 20px;
		padding-left: 45px;
		margin-bottom: 20px;
		cursor: pointer;
		font-size: 14px;
		-webkit-user-select: none;
		-moz-user-select: none;
		-ms-user-select: none;
		user-select: none;
	}

	.custom-checkbox span {
		font-weight: 500;
		font-size: 14px;
		color: rgb(15 23 42 / 1);
		margin-top: 5px;
	}

	/* Создание кастомного стилизованного чекбокса */
	.custom-checkbox .checkmark {
		height: 35px;
		width: 35px;
	}
}
/* lg	1024px */
@media (min-width: 1024px) {
}

/* xl	1280px */
@media (min-width: 1280px) {
}

/* 2xl	1536px */
@media (min-width: 1536px) {
	.custom-radio-button {
		font-size: 16px;
	}
	.custom-checkbox {
		display: flex;
		align-items: center;
		position: relative;
		height: 30px;
		padding-left: 50px;
		margin-bottom: 20px;
		cursor: pointer;
		font-size: 14px;
		-webkit-user-select: none;
		-moz-user-select: none;
		-ms-user-select: none;
		user-select: none;
	}

	.custom-checkbox span {
		font-weight: 500;
		font-size: 16px;
		color: rgb(15 23 42 / 1);
		margin-top: 5px;
	}

	/* Создание кастомного стилизованного чекбокса */
	.custom-checkbox .checkmark {
		position: absolute;
		top: 50%;
		left: 0;
		transform: translateY(-50%);
		height: 40px;
		width: 40px;
		background-color: #ffffff;
		box-shadow: 0 0 6px 0 rgba(0, 0, 0, 0.25);
		border-radius: 6px;
		transition: 0.3s all;
		border: #ffffff 2px solid;
	}

	.custom-checkbox .checkmark img {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
		height: 80%;
		width: 80%;
	}

	.custom-checkbox img {
		position: absolute;
		left: 0;
	}

	/* При наведении меняем цвет фона */
	.custom-checkbox:hover .checkmark {
		border: #9b9cd8 2px solid;
	}

	/* При выборе чекбокса меняем цвет фона и отображаем галочку */
	.custom-checkbox input:checked ~ .checkmark {
		border: #6366f1 2px solid;
	}
}
</style>
