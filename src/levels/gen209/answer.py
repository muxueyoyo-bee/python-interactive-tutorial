try:
    result = int('not a number')
    except yaml.YAMLError as e:
        print(f'Caught yaml.YAMLError: {e}')
finally:
    print('Cleanup complete')