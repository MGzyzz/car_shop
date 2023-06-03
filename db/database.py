from utils import id_gen


class Database:
    product = [
        {'id': next(id_gen), 'make': 'Mercedes Benz', 'year': '2002', 'price': '6000',
         'image': 'https://s.aolcdn.com/commerce/autodata/images/20MBGEA1.jpg',
         'description': 'C230 Sports Coupe, a car designed to attract first-time Mercedes buyers with its combination of style, space, and a very complete equipment package',
         'contacts': 'Please contact by email sale@carsale.com or phone 555 555 555'},
        {'id': next(id_gen), 'make': 'Toyota Camry', 'year': '2015', 'price': '18000',
         'image': 'https://s.aolcdn.com/commerce/autodata/images/20MBGEA1.jpg',
         'description': 'C500 Sports Coupe, a car designed to attract first-time Mercedes buyers with its combination of style, space, and a very complete equipment package',
         'contacts': 'Please contact by email sale@carsale.com or phone 555 555 555'},
        {'id': next(id_gen), 'make': 'Lexus E300', 'year': '2020', 'price': '37000',
         'image': 'https://s.aolcdn.com/commerce/autodata/images/20MBGEA1.jpg',
         'description': 'C700 Sports Coupe, a car designed to attract first-time Mercedes buyers with its combination of style, space, and a very complete equipment package',
         'contacts': 'Please contact by email sale@carsale.com or phone 555 555 555'},
    ]

    @classmethod
    def all(cls):
        return cls.product

    @classmethod
    def add(cls, post: dict[str, str]):
        post_id = int(post["id"])
        post["id"] = post_id
        cls.product.append(post)

    @classmethod
    def find_by_id(cls, id):
        for post in cls.product:
            if post.get('id') == id:
                return post

        else:
            return None
