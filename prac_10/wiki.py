"""
CP1404/CP5632 Practical
Wikipedia page search program using the wikipedia package
"""

import wikipedia
from wikipedia import DisambiguationError, PageError


def main():
    """Prompt user for page titles and display page summary and URL, with error handling."""
    print("Enter Wikipedia page titles (blank to exit)")
    while True:
        title = input("Enter page title: ").strip()
        if not title:
            break
        try:
            page = wikipedia.page(title)  # autosuggest removed
            print(page.title)
            print(wikipedia.summary(title, sentences=2))
            print(page.url)
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

    print("Thank you.")


if __name__ == '__main__':
    main()
