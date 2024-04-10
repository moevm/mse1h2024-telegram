class TextConverter:
    @staticmethod
    def convert_markdown(json_text) -> str:
        content = json_text["content"] if json_text["content"] else ""
        params = json_text["params"]
        type = params.get('type')

        if type == "confirm":
            format_values = [params["table_name"], params["table_url"]]
            content = str(content).format(*format_values)

        return content
