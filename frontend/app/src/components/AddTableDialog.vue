<script setup lang="ts">
import { ref, defineEmits } from 'vue';
import { useTablesStore } from '@/stores/tablesStore';
import type TableItem from '@/entities/TableEntity';

const tablesStore = useTablesStore();

const emit = defineEmits(['close-dialog']);

//- Данные ------------------------------------------------------
const tableName = ref('');
const tableLink = ref('');
const tableProvider = ref('');
const tableUpdateSeconds = ref();
const providers = ref(['Google', 'Yandex']);
const seconds = ref([10, 20, 30, 40, 50, 60]);
//---------------------------------------------------------------

const confirm = () => {
	const table: TableItem = {
		name: tableName.value,
		link: tableLink.value,
		provider: tableProvider.value.toUpperCase(),
		update_frequency: tableUpdateSeconds.value,
		pages: []
	}
	tablesStore.setTable(table);
	emit('close-dialog');
};
</script>

<template>
	<v-card
		height="430"
		title="Добавление таблицы">
		<v-card-text>
			<v-text-field
				v-model="tableName"
				clearable
				label="Название таблицы в системе"
				required></v-text-field>
			<v-text-field
				v-model="tableLink"
				clearable
				label="Ссылка"
				required></v-text-field>
			<v-select
				v-model="tableProvider"
				clearable
				label="Провайдер"
				:items="providers"
				required></v-select>
			<v-select
				v-model="tableUpdateSeconds"
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
						@click="confirm">
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