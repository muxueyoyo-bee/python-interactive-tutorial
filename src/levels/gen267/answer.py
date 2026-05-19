try:
    result = int('not a number')
    except OSError as e:
        print(f'Caught OSError: {e}')
    except WebSocketDisconnect as e:
        print(f'Caught WebSocketDisconnect: {e}')
finally:
    print('Cleanup complete')