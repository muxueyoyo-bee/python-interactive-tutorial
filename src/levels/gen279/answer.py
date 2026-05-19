try:
    result = int('not a number')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
    except ValidationError as e:
        print(f'Caught ValidationError: {e}')
finally:
    print('Cleanup complete')