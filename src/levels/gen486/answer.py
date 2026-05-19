try:
    result = int('not a number')
    except cv.error as e:
        print(f'Caught cv.error: {e}')
finally:
    print('Cleanup complete')