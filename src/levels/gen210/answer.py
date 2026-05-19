try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except json.JSONDecodeError as e:
        print(f'Caught json.JSONDecodeError: {e}')
finally:
    print('Cleanup complete')