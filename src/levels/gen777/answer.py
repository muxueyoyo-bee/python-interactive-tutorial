try:
    result = int('not a number')
    except PolyTranslationError as e:
        print(f'Caught PolyTranslationError: {e}')
finally:
    print('Cleanup complete')