try:
    result = int('not a number')
    except urllib.error.HTTPError as e:
        print(f'Caught urllib.error.HTTPError: {e}')
finally:
    print('Cleanup complete')