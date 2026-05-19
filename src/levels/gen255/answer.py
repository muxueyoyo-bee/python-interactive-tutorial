try:
    result = int('not a number')
    except (UnicodeDecodeError, LookupError) as e:
        print(f'Caught (UnicodeDecodeError, LookupError): {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    except ModuleNotFoundError as e:
        print(f'Caught ModuleNotFoundError: {e}')
finally:
    print('Cleanup complete')