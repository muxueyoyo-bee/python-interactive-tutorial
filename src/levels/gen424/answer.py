try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except urllib3.exceptions.HTTPError as e:
        print(f'Caught urllib3.exceptions.HTTPError: {e}')
finally:
    print('Cleanup complete')