from flask import Flask, request

from service.load_data_generic import GenericService
from service.report import ReportService

app = Flask(__name__)

# enable debugging mode
app.config["DEBUG"] = True


@app.route("/jobs/load-data", methods=['POST'])
def jobsLoadData():
      col_names= ['id', 'job', 'upload_file_name']
      table_name = 'jobs'
      file = request.files['file']
      job = GenericService()
      response = job.loadData(file,col_names,table_name)
      return response

@app.route("/departments/load-data", methods=['POST'])
def departmentsLoadData():
      col_names= ['id', 'department', 'upload_file_name']
      table_name = 'departments'
      file = request.files['file']
      department = GenericService()
      response = department.loadData(file,col_names,table_name)
      return response

@app.route("/hired-employees/load-data", methods=['POST'])
def hiredEmployeesLoadData():
      col_names= ['id', 'name', 'hired_date','department_id','job_id','upload_file_name']
      table_name = 'hired_employees'
      file = request.files['file']
      employee = GenericService()
      response = employee.loadData(file,col_names,table_name)
      return response

@app.route("/jobs/hires_per_quarter", methods=['GET'])
def hiresPerQuarter():
      hiresPerQuarter = ReportService()
      response = hiresPerQuarter.readData("db\scripts\hires_per_quarter_2021.sql")
      return response

@app.route("/jobs/departments_mean_hires", methods=['GET'])
def departmentsMeanHires():
      hiresPerQuarter = ReportService()
      response = hiresPerQuarter.readData("db\scripts\departments_mean_hires_2021.sql")
      return response

if (__name__ == "__main__"):
     app.run(port = 5001)
