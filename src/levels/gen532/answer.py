try:
    result = int('not a number')
    except TemplateNotFound as e:
        print(f'Caught TemplateNotFound: {e}')
finally:
    print('Cleanup complete')