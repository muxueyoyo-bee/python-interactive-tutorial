try:
    result = int('not a number')
    except queue.Empty as e:
        print(f'Caught queue.Empty: {e}')
finally:
    print('Cleanup complete')