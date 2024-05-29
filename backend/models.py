# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class Canasta(models.Model):
    id_canasta = models.AutoField(
        db_column="ID_Canasta", primary_key=True
    )  # Field name made lowercase.
    nombre = models.CharField(
        db_column="Nombre", max_length=50
    )  # Field name made lowercase.
    descripcion = models.CharField(
        db_column="Descripcion", max_length=200
    )  # Field name made lowercase.
    precio = models.DecimalField(
        db_column="Precio", max_digits=5, decimal_places=2, blank=True, null=True
    )  # Field name made lowercase.
    fk_canastaproductos = models.IntegerField(
        db_column="fk_canastaProductos", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "canasta"

    def __str__(self):
        return f"canasta: {self.nombre}"


class Canastaproductos(models.Model):
    id_canasta = models.OneToOneField(
        Canasta, models.DO_NOTHING, db_column="id_canasta", primary_key=True
    )  # The composite primary key (id_canasta, id_producto) found, that is not supported. The first column is selected.
    id_producto = models.ForeignKey(
        "Productos", models.DO_NOTHING, db_column="id_producto"
    )

    class Meta:
        managed = False
        db_table = "canastaproductos"
        unique_together = (("id_canasta", "id_producto"),)


class Cliente(models.Model):
    id = models.IntegerField(
        db_column="ID", primary_key=True
    )  # Field name made lowercase.
    nombre = models.CharField(
        db_column="Nombre", max_length=70, blank=True, null=True
    )  # Field name made lowercase.
    apellido_paterno = models.CharField(
        db_column="Apellido_Paterno", max_length=20
    )  # Field name made lowercase.
    apellido_materno = models.CharField(
        db_column="Apellido_Materno", max_length=20
    )  # Field name made lowercase.
    direccion = models.CharField(
        db_column="Direccion", max_length=255
    )  # Field name made lowercase.
    telefono = models.CharField(max_length=11)
    correo_electronico = models.CharField(
        db_column="Correo_Electronico", max_length=50
    )  # Field name made lowercase.
    numero_bancario = models.CharField(
        db_column="Numero_Bancario", max_length=20, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "cliente"


class Detallespedido(models.Model):
    id = models.IntegerField(
        db_column="ID", primary_key=True
    )  # Field name made lowercase.
    pedidoid = models.ForeignKey(
        "Pedido", models.DO_NOTHING, db_column="PedidoID", blank=True, null=True
    )  # Field name made lowercase.
    productoid = models.ForeignKey(
        "Productos", models.DO_NOTHING, db_column="ProductoID", blank=True, null=True
    )  # Field name made lowercase.
    cantidad = models.IntegerField(blank=True, null=True)
    preciounitario = models.DecimalField(
        db_column="precioUnitario",
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "detallespedido"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        "DjangoContentType", models.DO_NOTHING, blank=True, null=True
    )
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class Pedido(models.Model):
    id_pedido = models.IntegerField(
        db_column="ID_Pedido", primary_key=True
    )  # Field name made lowercase.
    clienteid = models.ForeignKey(
        Cliente, models.DO_NOTHING, db_column="clienteID", blank=True, null=True
    )  # Field name made lowercase.
    repartidorid = models.ForeignKey(
        "Repartidores",
        models.DO_NOTHING,
        db_column="RepartidorID",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    estado = models.CharField(
        db_column="Estado", max_length=25, blank=True, null=True
    )  # Field name made lowercase.
    fechahorapedido = models.DateTimeField(
        db_column="FechaHoraPedido", blank=True, null=True
    )  # Field name made lowercase.
    fechahoraentrega = models.DateTimeField(
        db_column="FechaHoraEntrega", blank=True, null=True
    )  # Field name made lowercase.
    direccion = models.CharField(max_length=255, blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "pedido"


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "productos"

    def __str__(self):
        return f"{self.nombre}"


class Repartidores(models.Model):
    id = models.IntegerField(
        db_column="ID", primary_key=True
    )  # Field name made lowercase.
    nombre = models.CharField(
        db_column="Nombre", max_length=100, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "repartidores"


class Transferencias(models.Model):
    id = models.IntegerField(
        db_column="ID", primary_key=True
    )  # Field name made lowercase.
    ordenid = models.ForeignKey(
        Pedido, models.DO_NOTHING, db_column="OrdenID"
    )  # Field name made lowercase.
    monto = models.DecimalField(
        db_column="Monto", max_digits=10, decimal_places=2, blank=True, null=True
    )  # Field name made lowercase.
    fechahoratransferencia = models.DateTimeField(
        db_column="FechaHoraTransferencia", blank=True, null=True
    )  # Field name made lowercase.
    tipodetransferencia = models.CharField(
        db_column="TipoDeTransferencia", max_length=50
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "transferencias"
