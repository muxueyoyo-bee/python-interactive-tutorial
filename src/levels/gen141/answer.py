try:
    result = int('not a number')
    except Exception as e:
        print(f'Caught Exception: {e}')
    except zipfile.BadZipFile as e:
        print(f'Caught zipfile.BadZipFile: {e}')
finally:
    print('Cleanup complete')