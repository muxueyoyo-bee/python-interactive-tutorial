try:
    result = int('not a number')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    except util.CommandError as e:
        print(f'Caught util.CommandError: {e}')
finally:
    print('Cleanup complete')