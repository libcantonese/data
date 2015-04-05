# Scraper for 中英對照香港學校中文學習基礎字詞
## Introduction
[中英對照香港學校中文學習基礎字詞](http://www.edbchinese.hk/lexlist_en/)
contains Chinese vocabulary taught in Hong Kong primary schools.

We think it might provides a good data source for related vocabulary feature in
input method editors.

## Usage
`download.py` downloads HTML data for all 4762 characters.

`scraper.py` scrapes downloaded data and save the result to several txt files,
it depends on `lxml` and `beautifulsoup4` PyPI package.
