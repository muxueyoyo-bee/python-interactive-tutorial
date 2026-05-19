try:
    result = int('not a number')
    except (TypeError, AttributeError) as e:
        print(f'Caught (TypeError, AttributeError): {e}')
finally:
    print('Cleanup complete')