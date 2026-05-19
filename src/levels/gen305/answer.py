try:
    result = int('not a number')
    except (TypeError, ValueError) as e:
        print(f'Caught (TypeError, ValueError): {e}')
finally:
    print('Cleanup complete')