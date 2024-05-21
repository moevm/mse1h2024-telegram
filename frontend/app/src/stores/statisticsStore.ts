import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from '@/config/defaultAxios'
import { type Ref } from "vue";
import StatisticCreator from "@/models/StatisticModel";
import type StatisticItem from "@/entities/StatisticEntity";

export const useStatisticsStore = defineStore('statistics', () => {
    const statistics: Ref<StatisticCreator> = ref(new StatisticCreator())

    const getStatistics = async (): Promise<void> => {
        axios.get('/statistics').then((response) => {
            response.data.forEach((data) => {
                const statistic: StatisticItem = {
                    status: data.status,
                    table_link: data.table_link,
                    teacher: data.teacher,
                    _id: data.id
                }
                statistics.value.addStatistic(statistic)
            })
        })
    }

    return {
        statistics,
        getStatistics
    }
})
