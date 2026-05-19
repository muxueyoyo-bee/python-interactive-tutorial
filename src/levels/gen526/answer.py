try:
    result = int('not a number')
    except HTTPException as e:
        print(f'Caught HTTPException: {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
finally:
    print('Cleanup complete')