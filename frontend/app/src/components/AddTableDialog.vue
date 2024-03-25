<script setup lang="ts">
import { ref, defineProps, defineEmits } from 'vue';
import TableCreator from '@/models/TableModel';

const props = defineProps({
	tables: {
		type: TableCreator,
		default: () => new TableCreator()
	}
});

const emit = defineEmits(['close-dialog']);

//-Тестовые данные ----------------------------------------------
const providers = ref(['Google', 'Microsoft', 'Apple', 'Yandex']);
const seconds = ref([10, 20, 30, 40, 50, 60]);
//---------------------------------------------------------------
</script>

<template>
	<v-card
		height="430"
		title="Добавление таблицы">
		<v-card-text>
			<v-text-field
				clearable
				label="Название таблицы в системе"
				required></v-text-field>
			<v-text-field
				clearable
				label="Ссылка"
				required></v-text-field>
			<v-select
				clearable
				label="Провайдер"
				:items="providers"
				required></v-select>
			<v-select
				clearable
				label="Частота обновления в секундах"
				:items="seconds"
				required></v-select>
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