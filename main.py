from src.log import setup_custom_logger

logger = setup_custom_logger(__name__)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logger.info('Inicio')
    try:
        print_hi('PyCharm')
    except Exception as ex:
        logger.exception(ex)
        input("Press Enter to close...")
    except KeyboardInterrupt as key:
        logger.warning("Se finaliza ejecucion de proceso.")
        input("Press Enter to close...")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
