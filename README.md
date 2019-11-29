# Unicode Babel

Is a easy to use python package for generating random unicode characters.

It's ideal for use in your tests or tools, Allowing you to quickly identify bugs and data processing issues.

* Easy to use iterator for repeated tests
* Unicode Planes 0 and 1 (...more coming soon)
* Python 3.x
* Free  to use and open source

## Getting started:

This simple code:
```python
from unicode_babel import tools, filters

genny = tools.CodePointGenerator()

for point in genny.random_codepoints(10, filters.filter_out_if_no_name)
    print(point)

```
Will out put 10 random unicode code-points rom the Basic Multilingual Plane, filtered to ensure only valid named code-points are returned.:
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

### License:
Copyright © 2019 Peter Houghton

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
