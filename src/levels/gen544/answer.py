try:
    result = int('not a number')
    except (ImportError, ValueError) as e:
        print(f'Caught (ImportError, ValueError): {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')