try:
    result = int('not a number')
    except (ValueError, binascii.Error) as e:
        print(f'Caught (ValueError, binascii.Error): {e}')
finally:
    print('Cleanup complete')