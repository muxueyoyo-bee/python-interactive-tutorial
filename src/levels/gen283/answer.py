try:
    result = int('not a number')
    except (MultiPartParserError, TooManyFilesSent) as e:
        print(f'Caught (MultiPartParserError, TooManyFilesSent): {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    except LookupError as e:
        print(f'Caught LookupError: {e}')
finally:
    print('Cleanup complete')