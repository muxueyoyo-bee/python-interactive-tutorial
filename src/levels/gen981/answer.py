try:
    result = int('not a number')
    except (ImportError, OSError) as e:
        print(f'Caught (ImportError, OSError): {e}')
    except (ImportError, SyntaxError) as e:
        print(f'Caught (ImportError, SyntaxError): {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
finally:
    print('Cleanup complete')