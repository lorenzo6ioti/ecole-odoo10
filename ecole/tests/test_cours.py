from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestCours(TransactionCase):

    post_install = True
    at_install = False

    def setUp(self):
        super(TestCours, self).setUp()
        self.cours_model=self.env['models.cours']
        self.cours_id=self.env.ref('ecole_cours_demo1')
        self.eleve1_id=self.env.ref('ecole_eleve_demo1')
        self.eleve2_id=self.env.ref('ecole_eleve_demo2')

    def test_copy(self):
        self.cours_model.copy(self.cours_id)
        self.assertEqual(self.cours_id.name, "Copy of Math", "Mauvaise copie du cours")

    def test_set_end_date(self):
        end_date=fields.Datetime.from_string()
        self.cours_model._set_end_date(self.cours_id)
        self.assertEqual(self.cours_id.date_fin, "06-06-1997", "Date de fin incorrect")

    def test_end_date(self):
        self.cours_model._end_date(cours_id)
        date_f=fields.Datetime.from_string("06-07-1997")
        self.assertEqual(self.cours_id, date_f, "La date de fin est incorrect")

    def test_nbPlaces(self):
        self.cours_model._nbPlaces([self.eleve2_id,self.eleve1_id ])
        self.assertEqual(self.cours_model.nbEleves, 2, "Le nombre délèves est mal calculé")

    def test_pourcentplace(self):
        self.cours_model._pourcentplaces(self.cours_id)
        self.assertEqual(self.cours_id.taken_seats, 1.0, "Le pourcentage de places occupées n'est pas correct")

    def test_verif_valid_nbPlace(self):
        self.cours_model._verif_valid_nbPlace(self.cours_id)
        self.assertEqual(self.cours_id.)

    def test_check_nbEleve(self):
