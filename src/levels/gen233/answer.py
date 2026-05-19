try:
    result = int('not a number')
    except (OSError, TypeError) as e:
        print(f'Caught (OSError, TypeError): {e}')
    except (TypeError, AttributeError, KeyError) as e:
        print(f'Caught (TypeError, AttributeError, KeyError): {e}')
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f'Caught (subprocess.CalledProcessError, FileNotFoundError): {e}')
finally:
    print('Cleanup complete')