try:
    result = int('not a number')
    except requests.exceptions.HTTPError as e:
        print(f'Caught requests.exceptions.HTTPError: {e}')
finally:
    print('Cleanup complete')