try:
    result = int('not a number')
    except (LookupError, TypeError) as e:
        print(f'Caught (LookupError, TypeError): {e}')
    except (TypeError, AttributeError, UnsupportedOperation) as e:
        print(f'Caught (TypeError, AttributeError, UnsupportedOperation): {e}')
    except DecodeError as e:
        print(f'Caught DecodeError: {e}')
finally:
    print('Cleanup complete')