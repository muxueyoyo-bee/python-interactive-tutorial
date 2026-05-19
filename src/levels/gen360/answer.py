try:
    result = int('not a number')
    except BaseException as e:
        print(f'Caught BaseException: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
    except h11.LocalProtocolError as e:
        print(f'Caught h11.LocalProtocolError: {e}')
finally:
    print('Cleanup complete')