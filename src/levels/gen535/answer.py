try:
    result = int('not a number')
    except BadRequest as e:
        print(f'Caught BadRequest: {e}')
finally:
    print('Cleanup complete')