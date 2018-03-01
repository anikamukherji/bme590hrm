# Duke BME590 Assignment 6 - Heart Rate Monitor

## Anika Mukherji

## How to run via example...
```
x = HeartRateMonitor("test_data/test_data1.csv")
x.calculate_all_values()
```
All values are now stored in the HeartRateMonitor object
```
>>> print(x.mean_hr_bpm)
75.78947368421053

>>> print(x.num_beats)
35
```
To graph...
```
x.graph_data()
```

*Note* -> if the matplotlib import throws a MacOX runtime error create
a user config file with...
```
echo "backend: TkAgg" >> ~/.matplotlib/matplotlibrc
```

[![Build Status](https://travis-ci.org/anikamukherji/bme590hrm.svg?branch=master)](https://travis-ci.org/anikamukherji/bme590hrm)

MIT License

Copyright (c) [2018] [Anika Mukherji]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
