try:
    result = int('not a number')
    except RequestError as e:
        print(f'Caught RequestError: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
    except json.JSONDecodeError as e:
        print(f'Caught json.JSONDecodeError: {e}')
finally:
    print('Cleanup complete')