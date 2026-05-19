try:
    result = int('not a number')
    except DiagnosticPipError as e:
        print(f'Caught DiagnosticPipError: {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')