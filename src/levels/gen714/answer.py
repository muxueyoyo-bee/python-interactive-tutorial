try:
    result = int('not a number')
    except (ImportError, AttributeError) as e:
        print(f'Caught (ImportError, AttributeError): {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
finally:
    print('Cleanup complete')