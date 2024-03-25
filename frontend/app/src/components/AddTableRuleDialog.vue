<script setup lang="ts">
import { defineProps } from 'vue';
import type TableItem from '@/entities/TableEntity';

const props = defineProps({
  table: {
    type: Object as () => TableItem,
    default: () => {}
  }
});

</script>

<template>
	<v-card
		height="430"
		title="Добавление правила">
		<v-card-text>
			<v-text-field
				clearable
				label="Название страницы"
				required></v-text-field>
			<v-text-field
				clearable
				label="Столбец преподавателей"
				required></v-text-field>
			<v-text-field
				clearable
				label="Столбец 1"
				required></v-text-field>
			<v-text-field
				clearable
				label="Столбец 2"
				required></v-text-field>
			<v-row justify="end">
				<v-col cols="auto">
					<v-btn 
						class="outlined-button"
						id="cancel-button"
						size="40px"
						variant="outlined"
						@click="$emit('close-dialog')">
						Отмена
					</v-btn>
				</v-col>
				<v-col cols="auto">
					<v-btn 
						class="outlined-button"
						id="confirm-button"
						size="40px" 
						variant="outlined"
						@click="$emit('close-dialog')">
						Подтвердить
					</v-btn>
				</v-col>
			</v-row>
		</v-card-text>
	</v-card>
</template>

<style scoped>
.v-card {
	text-align: center;
	font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
#confirm-button {
	width: 150px !important;
  color: limegreen;
	letter-spacing: 0px !important;
}
#cancel-button {
	width: 100px !important;
	color: darkred;
	letter-spacing: 0px !important;
}
</style>