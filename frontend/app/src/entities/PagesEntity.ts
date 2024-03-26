export default interface Pages {
	id: string;
	name: string;
	teacher_column: string;
	columns: string[];
	rule?: string;
	notification_text?: string;
}