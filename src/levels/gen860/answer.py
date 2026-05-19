try:
    result = int('not a number')
    except (KeyboardInterrupt, EOFError) as e:
        print(f'Caught (KeyboardInterrupt, EOFError): {e}')
    except ImportError as e:
        print(f'Caught ImportError: {e}')
    except SystemExit as e:
        print(f'Caught SystemExit: {e}')
finally:
    print('Cleanup complete')