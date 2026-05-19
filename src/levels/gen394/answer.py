try:
    result = int('not a number')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
    except NoSuchOption as e:
        print(f'Caught NoSuchOption: {e}')
    except UsageError as e:
        print(f'Caught UsageError: {e}')
finally:
    print('Cleanup complete')