try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except HTTPException as e:
        print(f'Caught HTTPException: {e}')
    except TimeoutError as e:
        print(f'Caught TimeoutError: {e}')
finally:
    print('Cleanup complete')