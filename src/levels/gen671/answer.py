try:
    result = int('not a number')
    except (ValueError, TypeError) as e:
        print(f'Caught (ValueError, TypeError): {e}')
    except PydanticUserError as e:
        print(f'Caught PydanticUserError: {e}')
finally:
    print('Cleanup complete')