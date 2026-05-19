try:
    result = int('not a number')
    except CookieError as e:
        print(f'Caught CookieError: {e}')
finally:
    print('Cleanup complete')