try:
    result = int('not a number')
    except (ValueError, SyntaxError, MemoryError) as e:
        print(f'Caught (ValueError, SyntaxError, MemoryError): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')