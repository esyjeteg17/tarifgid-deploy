<template>
	<TransitionRoot as="template" :show="open">
		<Dialog class="relative z-10" @close="open = false">
			<TransitionChild
				as="template"
				enter="ease-out duration-300"
				enter-from="opacity-0"
				enter-to="opacity-100"
				leave="ease-in duration-200"
				leave-from="opacity-100"
				leave-to="opacity-0"
			>
				<div
					class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
				/>
			</TransitionChild>

			<div class="fixed inset-0 z-10 w-screen overflow-y-auto">
				<div
					class="flex min-h-full items-end justify-center p-4 text-center md:items-center md:p-0"
				>
					<TransitionChild
						as="template"
						enter="ease-out duration-300"
						enter-from="opacity-0 translate-y-4 md:translate-y-0 md:scale-95"
						enter-to="opacity-100 translate-y-0 md:scale-100"
						leave="ease-in duration-200"
						leave-from="opacity-100 translate-y-0 md:scale-100"
						leave-to="opacity-0 translate-y-4 md:translate-y-0 md:scale-95"
					>
						<DialogPanel
							class="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all md:my-8 md:w-full md:max-w-lg"
						>
							<div class="bg-white px-4 pb-4 pt-5 md:p-6 md:pb-4">
								<div class="md:flex md:items-start">
									<div
										class="mx-auto flex h-12 w-12 flex-shrink-0 items-center justify-center rounded-full bg-red-100 md:mx-0 md:h-10 md:w-10"
									>
										<ExclamationTriangleIcon
											class="h-6 w-6 text-red-600"
											aria-hidden="true"
										/>
									</div>
									<div class="mt-3 text-center md:ml-4 md:mt-0 md:text-left">
										<DialogTitle
											as="h3"
											class="text-base font-semibold leading-6 text-gray-900"
											>Deactivate account</DialogTitle
										>
										<div class="mt-2">
											<p class="text-sm text-gray-500">
												Are you sure you want to deactivate your account? All of
												your data will be permanently removed. This action
												cannot be undone.
											</p>
										</div>
									</div>
								</div>
							</div>
							<div
								class="bg-gray-50 px-4 py-3 md:flex md:flex-row-reverse md:px-6"
							>
								<button
									type="button"
									class="inline-flex w-full justify-center rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 md:ml-3 md:w-auto"
									@click="open = false"
								>
									Deactivate
								</button>
								<button
									type="button"
									class="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 md:mt-0 md:w-auto"
									@click="open = false"
									ref="cancelButtonRef"
								>
									Cancel
								</button>
							</div>
						</DialogPanel>
					</TransitionChild>
				</div>
			</div>
		</Dialog>
	</TransitionRoot>
</template>

<script setup>
import { ref } from 'vue'

const open = ref(true)
</script>
