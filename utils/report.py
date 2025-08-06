from fpdf import FPDF
import os

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Cancer Detection Report', 0, 1, 'C')

    def generate(self, patient_name, cancer_type, diagnosis, image_name):
        self.add_page()
        self.set_font("Arial", size=12)
        self.cell(0, 10, f"Patient Name: {patient_name}", ln=True)
        self.cell(0, 10, f"Cancer Type: {cancer_type}", ln=True)
        self.cell(0, 10, f"Diagnosis: {diagnosis}", ln=True)
        self.cell(0, 10, f"Image Analyzed: {image_name}", ln=True)

        file_path = f"static/reports/{patient_name.replace(' ', '_')}_report.pdf"
        self.output(file_path)
        return file_path

def generate_report(patient_name, cancer_type, diagnosis, image_name):
    pdf = PDFReport()
    return pdf.generate(patient_name, cancer_type, diagnosis, image_name)
