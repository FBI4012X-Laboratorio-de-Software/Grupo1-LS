from telas.imagens import front
import logging

def main() -> None:
    logging.basicConfig(filename='.plenosono.log',
                        level=logging.DEBUG,
                        format='%(asctime)s | %(levelname)s : %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # logging.basicConfig(handlers=[logging.FileHandler('.plenosono.log', 'a', 'utf-8')])                  

    logging.info('-------------------Aplicacao iniciada-------------------')   
    front()
    logging.info('-------------------Aplicacao encerrada-------------------')


if __name__ == '__main__':
    main()
