try:
    result = int('not a number')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except ZoneInfoNotFoundError as e:
        print(f'Caught ZoneInfoNotFoundError: {e}')
    except revision.MultipleHeads as e:
        print(f'Caught revision.MultipleHeads: {e}')
finally:
    print('Cleanup complete')