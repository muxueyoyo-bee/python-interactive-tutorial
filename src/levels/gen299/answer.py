try:
    result = int('not a number')
    except RequestError as e:
        print(f'Caught RequestError: {e}')
finally:
    print('Cleanup complete')