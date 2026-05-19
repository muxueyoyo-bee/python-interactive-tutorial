try:
    result = int('not a number')
    except (TypeError, ValueError) as e:
        print(f'Caught (TypeError, ValueError): {e}')
    except (subprocess.CalledProcessError, OSError) as e:
        print(f'Caught (subprocess.CalledProcessError, OSError): {e}')
    except Exception as e:
        print(f'Caught Exception: {e}')
finally:
    print('Cleanup complete')