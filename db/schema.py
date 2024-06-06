'''  Schema Database Configurated for SQLITE Database  '''
from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.orm import sessionmaker, Session

from sqlalchemy.orm import declarative_base

from sqlalchemy import Column, String, Integer, Boolean, Float, Date, Time, DateTime, ForeignKey, ARRAY,Null

SQLALCHEMY_DATABASE_URL = "sqlite:///./db/globalpass.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False})
#Seesion HAndler
session = sessionmaker(autocommit=False, autoflush=False,bind=engine)

base = declarative_base()


class db_terms(base):

    __tablename__ = "terms"

    id    =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False)
    name  = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

class db_users(base):


    __tablename__ = "users"

    id    =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False)
    email  = Column(String(255), nullable=False, unique=True)
    encrypted_password = Column(String(255), nullable=False)
    reset_password_token = Column(String(255), nullable=False, unique = True)
    reset_password_sent_at = Column(DateTime, nullable=False)
    remember_created_at = Column(DateTime, nullable=False)
    sign_in_count         = Column(Integer, nullable=False, default= 0)
    current_sign_in_at = Column(DateTime, nullable=False)
    last_sign_in_at = Column(DateTime, nullable=False)
    current_sign_in_ip  = Column(String(255), nullable=False)
    last_sign_in_ip      = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name  = Column(String(255), nullable=False)
    birthday     = Column(Date, nullable=False)
    gender = Column(String(255), nullable=False)
    language = Column(String(255), nullable=False)
    phone_number = Column(String(50), nullable=False)
    street_address = Column(String(255), nullable=False)
    apartment = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    state_province = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    postal_code = Column(String(255), nullable=False)
    role = Column(Integer, nullable=False)
    provider = Column(String(50), nullable=False, default =Null)
    uid = Column(String(50), nullable=False, default =Null)
    username  = Column(String(255), nullable=False)
    stage = Column(String(255), nullable=False)
    recent_university_id = Column(Integer,ForeignKey("universities.id") , nullable=False)
    secondary_education_school_name = Column(String(255), nullable=False)
    secondary_education_start_date = Column(Date, nullable=False)
    secondary_education_graduration_date = Column(Date, nullable=False)
    post_secondary_education_school_name = Column(String(255), nullable=False)
    post_secondary_education_degree_type = Column(String(255), nullable=False)
    post_secondary_education_street_address = Column(String(255), nullable=False)
    post_secondary_education_city = Column(String(255), nullable=False)
    post_secondary_education_state_province = Column(String(255), nullable=False)
    post_secondary_education_country = Column(String(255), nullable=False)
    post_secondary_education_postal_code = Column(String(255), nullable=False)
    able_to_pay = Column(String(255), nullable=False)
    country_to_study = Column(String(255), nullable=False)
    degree_to_study = Column(String(255), nullable=False)
    when_to_start = Column(String(255), nullable=False)
    recruiter_number_of_student_or_immigrants   = Column(String(255), nullable=False)
    recruiter_top_destinations  = Column(String(255), nullable=False)
    recruiter_number_of_employees  = Column(String(255), nullable=False)
    recruiter_agency_earning  = Column(String(255), nullable=False)
    recruiter_begin_recruitment_date = Column(String(255), nullable=False)
    recruiter_company_name = Column(String(255), nullable=False)
    sent_immigration_post_purchase_email = Column(Boolean, default=False, nullable=False)
    confirmation_token = Column(String(255), nullable=False, unique=True)
    confirmed_at = Column(DateTime, nullable=False)
    confirmation_sent_at = Column(DateTime, nullable=False)
    from_job_portal = Column(Boolean)
    recruiter_help_with_immigration = Column(String(255))
    recruiter_facebook = Column(String(255))
    recruiter_instagram = Column(String(255))
    recruiter_twitter = Column(String(255))
    recruiter_linkedin = Column(String(255))
    partner = Column(String(255))
    questionnaires = Column(String(255))

class db_visas(base):

    __tablename__ = "visas"

    id    =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


class db_applications(base):
    __tablename__ = "Applications"
    
    id      = Column(Integer,primary_key = True, autoincrement= True)
    status  = Column(String(50), nullable= False)
    amount  = Column(Float, nullable= False)
    currency = Column(Float, nullable= False)
    created_at = Column(DateTime, nullable= False)
    updated_at = Column(Float, nullable= False)
    user_id     = Column(Integer, nullable= False , index = True)
    program_id   = Column(Integer, nullable= False, index = True)
    term_id     = Column(Integer, nullable= False, index= True)


class db_categories(base):
    __tablename__ = "Categories"
    
    id = Column(Integer, primary_key=True,autoincrement=False, index=True)
    name = Column(String(255), nullable= False)
    created_at = Column(DateTime, nullable= False)
    updated_at = Column(DateTime, nullable= False)

class db_documents(base):
    __tablename__ = "documents"

    id          =  Column(Integer, primary_key= True, autoincrement= True, index=True,nullable= False)
    object_key  = Column(String(255), nullable= False)
    document_type = Column(Integer, nullable= False)
    user_id      = Column(Integer, ForeignKey("users.id"), nullable= False)
    created_at      = Column(DateTime, nullable= False)
    updated_at = Column(DateTime, nullable= False)


class db_immigration_profiles(base): 

    __tablename__ = "ImmigrationProfiles"

    id = Column(Integer,primary_key= True, autoincrement= True, index=True)
    where_to_immigration         = Column(String(50))
    already_applied_for_visa    =  Column(String(50))
    interested_in_visa_type     =  Column(String(50))
    admitted_to_university_or_job_offer =   Column(String(50))
    taken_english_or_french_test=   Column(String(50))
    ever_traveled_to_canada_or_us =  Column(String(50))
    family_in_canada_or_us       =  Column(String(50))
    highest_level_of_education   =  Column(String(50))
    current_job                 =  Column(String(50))
    year_of_work_experience      =  Column(String(50))
    monthly_salary             =  Column(String(50))
    able_to_afford              =  Column(String(50))
    pecific_skills             =  Column(String(50))
    dependents                  =  Column(String(50))
    user_id      =   Column(Integer, ForeignKey ("users.id"), nullable = False)
    created_at =  Column(DateTime,nullable=False)
    updated_at =  Column(DateTime, nullable=False)
    is_currently_an_university_student =  Column(String(50), nullable=False)
    enrolled_in_university_before =  Column(String(50))
    university_enrolled_in =  Column(String(50))
    highschool_gpa          =  Column(String(50))
    ielts_overall           =  Column(String(50))
    ielts_reading           =  Column(String(50))
    ielts_writing           =  Column(String(50))
    ielts_speaking          =  Column(String(50))
    ielts_listening         =  Column(String(50))
    intension_of_coming_to_canada =  Column(String(50))
    programs_interested_in=  Column(String(50))
    tuition_budget =  Column(String(50))
    have_fund_available =  Column(String(50))
    completed_secondary_school_in_english =  Column(String(50))
    taken_standardized_admissions_tests =  Column(String(50))
    work_experience_company_name =  Column(String(50))
    work_experience_job_title =  Column(String(50))
    work_experience_start_date  =  Column(String(50))
    work_experience_end_date =  Column(String(50))
    applied_for_permanent_residence_before =  Column(String(50))
    been_in_canada_before =  Column(String(50))
    length_stayed_in_canada =  Column(String(50))
    passport_number =  Column(String(50))
    fund_available =  Column(String(50))
    is_family_member_in_canada =  Column(String(50))
    family_member_in_canada =  Column(String(50))
    has_traveled_outside_of_country =  Column(String(50))
    country_traveled_to =  Column(String(50))
    country_traveled_to_date =  Column(String(50))
    first_name =  Column(String(255), nullable= False)
    last_name =  Column(String(255), nullable=False)
    birthday =  Column(Date,nullable= False)
    title =  Column(String(125))
    country_of_citizenship =  Column(String(125))
    province_of_residence =  Column(String(125))
    city_of_residence =  Column(String(125))
    postal_code =  Column(String(50))
    language =  Column(String(50))
    email =  Column(String(255))
    phone_number =  Column(String(50))
    english_is_first_language =  Column(Boolean)
    emergency_contact_name =  Column(String(50))
    emergency_contact_email =  Column(String(50))
    emergency_contact_phone_number =  Column(String(50))


class jwt_denylists(base):

    __tablename__ = "jwt_denylists"

    id      = Column(Integer,primary_key=True, autoincrement=True, index=True)
    jti      =  Column(String(255), nullable=False, index=True)
    exp    =  Column(DateTime, nullable=False)
    created_at=  Column(DateTime, nullable=False)
    updated_at=  Column(DateTime , nullable=False)

class db_messages(base) :

    __tablename__ = "Messages"

    id = Column(Integer, primary_key= True,autoincrement=True, index=True )
    body =  Column(String(255), nullable=False)
    created_at =  Column(DateTime, nullable=False)
    updated_at =  Column(DateTime, nullable=False)
    user_id      =  Column(Integer, ForeignKey  ("users.id") , nullable=False)
    admin_id     =  Column(Integer, ForeignKey  ("users.id") , nullable=False)


class db_order_applications(base):
     __tablename__ = "OrdersApplications"

     id =   Column(Integer , primary_key=True , nullable=False)
     created_at   =  Column(DateTime, nullable=False)
     updated_at   =  Column(DateTime, nullable=False)
     application_id =  Column(Integer,ForeignKey("Applications.id"), nullable=False)
     order_id       =  Column(Integer,ForeignKey("Orders.id"), nullable=False)


class db_orders(base): 
    __tablename__ = "Orders"

    id         =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    card_number = Column(String(255))
    expiration = Column(String(255))
    address = Column(String(255))
    city = Column(String(255))
    country = Column(String(255))
    state = Column(String(255))
    postal = Column(String(255))
    created_at = Column(String(255), nullable=False)
    updated_at = Column(String(255), nullable=False)
    user_id = Column(Integer,ForeignKey ("users.id"), nullable=False)
    cost = Column(String(255), nullable=False)
    stripe_payment_intent_id = Column(String(255), nullable=False)
    status = Column(Integer, nullable=False)



class db_packages(base):
    __tablename__ = "Packages"

    id    =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False)
    name  = Column(String(255), nullable=False)
    description  = Column(String(255), nullable=False)
    rice  = Column(Float, nullable=False)
    created_at  = Column(DateTime, nullable=False)
    updated_at  = Column(DateTime, nullable=False)


class passports(base):

    __tablename__ = "Passports"

    id    =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False)
    object_key = Column(String(255), nullable=False)
    user_id  = Column(Integer,ForeignKey("users.id"),nullable=False)
    created_at= Column(DateTime, nullable=False)
    updated_at= Column(DateTime, nullable=False)



class db_program_categories(base): 

    __tablename__ = "Program_Categories"

    id    =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    category_id  = Column(Integer,ForeignKey ("Categories.id") , nullable=False)



class db_program_likes(base) : 
    __tablename__ = "Programs_likes"

    id    =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    user_id  = Column(Integer,ForeignKey ("users.id"), nullable=False)
    program_id = Column(Integer,ForeignKey ("Programs.id"), nullable=False)

class db_program_terms (base) :
     __tablename__ = "Programs_terms"

     id         =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False)  
     created_at = Column(DateTime, nullable=False)
     updated_at = Column(DateTime, nullable=False)
     term_id = Column(Integer,ForeignKey("terms.id"), nullable=False)
     program_id = Column(Integer,ForeignKey("users.id") ,nullable=False)

class db_programs (base) :
    __tablename__ = "Programs"

    id    =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False) 

    name = Column(String(255), nullable=False)
    degree_type  = Column(String(255), nullable=False)
    gpa_requirement = Column(String(255), nullable=False)
    cost_of_living_per_year = Column(Float, nullable=False)
    tuition = Column(String(255), nullable=False)
    one_time_charge = Column(Boolean, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    university_id = Column(Integer,ForeignKey("universities.id"), nullable=False)
    cost = Column(Float,  nullable=False)
    duration = Column(String(50), nullable=False)
    language_of_study = Column(String(50), nullable=False)
    min_tuition = Column(Float, nullable=False)
    max_tuition = Column(Float, nullable=False)
    sort_weight = Column(Integer, nullable=False, default= 0)
    brochure = Column(String(255), nullable=False)


class db_qas (base): 

    __tablename__ = "qas"

    id    =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False) 
    question   = Column(String(255), nullable=False)
    answer       = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

class db_sessions (base) : 

    __tablename__ = "sessions"

    session_id =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False) 
    data       = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, index=True)



  



class db_universities(base) :

    __tablename__ = "universities"

    id    =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False)
    city = Column(String(255), nullable=False)
    province = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    global_ranking = Column(Integer, nullable=False)
    student_population = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    grading_scale = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    gallery_images = Column(String(255))
    cover_image = Column(String(50), nullable=False)


class db_user_packages (base) :
     __tablename__ = "users_packages"

     id    =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False)

     name = Column(String(255), nullable=False)
     state = Column(String(255), nullable=False)
     cost = Column(Float, nullable=False)
     created_at  = Column(DateTime, nullable=False)
     updated_at  = Column(DateTime, nullable=False)
     user_id  = Column(Integer,ForeignKey ("users.id"), nullable=False)
     package_id = Column(Integer,ForeignKey ("Packages.id") ,nullable=False)
     order_id = Column(Integer,ForeignKey ("Orders.id") ,nullable=False)




class db_user_visas (base):


     __tablename__ = "users_visas"

     id    =  Column(Integer,primary_key=True,autoincrement=True, index=True, nullable=False)
     name = Column(String(255), nullable=False)
     country = Column(String(255), nullable=False)
     cost = Column(Float, nullable=False)
     state = Column(String(255), nullable=False)
     created_at  = Column(DateTime, nullable=False)
     updated_at  = Column(DateTime, nullable=False)
     user_id = Column(Integer,ForeignKey("users.id"), nullable=False)
     visa_id = Column(Integer,ForeignKey ("visas.id"), nullable=False)
     order_id = Column(Integer,ForeignKey ("Orders.id"), nullable=False)










base.metadata.drop_all(bind = engine)
base.metadata.create_all(bind = engine)