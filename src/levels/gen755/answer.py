try:
    result = int('not a number')
    except PackageInfoError as e:
        print(f'Caught PackageInfoError: {e}')
finally:
    print('Cleanup complete')