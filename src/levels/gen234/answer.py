try:
    result = int('not a number')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
    except idna.IDNAError as e:
        print(f'Caught idna.IDNAError: {e}')
    except ipaddress.AddressValueError as e:
        print(f'Caught ipaddress.AddressValueError: {e}')
finally:
    print('Cleanup complete')