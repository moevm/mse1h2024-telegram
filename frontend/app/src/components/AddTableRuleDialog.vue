<script setup lang="ts">
import { ref, defineProps, defineEmits } from 'vue';
import type TableItem from '@/entities/TableEntity';
import type Pages from '@/entities/PagesEntity';
import { v4 as uuidv4 } from 'uuid';
import { useTablesStore } from '@/stores/tablesStore';

const tablesStore = useTablesStore();

const emit = defineEmits(['close-dialog']);

const props = defineProps({
  table: {
    type: Object as () => TableItem,
    default: () => {}
  }
});

//- Данные ----------------------
const pageName = ref('');
const teacherColumn = ref('');
const column1 = ref('');
const column2 = ref('');
//-------------------------------

const confirm = () => {
	const rule: Pages = {
    id: uuidv4(),
		name: pageName.value,
		teacher_column: teacherColumn.value,
		columns: [column1.value, column2.value],
		rule: '',
		notification_text: ''
	}
	tablesStore.setTableRule(props.table, rule);
	emit('close-dialog');
};
</script>

<template>
	<v-card
		height="430"
		title="Добавление правила">
		<v-card-text>
			<v-text-field
				v-model:="pageName"
				clearable
				label="Название страницы"
				required></v-text-field>
			<v-text-field
				v-model:="teacherColumn"
				clearable
				label="Столбец преподавателей"
				required></v-text-field>
			<v-text-field
				v-model:="column1"
				clearable
				label="Столбец 1"
				required></v-text-field>
			<v-text-field
				v-model:="column2"
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