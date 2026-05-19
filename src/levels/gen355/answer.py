try:
    result = int('not a number')
    except (AttributeError, OSError) as e:
        print(f'Caught (AttributeError, OSError): {e}')
    except KeyboardInterrupt as e:
        print(f'Caught KeyboardInterrupt: {e}')
finally:
    print('Cleanup complete')