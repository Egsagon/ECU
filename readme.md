# ECU
*A simple and minimalist CLI helper tool.*

This package was designed to help building CLI tools in python that will look more elegant than the built-in `print()` and `input()`, while not being overcomplicated.

## Installation
Package is available on PyPI.
```
pip install ecu
```

## Usage
Import the library in your project, and use the provided functions as you want.
```py
import ecu
```

#### Header display
```py
ecu.frame('Hello, world', 'Have some text')
```
![](.github/images/demo1.png)

#### Selection input
```py
ecu.select('Choose a fruit', ['Banana', 'Carrot', 'Kiwi'])
```
![](.github/images/demo2.png)

#### Confirm input
```py
ecu.confirm('Do you really want to do this?')
```
![](.github/images/demo3.png)

#### Spinner display
```py
with ecu.spin():
    # Do something slow
    time.sleep(5)
```
![](.github/images/demo4.png)

## License
Licensed under MIT. See `LICENSE`.
