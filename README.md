# Unicode Babel

Is a easy to use python package for generating random unicode characters.

It's ideal for use in your tests or tools, Allowing you to quickly identify bugs and data processing issues.

* Easy to use iterator for repeated tests
* Unicode Planes 0, 1 and 2
* Python 3.6+
* Free  to use and open source

## Getting started:

To install:
```bash
pip install unicode-babel
```

This code:
```python
from unicode_babel import tools, filters

genny = tools.CodePointGenerator()

for point in genny.random_codepoints(10, filters.filter_out_if_no_name):
    print(point)

```
Will output 10 random unicode code-points from the Basic Multilingual Plane, filtered to ensure only valid named code-points are returned.:
```
ᓆ
ᗡ
ꋛ
販
ۅ
䶣
楨
蟷
䔉
ݥ
```
As these are valid characters from valid code-points you can use these anywhere that clams to accept text.

If you want to really put the cat among the pigeons try this code:
```python
from unicode_babel import *

genny = tools.CodePointGenerator()

for point in genny.random_codepoints(10, filters.filter_in_if_no_name):
    print(point)

```

...it will fail badly, as the code-points filtered-in can not be encoded, the codepoints don't map to a 'character'.
The error might look something like this:

```dos
Traceback (most recent call last):
  File "tryout.py", line 6, in <module>
    print(point)
UnicodeEncodeError: 'utf-8' codec can't encode character '\ud8b4' in position 0: surrogates not allowed
```
But this nonetheless might be useful in unit testing etc.


Or you can get individual code-points and them use them with other tools, for example Selenium Webdriver:

```python
from unicode_babel import tools, filters
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://www.google.com")

data_genny = tools.CodePointGenerator()
unusual_char = data_genny.get_random_codepoint(filters.filter_out_if_no_name)

search_box = browser.find_element_by_name("q")
search_box.send_keys(unusual_char + Keys.RETURN)

```
Assuming you have Chromedriver in your path, that should open Google and search for a random character.


### License:
Copyright © 2020 Peter Houghton

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
