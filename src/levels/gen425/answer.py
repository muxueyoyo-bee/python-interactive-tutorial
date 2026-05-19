try:
    result = int('not a number')
    except HttpError as e:
        print(f'Caught HttpError: {e}')
finally:
    print('Cleanup complete')