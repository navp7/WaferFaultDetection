import os


#AWS_S3_BUCKET_NAME = "wafer-fault"
MONGO_DATABASE_NAME = "ML"
MONGO_COLLECTION_NAME = "wafersensorfault"

TARGET_COLUMN = "quality"
UNWANTED_COL = ['Sensor-6', 'Sensor-14', 'Sensor-43', 'Sensor-50', 'Sensor-53', 'Sensor-70', 'Sensor-75', 'Sensor-98', 'Sensor-142', 'Sensor-150', 'Sensor-158', 'Sensor-159', 'Sensor-179', 'Sensor-180', 'Sensor-187', 'Sensor-190', 'Sensor-191', 'Sensor-192', 'Sensor-193', 'Sensor-194', 'Sensor-195', 'Sensor-207', 'Sensor-210', 'Sensor-227', 'Sensor-230', 'Sensor-231', 'Sensor-232', 'Sensor-233', 'Sensor-234', 'Sensor-235', 'Sensor-236', 'Sensor-237', 'Sensor-238', 'Sensor-241', 'Sensor-242', 'Sensor-243', 'Sensor-244', 'Sensor-257', 'Sensor-258', 'Sensor-259', 'Sensor-260', 'Sensor-261', 'Sensor-262', 'Sensor-263', 'Sensor-264', 'Sensor-265', 'Sensor-266', 'Sensor-267', 'Sensor-277', 'Sensor-285', 'Sensor-293', 'Sensor-294', 'Sensor-314', 'Sensor-315', 'Sensor-316', 'Sensor-323', 'Sensor-326', 'Sensor-327', 'Sensor-328', 'Sensor-329', 'Sensor-330', 'Sensor-331', 'Sensor-343', 'Sensor-348', 'Sensor-365', 'Sensor-370', 'Sensor-371', 'Sensor-372', 'Sensor-373', 'Sensor-374', 'Sensor-375', 'Sensor-376', 'Sensor-379', 'Sensor-380', 'Sensor-381', 'Sensor-382', 'Sensor-395', 'Sensor-396', 'Sensor-397', 'Sensor-398', 'Sensor-399', 'Sensor-400', 'Sensor-401', 'Sensor-402', 'Sensor-403', 'Sensor-404', 'Sensor-405', 'Sensor-415', 'Sensor-423', 'Sensor-450', 'Sensor-451', 'Sensor-452', 'Sensor-459', 'Sensor-462', 'Sensor-463', 'Sensor-464', 'Sensor-465', 'Sensor-466', 'Sensor-467', 'Sensor-479', 'Sensor-482', 'Sensor-499', 'Sensor-502', 'Sensor-503', 'Sensor-504', 'Sensor-505', 'Sensor-506', 'Sensor-507', 'Sensor-508', 'Sensor-509', 'Sensor-510', 'Sensor-513', 'Sensor-514', 'Sensor-515', 'Sensor-516', 'Sensor-529', 'Sensor-530', 'Sensor-531', 'Sensor-532', 'Sensor-533', 'Sensor-534', 'Sensor-535', 'Sensor-536', 'Sensor-537', 'Sensor-538', 'Sensor-539']
MONGO_DB_URL="mongodb+srv://navi:navimongodb@cluster0.0iyu8a9.mongodb.net/?retryWrites=true&w=majority"

#MODEL_FILE_NAME = "model"
#MODEL_FILE_EXTENSION = ".pkl"


#artifact_folder =  "artifacts"