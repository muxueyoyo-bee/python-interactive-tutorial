try:
    result = int('not a number')
    except (tomllib.TOMLDecodeError, configparser.Error, ConfigTOMLValueError) as e:
        print(f'Caught (tomllib.TOMLDecodeError, configparser.Error, ConfigTOMLValueError): {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
    except VersionTypeError as e:
        print(f'Caught VersionTypeError: {e}')
finally:
    print('Cleanup complete')