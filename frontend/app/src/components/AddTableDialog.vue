<script setup lang="ts">
import { ref } from 'vue';

const providers = ref(['Google', 'Microsoft', 'Apple', 'Yandex']);
const seconds = ref([10, 20, 30, 40, 50, 60]);
</script>

<template>
	<v-card
			title="Добавление таблицы">
			<v-card-text>
				<v-text-field
					clearable
					label="Название таблицы в системе"
					required
				></v-text-field>
				<v-text-field
					clearable
					label="Ссылка"
					required
				></v-text-field>
				<v-select
					clearable
					label="Провайдер"
					:items="providers"
					required
				></v-select>
				<v-select
					clearable
					label="Частота обновления в секундах"
					:items="seconds"
					required
				></v-select>
				<v-btn>Добавить</v-btn>
			</v-card-text>
	</v-card>
</template>

<style scoped>

</style>