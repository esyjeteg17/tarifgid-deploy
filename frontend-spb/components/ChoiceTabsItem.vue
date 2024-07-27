<script setup>
import { defineProps, ref, defineEmits } from "vue";

defineProps({
  title: String,
  isActive: Boolean,
  index: Number,
});

const emit = defineEmits(["setActiveTab"]);
</script>

<template>
  <div
    :class="
      isActive
        ? 'bg-gradient-to-l from-indigo-500 to-violet-500 text-white relative p-5 justify-center shadow-md mx-2 font-medium rounded-lg flex items-center h-full w-1/5 cursor-pointer transition-all select-none text-sm text-center hover:shadow-xl'
        : 'bg-[#ffffff] text-slate-900 relative p-5 justify-center shadow-md mx-2 font-medium rounded-lg flex items-center h-full w-1/5 cursor-pointer transition-all select-none text-sm text-center hover:shadow-xl'
    "
    @click="$emit('setActiveTab', index)"
  >
    <!-- <img
      v-if="title === 'Мобильная связь'"
      class="absolute top-1/2 -translate-y-1/2 left-1 h-3/4"
      src="/for-phone.png"
      alt="phones"
    /> -->
    {{ title }}
  </div>
</template>
