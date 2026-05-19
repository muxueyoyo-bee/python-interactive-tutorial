try:
    result = int('not a number')
    except (OSError, UnicodeDecodeError, configparser.ParsingError) as e:
        print(f'Caught (OSError, UnicodeDecodeError, configparser.ParsingError): {e}')
    except AttributeError as e:
        print(f'Caught AttributeError: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')