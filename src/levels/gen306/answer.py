try:
    result = int('not a number')
    except (TypeError, AttributeError) as e:
        print(f'Caught (TypeError, AttributeError): {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
finally:
    print('Cleanup complete')