import config
import re
import pandas as pd


def parser(filepath: str) -> str:
    with open(filepath, 'r') as file:
        filestr = str(file.read())
        # parse out quotations
        regex = re.compile('"(.*?)"')
        filestr = regex.sub(' ', filestr)
        # parse out all non-alpha
        regex = re.compile('[^a-zA-Z]')
        filestr = regex.sub(' ', filestr)

        return filestr.lower()


def count_words(text: str) -> dict:
    words = text.split()
    words_unique = list(set(words))
    counts = [words.count(i) for i in words_unique]
    return {'word': words_unique, 'count': counts}


def main() -> None:
    parsed_text = parser(config.input_file)
    stats_dict = count_words(parsed_text)
    stats_df = pd.DataFrame(stats_dict).sort_values(by='count', ascending=False)

    stats_df.to_csv(config.output_file, index=False)


if __name__ == "__main__":
    main()
