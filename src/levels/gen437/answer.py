try:
    result = int('not a number')
    except json.JSONDecodeError as e:
        print(f'Caught json.JSONDecodeError: {e}')
finally:
    print('Cleanup complete')