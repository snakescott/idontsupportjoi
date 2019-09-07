from bs4 import BeautifulSoup


def extract_names(html):
    """Exctract the names of signatories from raw wesupportjoi.org html"""
    soup = BeautifulSoup(html, "html.parser")

    # divs sadly do not have ids, but the site is laid out such that the third
    # <div> with this class contains a list of <p>s of signatories
    names_div = soup.find_all(class_="sqs-block html-block sqs-block-html")[2]

    # The final two <p>s contain the count of anonymous signatories and a disclaimer,
    # which are removed
    names_html = names_div.find_all("p")[:-2]

    # At this point get_text will return what we want. There are some empty names,
    # so use filter to strip them out
    return list(filter(None, [name.get_text() for name in names_html]))

