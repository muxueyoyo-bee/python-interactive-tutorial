try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except urllib.error.HTTPError as e:
        print(f'Caught urllib.error.HTTPError: {e}')
finally:
    print('Cleanup complete')