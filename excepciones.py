
import re


class EmptyEmailError(Exception):
    pass
class InvalidEmailError(Exception):
    pass

class UnrecognizedEmailError(Exception):
    pass


def login():
    usuario = ('vicente@eni.es')
    while True:
        try:
            email = input('-->')
            if email == '':
                raise EmptyEmailError

            elif not re.search(r'.*@.*\..*', email):
                raise InvalidEmailError
            
            elif email not in usuario:
                raise UnrecognizedEmailError

            nombre = email.split('@')[0]
            print(f'¡Bienvenido {nombre.capitalize()}!')
            break
        except EmptyEmailError:
            print('" " no es un email valido. Introduce un email valido.')
        except InvalidEmailError:
            print('Una dirección de correo electrónico debe tener el formato xxx@xxx.xx')
        except UnrecognizedEmailError:
            print('Cuenta bloqueda por un ataque.')
            break



login()

