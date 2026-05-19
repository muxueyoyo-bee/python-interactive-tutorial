try:
    result = int('not a number')
    except TemplateSyntaxError as e:
        print(f'Caught TemplateSyntaxError: {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
finally:
    print('Cleanup complete')