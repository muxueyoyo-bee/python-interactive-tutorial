try:
    result = int('not a number')
    except payload.LookupError as e:
        print(f'Caught payload.LookupError: {e}')
finally:
    print('Cleanup complete')