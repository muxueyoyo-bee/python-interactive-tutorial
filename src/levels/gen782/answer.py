try:
    result = int('not a number')
    except (ModuleNotFound, CompileError) as e:
        print(f'Caught (ModuleNotFound, CompileError): {e}')
    except (OSError, IPCException) as e:
        print(f'Caught (OSError, IPCException): {e}')
    except (OSError, UnicodeDecodeError, DecodeError) as e:
        print(f'Caught (OSError, UnicodeDecodeError, DecodeError): {e}')
finally:
    print('Cleanup complete')