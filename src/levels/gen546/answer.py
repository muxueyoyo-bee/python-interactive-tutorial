try:
    result = int('not a number')
    except db.IntegrityError as e:
        print(f'Caught db.IntegrityError: {e}')
finally:
    print('Cleanup complete')