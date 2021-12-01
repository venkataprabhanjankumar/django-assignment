class UsersModel:
    # name of the apps we need to specify here
    route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin', 'users'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'UsersDb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'UsersDb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'UsersDb'
        return None


class ProductsModel:
    # name of the apps we need to specify here
    route_app_labels = {'products'}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'ProductsDb'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'ProductsDb'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == 'ProductsDb'
        return None
