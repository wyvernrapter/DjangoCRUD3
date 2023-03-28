BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "app_item" (
	"id"	integer NOT NULL,
	"name"	varchar(200) NOT NULL,
	"age"	integer,
	"sex"	integer NOT NULL,
	"memo"	text,
	"created_at"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
INSERT INTO "django_migrations" ("id","app","name","applied") VALUES (1,'contenttypes','0001_initial','2023-01-02 13:52:53.003311'),
 (2,'auth','0001_initial','2023-01-02 13:52:53.038044'),
 (3,'admin','0001_initial','2023-01-02 13:52:53.067057'),
 (4,'admin','0002_logentry_remove_auto_add','2023-01-02 13:52:53.089818'),
 (5,'admin','0003_logentry_add_action_flag_choices','2023-01-02 13:52:53.106350'),
 (6,'app','0001_initial','2023-01-02 13:52:53.118353'),
 (7,'contenttypes','0002_remove_content_type_name','2023-01-02 13:52:53.150689'),
 (8,'auth','0002_alter_permission_name_max_length','2023-01-02 13:52:53.172300'),
 (9,'auth','0003_alter_user_email_max_length','2023-01-02 13:52:53.192943'),
 (10,'auth','0004_alter_user_username_opts','2023-01-02 13:52:53.211585'),
 (11,'auth','0005_alter_user_last_login_null','2023-01-02 13:52:53.238385'),
 (12,'auth','0006_require_contenttypes_0002','2023-01-02 13:52:53.249839'),
 (13,'auth','0007_alter_validators_add_error_messages','2023-01-02 13:52:53.263836'),
 (14,'auth','0008_alter_user_username_max_length','2023-01-02 13:52:53.284820'),
 (15,'auth','0009_alter_user_last_name_max_length','2023-01-02 13:52:53.305820'),
 (16,'auth','0010_alter_group_name_max_length','2023-01-02 13:52:53.330412'),
 (17,'auth','0011_update_proxy_permissions','2023-01-02 13:52:53.355153'),
 (18,'auth','0012_alter_user_first_name_max_length','2023-01-02 13:52:53.393391'),
 (19,'sessions','0001_initial','2023-01-02 13:52:53.422784');
INSERT INTO "django_admin_log" ("id","object_id","object_repr","action_flag","change_message","content_type_id","user_id","action_time") VALUES (1,'1','羽鳥航',1,'[{"added": {}}]',7,1,'2023-01-02 14:04:40.739815'),
 (2,'2','rapter1996',1,'[{"added": {}}]',4,1,'2023-01-02 14:07:08.858637'),
 (3,'2','羽鳥航',2,'[{"changed": {"fields": ["Username", "First name", "Last name", "Email address", "Superuser status"]}}]',4,1,'2023-01-02 14:09:07.609660'),
 (4,'2','羽鳥航',2,'[{"changed": {"fields": ["Staff status"]}}]',4,1,'2023-01-02 14:09:55.938851');
INSERT INTO "app_item" ("id","name","age","sex","memo","created_at") VALUES (1,'羽鳥航',26,1,'administorater','2023-01-02 14:04:40.737275'),
 (2,'皐月龍斗',24,1,'maykiller','2023-01-03 13:59:43.370177'),
 (3,'山本五十六',65,1,'やって見せ

言って聞かせてさせてみて

褒めてやらねば人は動かじ','2023-01-03 14:01:50.488586');
INSERT INTO "django_content_type" ("id","app_label","model") VALUES (1,'admin','logentry'),
 (2,'auth','permission'),
 (3,'auth','group'),
 (4,'auth','user'),
 (5,'contenttypes','contenttype'),
 (6,'sessions','session'),
 (7,'app','item');
INSERT INTO "auth_permission" ("id","content_type_id","codename","name") VALUES (1,1,'add_logentry','Can add log entry'),
 (2,1,'change_logentry','Can change log entry'),
 (3,1,'delete_logentry','Can delete log entry'),
 (4,1,'view_logentry','Can view log entry'),
 (5,2,'add_permission','Can add permission'),
 (6,2,'change_permission','Can change permission'),
 (7,2,'delete_permission','Can delete permission'),
 (8,2,'view_permission','Can view permission'),
 (9,3,'add_group','Can add group'),
 (10,3,'change_group','Can change group'),
 (11,3,'delete_group','Can delete group'),
 (12,3,'view_group','Can view group'),
 (13,4,'add_user','Can add user'),
 (14,4,'change_user','Can change user'),
 (15,4,'delete_user','Can delete user'),
 (16,4,'view_user','Can view user'),
 (17,5,'add_contenttype','Can add content type'),
 (18,5,'change_contenttype','Can change content type'),
 (19,5,'delete_contenttype','Can delete content type'),
 (20,5,'view_contenttype','Can view content type'),
 (21,6,'add_session','Can add session'),
 (22,6,'change_session','Can change session'),
 (23,6,'delete_session','Can delete session'),
 (24,6,'view_session','Can view session'),
 (25,7,'add_item','Can add アイテム'),
 (26,7,'change_item','Can change アイテム'),
 (27,7,'delete_item','Can delete アイテム'),
 (28,7,'view_item','Can view アイテム');
INSERT INTO "auth_user" ("id","password","last_login","is_superuser","username","last_name","email","is_staff","is_active","date_joined","first_name") VALUES (1,'pbkdf2_sha256$390000$lDoUYjiVer1WkhRtiWnNfN$rr+y+66AQOOzoQbSWB9nUkbcKDX7UwXUsHA70ScuIbE=','2023-01-02 14:05:16.680162',1,'wata8100','','',1,1,'2023-01-02 13:54:23.300055',''),
 (2,'pbkdf2_sha256$390000$lHszYuT3eyHGTJgQF2KV1h$OXDvcz/Ve5xTMjd177HyNaPtRUAVSuMIbux9BC5kLfs=','2023-01-03 09:16:11.202821',1,'羽鳥航','ハトリ','wata8126@outlook.jp',1,1,'2023-01-02 14:07:08','ワタル');
INSERT INTO "django_session" ("session_key","session_data","expire_date") VALUES ('85hxq2gt8sq5nffe356rur33df4lt4ra','.eJxVjDsOwjAQBe_iGln-J6ak5wzRrneXBJAjxUmFuDtESgHtm5n3UgNs6zhsjZdhInVWTp1-N4Ty4LoDukO9zbrMdV0m1LuiD9r0dSZ-Xg7372CENn7rmMVC9iH5UJAEwQCDcdx77_qOI0u2Hg05yRQMUpIoKUeJve1CZ5N6fwDxvzff:1pCdP1:TNH4m2ogeFHQycEJO1P6BL-WITZv_WCszGS8HPp8yf8','2023-01-17 09:16:11.223803');
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
COMMIT;
