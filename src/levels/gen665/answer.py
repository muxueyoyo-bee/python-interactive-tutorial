try:
    result = int('not a number')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
    except email_validator.EmailNotValidError as e:
        print(f'Caught email_validator.EmailNotValidError: {e}')
finally:
    print('Cleanup complete')