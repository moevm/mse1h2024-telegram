<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps({
  tableName: {
    type: String,
    default: () => ""
  }
});
</script>

<template>
	<v-card
		height="240"
		title="Удаление таблицы">
		<v-card-text>
      Вы уверены, что хотите удалить таблицу: {{props.tableName}}?<br/>
      <strong>Данное действие не обратимо, вся информация и настройки таблицы будут удалены.</strong>
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
						id="delete-button"
						size="40px" 
						variant="outlined"
						@click="$emit('close-dialog')">
						Удалить
					</v-btn>
				</v-col>
			</v-row>
		</v-card-text>
	</v-card>
</template>

<style scoped>
strong {
  color: rgb(185,34,34);
}
.v-card-text {
  text-align: left;
  font-weight: 600;
}
.v-card {
  text-align: center;
	font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
#delete-button {
	width: 100px !important;
  color: darkred;
	letter-spacing: 0px !important;
}
#cancel-button {
	width: 100px !important;
	color: gray;
	letter-spacing: 0px !important;
}
</style>