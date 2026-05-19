try:
    result = int('not a number')
    except urllib.error.URLError as e:
        print(f'Caught urllib.error.URLError: {e}')
finally:
    print('Cleanup complete')