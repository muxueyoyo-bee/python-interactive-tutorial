try:
    result = int('not a number')
    except (nodes.Impossible, Exception) as e:
        print(f'Caught (nodes.Impossible, Exception): {e}')
    except CompilerExit as e:
        print(f'Caught CompilerExit: {e}')
    except IndexError as e:
        print(f'Caught IndexError: {e}')
finally:
    print('Cleanup complete')