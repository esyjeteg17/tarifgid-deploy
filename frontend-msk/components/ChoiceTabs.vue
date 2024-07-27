<script setup>
import { tabs } from './TABS'

const category = inject('category')

const activeTab = ref(0)

const setActiveTab = index => {
	activeTab.value = index
	category.value = tabs[index].tab
}
</script>

<template>
	<div class="flex justify-between h-16 w-full rounded-md">
		<ChoiceTabsItem
			v-for="tab in tabs"
			:title="tab.title"
			:is-active="activeTab === tabs.indexOf(tab)"
			:key="tab.title"
			:index="tabs.indexOf(tab)"
			@setActiveTab="setActiveTab"
		/>
	</div>
</template>
