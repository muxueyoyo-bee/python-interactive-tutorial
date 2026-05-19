try:
    result = int('not a number')
    except (ValueError, IndexError) as e:
        print(f'Caught (ValueError, IndexError): {e}')
    except ValueError as e:
        print(f'Caught ValueError: {e}')
finally:
    print('Cleanup complete')