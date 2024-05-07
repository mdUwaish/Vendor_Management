Vendor Management System with Performance Metrics
This repository contains a Django-based Vendor Management System that facilitates vendor profile management, purchase order tracking, and vendor performance evaluation. The system is built using Django and Django REST Framework.

Core Features

1) Vendor Profile Management
Create, update, retrieve, and delete vendor profiles.
Track essential information such as name, contact details, address, and unique vendor code.
2) Purchase Order Tracking
Manage purchase orders with details like PO number, vendor reference, order date, items, quantity, and status.
Support CRUD operations for purchase orders and provide filtering options by vendor.
3) Vendor Performance Evaluation
Calculate various performance metrics for vendors:
-> On-Time Delivery Rate
-> Quality Rating Average
-> Average Response Time
-> Fulfillment Rate
Historical performance data is optionally stored for trend analysis.

API Endpoints

1) Vendors
POST /api/vendors/: Create a new vendor.
GET /api/vendors/: List all vendors.
GET /api/vendors/{vendor_id}/: Retrieve details of a specific vendor.
PUT /api/vendors/{vendor_id}/: Update a vendor's details.
DELETE /api/vendors/{vendor_id}/: Delete a vendor.
2) Purchase Orders
POST /api/purchase_order/: Create a new purchase order.
GET /api/purchase_order_all/: List all purchase orders with optional filtering by vendor name.
GET /api/purchase_order/id/: Retrieve details of a specific purchase order.
PUT /api/purchase_order/update/: Update a purchase order.
DELETE /api/purchase_order/delete/: Delete a purchase order.
3) Vendor Performance
GET /api/vendors/{vendor_id}/performance/: Retrieve performance metrics for a specific vendor.


Data Models


1) Vendor Model
Fields: name, contact_details, address, vendor_code, on_time_delivery_rate, quality_rating_avg, average_response_time, fulfillment_rate
2) Purchase Order Model
Fields: po_number, vendor, order_date, delivery_date, items, quantity, status, quality_rating, issue_date, acknowledgment_date
3) Historical Performance Model
Fields: vendor, date, on_time_delivery_rate, quality_rating_avg, average_response_time, fulfillment_rate

Technical Considerations

->Efficient Calculation: Optimized logic for metric calculations to handle large datasets.
->Data Integrity: Checks to handle missing data or division by zero.
->Real-time Updates: Utilize Django signals for real-time metric updates.

Technical Requirements

Latest stable version of Django and Django REST Framework.
Adherence to RESTful API design principles.
Comprehensive data validations for models.
Django ORM for database interactions.
Token-based authentication for securing API endpoints.
PEP 8 style guidelines for Python code.


Setup Instructions

Clone Repository:
bash
Copy code
git clone https://github.com/your_username/vendor-management-system.git
cd vendor-management-system
1) Setup Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

2) Install Dependencies:
pip install -r requirements.txt

3) Run Migrations:
python manage.py migrate

4) Start Development Server:
python manage.py runserver

5) Access API Endpoints:
Open a web browser or use tools like Postman to interact with the API endpoints.

6) Testing
Run the test suite to verify functionality and reliability:
python manage.py test
