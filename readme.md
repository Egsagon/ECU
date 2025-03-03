# ECU

A simple CLI helper tool.

## Usage

```py
import ecu

# Selection
ecu.select('Choose a fruit', ['tomato', 'banana', 'peach'])

# Confirmation
ecu.confirm('Do you really want to do this?')

# Spinner for long tasks
with ecu.spin():
    ...
```

## License

Licensed under MIT. See `LICENSE`.