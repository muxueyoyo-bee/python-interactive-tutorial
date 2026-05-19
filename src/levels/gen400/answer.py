try:
    result = int('not a number')
    except EnumStringValueParseError as e:
        print(f'Caught EnumStringValueParseError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')