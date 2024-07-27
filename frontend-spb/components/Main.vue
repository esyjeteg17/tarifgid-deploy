<script setup lang="ts"></script>

<template>
	<div class="w-11/12 2xl:mt-36 xl:mt-24 mx-auto flex relative">
		<div class="md:w-1/2 max-md:w-full my-20">
			<!-- <h3
        class="economy text-2xl font-bold bg-clip-text bg-gradient-to-r from-indigo-500 to-violet-500"
      >
        Начните экономить прямо сейчас!
      </h3> -->
			<h1
				class="2xl:text-6xl font-bold text-slate-900 md:mt-5 relative xl:text-5xl md:text-4xl max-md:text-4xl md:leading-8 2xl:leading-12 max-md:leading-8 max-md:text-center"
			>
				Поиск тарифа
				<span
					class="economy block mt-3 bg-clip-text bg-gradient-to-r from-indigo-500 to-violet-500"
					>никогда не был</span
				>
				<span class="bef relative block mt-3 z-10">таким простым</span>
			</h1>
			<p
				class="mt-8 text-[#7B7B7B] font-medium 2xl:text-base md:text-sm max-md:text-sm max-md:text-center"
			>
				Вас приветствует портал, где простота встречается с эффективностью.
				Отправьтесь в путешествие по миру тарифов, где Вы найдёте идеальное
				сочетание цены и качества, соответствующее именно Вашим нуждам.
			</p>
			<div class="md:mt-10 max-md:mt-5 max-md:mx-auto">
				<nuxt-link to="/sravni" class="max-md:flex max-md:justify-center"
					><button
						class="go max-md:mx-auto bg-gradient-to-l from-indigo-500 to-violet-500 text-white 2xl:px-10 2xl:py-3 md:px-5 max-md:px-7 md:py-2 max-md:py-2 rounded-3xl boreder-slate-300 box-border font-bold transition-all hover:bg-indigo-600 2xl:text-base md:text-sm"
					>
						Вперед
					</button></nuxt-link
				>
				<!-- <span
          class="it-work text-indigo-700 ml-5 font-bold underline cursor-pointer transition-all hover:text-indigo-900 relative"
          >Как это работает?
        </span> -->
				<!-- <div
					class="description absolute min-h-0 p-8 w-full bg-white rounded-3xl border-2 top-72 left-1/2 -translate-x-1/2 border-slate-300 z-50 hidden"
				>
					Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro, labore
					est? Rerum, consequatur quas? Aut odio ex libero atque voluptas nisi
					iusto esse temporibus, eius labore dolorum modi corrupti cupiditate!
					Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo tempora
					explicabo, illum consequuntur consequatur corporis quam aut voluptas
					error inventore ipsam corrupti, officia unde rerum labore ratione eum
					quisquam id. Lorem ipsum dolor sit amet consectetur adipisicing elit.
					Ut fugiat quam saepe, eum, repudiandae, blanditiis odio voluptatem in
					repellat aperiam aliquid? Vel impedit eveniet, dolorum iste labore
					mollitia at nisi.
				</div> -->
			</div>
		</div>
		<div
			class="picture w-5/12 absolute md:left-1/2 max-md:-transform-left-1/2 ml-32 xl:top-0 md:top-20 max-md:hidden"
		>
			<img class="w-full" src="/Group 75.png" alt="img" />
		</div>
	</div>
</template>

<style scoped>
.economy {
	color: transparent;
}
.picture {
	animation: picture 4s ease-in-out forwards;
}

.star {
	animation: star 2s ease-in-out forwards;
	left: 600px;
}

.bef {
	position: relative;
	display: inline-block;
}

.bef:hover::before {
	height: 85%;
}

.bef::before {
	content: '';
	position: absolute;
	bottom: 0;
	left: 0;
	width: 100%;
	height: 40%;
	background-color: #48ffb0;
	z-index: -1;
	border-radius: 1rem;
	transition: all 0.2s ease-in-out;
	animation: line 1s ease-in-out forwards;
}

/* h1::after {
	content: '';
	display: block;
	position: absolute;
	top: -20px;
	left: 600px;
	width: 80px;
	height: 80px;
	background: url('/Star 1.svg') center center/contain no-repeat;
	animation: star 1s ease-in-out forwards;
} */

@media (max-width: 1024px) {
}

.go {
	animation: go 0.8s ease-in-out infinite alternate;
}

.it-work:hover ~ .description {
	display: block;
}

@keyframes pict {
	0% {
		opacity: 0;
	}
	50% {
		opacity: 0;
	}
	100% {
		opacity: 1;
	}
}

@keyframes go {
	0% {
		transform: scale(1);
	}
	100% {
		transform: scale(1.1);
	}
}

@keyframes line {
	0% {
		width: 0;
	}
	100% {
		width: 100%;
	}
}
@keyframes star {
	0% {
		transform: translateX(100px) rotate(180deg);
		opacity: 0;
	}
	50% {
		transform: translateX(100px) rotate(180deg);
		opacity: 0;
	}
	100% {
		transform: translateX(0) rotate(0);
		opacity: 1;
	}
}
</style>
