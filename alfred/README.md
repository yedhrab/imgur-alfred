# AlfredClient

Simplest Alfred Client that I use my own projects.

## ⭐️ Example Project

![alt](https://i.imgur.com/tUJjVUJ.png)

```python
from re import sub
from urllib.parse import quote_plus

from alfred.client import AlfredClient


def main():
    query = AlfredClient.get_query()

    char_count = str(len(query))
    word_count = str(len(query.split(" ")))
    line_count = str(len(query.split("\n")))

    encoded_string = quote_plus(query)
    remove_dublication = " ".join(dict.fromkeys(query.split(" ")))

    upper_case = query.upper()
    lower_case = query.lower()
    capitalized = query.capitalize()
    template = sub(r"[a-zA-Z0-9]", "X", query)

    results = [
        AlfredClient.to_result(encoded_string, "Encoded", arg=encoded_string),
        AlfredClient.to_result(remove_dublication, "Remove dublication", arg=remove_dublication),
        AlfredClient.to_result(upper_case, "Upper Case", arg=upper_case),
        AlfredClient.to_result(lower_case, "Lower Case", arg=lower_case),
        AlfredClient.to_result(capitalized, "Capitalized", arg=capitalized),
        AlfredClient.to_result(template, "Template", arg=template),
        AlfredClient.to_result(char_count, "Characters", arg=char_count),
        AlfredClient.to_result(word_count, "Words", arg=word_count),
        AlfredClient.to_result(line_count, "Lines", arg=line_count),
    ]

    AlfredClient.response(results)


if __name__ == "__main__":
    main()

```

## 🪪 License

```
Copyright 2022 Yunus Emre Ak ~ YEmreAk.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
