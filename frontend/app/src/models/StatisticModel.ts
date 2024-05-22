import type StatisticItem from "../entities/StatisticEntity";

export default class StatisticCreator {
    data: StatisticItem[]
    sended: number
    confirmed: number

    constructor() {
        this.data = []
        this.sended = 0
        this.confirmed = 0
    }

    addStatistic(stat: StatisticItem): void {
        this.data.unshift(stat)
        if(stat.status == "SENDED"){
            this.sended += 1
        }
        else if(stat.status == "CONFIRMED"){
            this.confirmed += 1
        }
    }
}