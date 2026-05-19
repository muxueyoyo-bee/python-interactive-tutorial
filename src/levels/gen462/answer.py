try:
    result = int('not a number')
    except nodes.Impossible as e:
        print(f'Caught nodes.Impossible: {e}')
finally:
    print('Cleanup complete')