<script setup lang="ts">
import TablePanel from '@/components/TablePanel.vue';

const tables = [
  [
    {
      page: 1,
      teachersColumn: "C",
      column1: "F",
      column2: "I"
    },
    {
      page: 2,
      teachersColumn: "E",
      column1: "-",
      column2: "-"
    }
  ],
  [
    {
      page: 1,
      teachersColumn: "E",
      column1: "F",
      column2: "G"
    },
  ]
];

</script>

<template>
  <v-container style="width: 80%" >
    <v-row justify="start">
      <v-col cols="12" md="10" sm="6">
        <v-btn class="outlined-button" id="add-table-button" size="35px" prepend-icon="$plus" variant="outlined">
          Добавить
        </v-btn>
        <v-expansion-panels>
          <TablePanel :tables="tables" />
        </v-expansion-panels>
      </v-col>
    </v-row>
  </v-container>
</template>

<style>
.outlined-button {
  margin-bottom: 10px;
  letter-spacing: 0px;
  border: 2px solid currentColor !important;
  font-size: large;
  font-weight: 600;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
#add-table-button {
  width: 150px !important;
  color: limegreen;
}
</style>