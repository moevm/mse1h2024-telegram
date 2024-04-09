<script setup lang="ts">
import { ref, defineProps, defineEmits } from 'vue';
import type Pages from '@/entities/PagesEntity';
import { useTablesStore } from '@/stores/tablesStore';

const tablesStore = useTablesStore();

const emit = defineEmits(['close-dialog']);

const props = defineProps({
	tableId: {
		type: String,
		default: ''
	},
  page: {
    type: Object as () => Pages,
    default: () => {}
  }
});

//- Данные ----------------------------------------
const pageName = ref(props.page.name);
const teacherColumn = ref(props.page.teacher_column);
const column1 = ref(props.page.columns[0]);
const column2 = ref(props.page.columns[1]);
//-------------------------------------------------

const confirm = () => {
	const changedRule: Pages = {
    id: props.page.id,
		name: pageName.value,
		teacher_column: teacherColumn.value,
		columns: [column1.value, column2.value],
		rule: '',
		notification_text: ''
	}
	tablesStore.editTableRule(changedRule, props.tableId);
	emit('close-dialog');
};
</script>

<template>
	<v-card
		height="430"
		title="Изменить правило">
		<v-card-text>
			<v-text-field
        v-model="pageName"
				clearable
				label="Название страницы"
				required></v-text-field>
			<v-text-field
				v-model="teacherColumn"
				clearable
				label="Столбец преподавателей"
				required></v-text-field>
			<v-text-field
				v-model="column1"
				clearable
				label="Столбец 1"
				required></v-text-field>
			<v-text-field
				v-model="column2"
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