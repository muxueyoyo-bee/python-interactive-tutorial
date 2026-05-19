try:
    result = int('not a number')
    except (InvalidInputError, OSError) as e:
        print(f'Caught (InvalidInputError, OSError): {e}')
    except OSError as e:
        print(f'Caught OSError: {e}')
finally:
    print('Cleanup complete')