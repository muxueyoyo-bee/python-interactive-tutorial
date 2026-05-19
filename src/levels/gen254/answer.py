try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except json.decoder.JSONDecodeError as e:
        print(f'Caught json.decoder.JSONDecodeError: {e}')
finally:
    print('Cleanup complete')