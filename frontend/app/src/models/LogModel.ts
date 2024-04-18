import type LogItem from '../entities/LogEntity';

export default class LogCreator {
    data: LogItem[];

    constructor() {
        this.data = [];
    }

    addLog(log: LogItem) {
        this.data.push(log);
    }
}