# ECU

A simple and minimalist CLI helper tool.

## Installation

Package is available on PyPI.
```
pip install ecu
```

## Usage

Import the library in your project, and use the provided
functions as you want.
```py
import ecu
```

#### Header display
```py
ecu.frame('Hello, world', 'Have some text')
```

#### Selection input
```py
ecu.select('Choose a fruit', ['Banana', 'Carrot', 'Kiwi'])
```

#### Confirm input
```py
ecu.confirm('Do you really want to do this?')
```

#### Spinner display

```py
with ecu.spin()
```

## License

Licensed under MIT. See `LICENSE`.