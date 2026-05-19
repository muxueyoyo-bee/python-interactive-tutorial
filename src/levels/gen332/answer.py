try:
    result = int('not a number')
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f'Caught (FileNotFoundError, NotADirectoryError): {e}')
    except FileNotFoundError as e:
        print(f'Caught FileNotFoundError: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')