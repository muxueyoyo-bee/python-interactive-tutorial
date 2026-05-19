try:
    result = int('not a number')
    except OSError as e:
        print(f'Caught OSError: {e}')
    except TemplateNotFound as e:
        print(f'Caught TemplateNotFound: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
finally:
    print('Cleanup complete')