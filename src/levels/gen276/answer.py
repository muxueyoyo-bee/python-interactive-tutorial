try:
    result = int('not a number')
    except ValidationError as e:
        print(f'Caught ValidationError: {e}')
finally:
    print('Cleanup complete')