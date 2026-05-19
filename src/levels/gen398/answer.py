try:
    result = int('not a number')
    except (KeyboardInterrupt, EOFError) as e:
        print(f'Caught (KeyboardInterrupt, EOFError): {e}')
    except KeyError as e:
        print(f'Caught KeyError: {e}')
    except UsageError as e:
        print(f'Caught UsageError: {e}')
finally:
    print('Cleanup complete')