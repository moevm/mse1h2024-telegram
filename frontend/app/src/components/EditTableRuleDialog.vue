<script setup lang="ts">
import { defineProps } from 'vue';
import type Pages from '@/entities/PagesEntity';

const props = defineProps({
  page: {
    type: Object as () => Pages,
    default: () => {}
  }
});

</script>

<template>
	<v-card
		height="430"
		title="Изменить правило">
		<v-card-text>
			<v-text-field
        v-model="props.page.name"
				clearable
				label="Название страницы"
				required></v-text-field>
			<v-text-field
				v-model="props.page.teacher_column"
				clearable
				label="Столбец преподавателей"
				required></v-text-field>
			<v-text-field
				v-model="props.page.columns[0]"
				clearable
				label="Столбец 1"
				required></v-text-field>
			<v-text-field
				v-model="props.page.columns[1]"
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